import requests

def geocode(address, bounds, api_key):
    url = "https://maps.googleapis.com/maps/api/geocode/json"

    params = {
        "address": address,
        "bounds": bounds,
        "key": api_key
    }

    r = requests.get(url, params=params, timeout=10)
    return r.json()