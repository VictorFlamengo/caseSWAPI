from app.logger import logger
from app.swapi_client import fetch_resource

def search_resource(resource_type, name=None, order="asc"):
    logger.info(
        f"Iniciando busca de recurso | tipo='{resource_type}' | filtro='{name}' | ordem='{order}'"
    )

    results = fetch_resource(resource_type)

    logger.debug(
        f"Total de registros retornados pela SWAPI antes do filtro: {len(results)}"
    )

    if name:
        results = [
            r for r in results
            if name.lower() in (r.get("name") or r.get("title", "")).lower()
        ]
        logger.info(
            f"Filtro aplicado pelo nome | resultados após filtro: {len(results)}"
        )

    results.sort(
        key=lambda r: (r.get("name") or r.get("title", "")).lower(),
        reverse=(order == "desc")
    )

    logger.info(
        f"Busca finalizada | tipo='{resource_type}' | total_resultados={len(results)}"
    )

    return {
        "count": len(results),
        "results": results
    }
