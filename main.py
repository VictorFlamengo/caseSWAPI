import requests
import json

def search(request):
    params = request.args or {}
    type_ = params.get("type")
    name = params.get("name")

    if not type_:
        return (
            json.dumps({"error": "Parâmetro 'type' é obrigatório"}),
            400,
            {"Content-Type": "application/json"}
        )

    url = f"https://swapi.dev/api/{type_}/"

    try:
        response = requests.get(url, params={"search": name})
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return (
            json.dumps({"error": "Erro ao acessar a SWAPI"}),
            500,
            {"Content-Type": "application/json"}
        )

    return (
        json.dumps(response.json()),
        200,
        {"Content-Type": "application/json"}
    )
