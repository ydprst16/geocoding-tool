import pandas as pd
import time

from core.bounds import KECAMATAN_BOUNDS, KECAMATAN_NAMA
from core.cache import Cache
from core.geocoder import DumaiGeocoder

from pipeline.validator import validate_dataframe
from pipeline.counter import create_status_counter, update_counter

from utils.file_utils import get_next_output_filename
from config import INPUT_FILE, BASE_OUTPUT_FILE, CACHE_FILE, DELAY, SAVE_EVERY

from utils.logger import log_status


def run_geocode_pipeline(logger):
    df = pd.read_excel(INPUT_FILE)
    df = validate_dataframe(df)

    output_file = get_next_output_filename(BASE_OUTPUT_FILE)

    cache = Cache(CACHE_FILE)

    geocoder = DumaiGeocoder(
        cache,
        KECAMATAN_BOUNDS,
        KECAMATAN_NAMA,
        logger
    )

    status_counter = create_status_counter()

    logger.info(f"Total alamat: {len(df)}")

    for i, row in df.iterrows():
        alamat = str(row["alamat"]).strip()
        kode_kec = str(row["kode_kec"]).strip()

        if alamat == "" or alamat.lower() == "nan":
            df.at[i, "status"] = "EMPTY"
            update_counter(status_counter, "EMPTY")
            continue

        lat, lng, status = geocoder.geocode_dumai(alamat, kode_kec)

        df.at[i, "lat"] = lat
        df.at[i, "long"] = lng
        df.at[i, "status"] = status

        update_counter(status_counter, status)

        log_msg = f"{i+1}/{len(df)} → {alamat} | {status}"
        log_status(logger, log_msg, status)

        if (i + 1) % SAVE_EVERY == 0:
            df.to_excel(output_file, index=False)
            cache.save()
            logger.info(f"💾 Autosave {i+1}")

        time.sleep(DELAY)

    df.to_excel(output_file, index=False)
    cache.save()

    logger.info(f"Summary: {status_counter}")
    logger.info(f"✅ Done! File: {output_file}")