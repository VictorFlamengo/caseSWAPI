from swapi_client import fetch_resource

def search_resource(resource_type, name=None):
    data = fetch_resource(resource_type, search=name)
    return data.get("results", [])
