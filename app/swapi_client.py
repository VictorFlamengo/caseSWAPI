import requests

BASE_URL = "https://swapi.dev/api/"

def fetch_resource(resource: str, params=None, absolute_url=False):
    if absolute_url:
        url = resource
    else:
        url = f"{BASE_URL}{resource}/"

    response = requests.get(url, params=params)
    response.raise_for_status()
    return response.json()
