from app.swapi_client import fetch_resource
from app.logger import logger

VALID_RELATIONS = {
    "characters",
    "planets",
    "starships",
    "vehicles",
    "species"
}

def get_film_relations(film_name: str, relation: str, name: str | None = None):
    logger.info(
        f"Iniciando busca de relações do filme | filme='{film_name}' | relação='{relation}' | filtro={repr(name)}"
    )

    if relation not in VALID_RELATIONS:
        logger.warning(
            f"Relação inválida solicitada: '{relation}'. Relações válidas: {VALID_RELATIONS}"
        )
        return {
            "error": f"Relação inválida. Use uma de: {list(VALID_RELATIONS)}"
        }

    logger.info("Buscando lista de filmes na SWAPI")
    
    films = fetch_resource("films")

    logger.debug(f"Total de filmes retornados: {len(films)}")

    film = next(
        (f for f in films if f["title"].lower() == film_name.lower()),
        None
    )

    if not film:
        logger.warning(f"Filme não encontrado: '{film_name}'")
        return {"error": f"Filme '{film_name}' não encontrado"}

    logger.info(f"Filme encontrado: '{film['title']}'")

    urls = film.get(relation, [])
    logger.info(
        f"Total de itens relacionados encontrados ({relation}): {len(urls)}"
    )

    results = []

    for url in urls:
        logger.debug(f"Buscando recurso relacionado: {url}")

        data = fetch_resource(url, absolute_url=True)

        if not isinstance(data, dict):
            logger.error(f"Resposta inesperada da SWAPI: {data}")
            continue

        item_name = data.get("name") or data.get("title")
        results.append({
            "name": item_name,
            "url": url
        })

    # Filtrar por nome se fornecido
    if name:
        logger.info(f"Aplicando filtro de nome: '{name}'")
        results = [
            r for r in results
            if name.lower() in r.get("name", "").lower()
        ]
        logger.info(
            f"Filtro aplicado pelo nome | resultados após filtro: {len(results)}"
        )
    else:
        logger.info("Nenhum filtro de nome fornecido")

    logger.info(
        f"Processamento finalizado | filme='{film['title']}' | relação='{relation}' | filtro_nome='{name}' | total={len(results)}"
    )

    return {
        "film": film["title"],
        "relation": relation,
        "count": len(results),
        "results": results
    }
