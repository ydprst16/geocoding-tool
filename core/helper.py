import re

def bersihkan_alamat(alamat):
    alamat = alamat.upper()
    alamat = re.sub(r"\s+", " ", alamat)
    alamat = alamat.replace(".", "")
    return alamat.strip()

def parse_bounds(bounds_str):
    sw, ne = bounds_str.split("|")
    s, w = map(float, sw.split(","))
    n, e = map(float, ne.split(","))
    return s, w, n, e

def point_in_bounds(lat, lng, bounds_str):
    s, w, n, e = parse_bounds(bounds_str)
    return s <= lat <= n and w <= lng <= e