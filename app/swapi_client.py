import requests

BASE_URL = "https://swapi.dev/api/"

def fetch_resource(resource: str, params=None, absolute_url=False):
    if absolute_url:
        response = requests.get(resource)
        response.raise_for_status()
        return response.json()

    url = f"{BASE_URL}{resource}/"
    results = []
    is_first_request = True

    while url:
        response = requests.get(url, params=params if is_first_request else None)
        response.raise_for_status()

        data = response.json()

        if isinstance(data, dict) and "results" in data:
            results.extend(data["results"])
            url = data.get("next")
            is_first_request = False
            continue

        return data

    return results
