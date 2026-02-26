import os

API_KEY = os.getenv("GOOGLE_API_KEY")

INPUT_FILE = "data/alamat.xlsx"
BASE_OUTPUT_FILE = "data/output/alamat_geo.xlsx"
CACHE_FILE = "data/geocode_cache.json"

DELAY = 0.5
SAVE_EVERY = 50

DUMAI_BOUNDS = "1.44722314,101.00929219|2.245761272,101.727404922"