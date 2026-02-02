import requests

BASE_URL = "https://swapi.dev/api"

def fetch_resource(resource, search=None):
    params = {}
    if search:
        params["search"] = search

    response = requests.get(f"{BASE_URL}/{resource}/", params=params)
    response.raise_for_status()
    return response.json()
