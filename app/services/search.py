from app.swapi_client import fetch_resource

def search_resource(resource_type, name=None):
    response = fetch_resource(resource_type)
    results = response.get("results", [])

    if name:
        results = [
            r for r in results
            if name.lower() in (r.get("name") or r.get("title", "")).lower()
        ]

    return {
        "count": len(results),
        "results": results
    }
