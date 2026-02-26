from core.helper import bersihkan_alamat, point_in_bounds
from services.google_api import geocode
from config import API_KEY, DUMAI_BOUNDS
from core.bounds import KECAMATAN_BOUNDS, KECAMATAN_NAMA

class DumaiGeocoder:
    def __init__(self, cache, kecamatan_bounds, kecamatan_nama, logger=None):
        self.cache = cache
        self.kecamatan_bounds = kecamatan_bounds
        self.kecamatan_nama = kecamatan_nama
        self.logger = logger

    def geocode_dumai(self, alamat, kode_kec=None):
        alamat_clean = bersihkan_alamat(alamat)
        kode_kec = str(kode_kec)

        bounds = self.kecamatan_bounds.get(kode_kec, DUMAI_BOUNDS)
        nama_kec = self.kecamatan_nama.get(kode_kec, "")

        cache_key = f"{alamat_clean}|{kode_kec}"
        cached = self.cache.get(cache_key)

        if cached:
            if self.logger:
                self.logger.debug(f"Cache hit: {alamat_clean}")
            return cached

        # build query
        if nama_kec:
            query = f"{alamat_clean}, {nama_kec}, Dumai"
        else:
            query = f"{alamat_clean}, Dumai"

        # call Google API
        try:
            r = geocode(query, bounds, API_KEY)
        except Exception:
            return None, None, "ERROR_REQUEST"

        if r["status"] != "OK":
            return None, None, r["status"]

        result = r["results"][0]
        formatted_address = result["formatted_address"]

        # validasi harus Dumai
        if "Dumai" not in formatted_address:
            return None, None, "OUT_OF_DUMAI"

        location = result["geometry"]["location"]
        lat = location["lat"]
        lng = location["lng"]

        # validasi kecamatan bounds
        if not point_in_bounds(lat, lng, bounds):
            return None, None, "OUT_OF_KECAMATAN"

        # save cache
        self.cache.set(cache_key, (lat, lng, "SUCCESS"))

        return lat, lng, "SUCCESS"