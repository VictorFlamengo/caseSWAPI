import json
from services.search import search_resource

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
