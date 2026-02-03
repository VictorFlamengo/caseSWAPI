from app.swapi_client import fetch_resource

VALID_RELATIONS = {
    "characters",
    "planets",
    "starships",
    "vehicles",
    "species"
}

def get_film_relations(film_name: str, relation: str):
    if relation not in VALID_RELATIONS:
        return {
            "error": f"Relação inválida. Use uma de: {list(VALID_RELATIONS)}"
        }

    films_response = fetch_resource("films")
    films = films_response.get("results", [])

    film = next(
        (f for f in films if f["title"].lower() == film_name.lower()),
        None
    )

    if not film:
        return {"error": f"Filme '{film_name}' não encontrado"}

    urls = film.get(relation, [])

    results = []

    for url in urls:
        data = fetch_resource(url, absolute_url=True)

        results.append({
            "name": data.get("name") or data.get("title"),
            "url": url
        })

    return {
        "film": film["title"],
        "relation": relation,
        "count": len(results),
        "results": results
    }
