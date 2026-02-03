import json
from services.search import search_resource
from services.film_relations import get_film_relations

def search(request):
    args = request.args

    resource_type = args.get("type")
    name = args.get("name")

    if not resource_type:
        return {"error": "Parâmetro 'type' é obrigatório"}, 400

    try:
        result = search_resource(resource_type, name)
        return json.dumps(result), 200
    except Exception as e:
        return {"error": str(e)}, 500

def film_relations(request):
    film = request.args.get("film")
    relation = request.args.get("relation")

    if not film or not relation:
        return {
            "error": "Parâmetros obrigatórios: film e relation"
        }, 400

    return get_film_relations(film, relation)

