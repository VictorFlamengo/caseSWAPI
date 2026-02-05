import json
from app.services.search import search_resource
from app.services.film_relations import get_film_relations

def search(request):
    args = request.args

    resource_type = args.get("type")
    name = args.get("name")
    order = args.get("order", "asc")

    if not resource_type:
        return {"error": "Parâmetro 'type' é obrigatório"}, 400

    if order not in ["asc", "desc"]:
        return {"error": "Parâmetro 'order' deve ser 'asc' ou 'desc'"}, 400

    try:
        result = search_resource(
            resource_type=resource_type,
            name=name,
            order=order
        )
        return result, 200  
    except Exception as e:
        return {"error": str(e)}, 500

def film_relations(request):
    film = request.args.get("film")
    relation = request.args.get("relation")
    name = request.args.get("name")

    if not film or not relation:
        return {
            "error": "Parâmetros obrigatórios: film e relation"
        }, 400

    return get_film_relations(film, relation, name), 200

