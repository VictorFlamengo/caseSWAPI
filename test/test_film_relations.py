from app.services.film_relations import get_film_relations
from unittest.mock import patch

@patch("app.services.film_relations.fetch_resource")
def test_get_film_characters_success(mock_fetch):
    mock_fetch.side_effect = [
        [
            {
                "title": "A New Hope",
                "characters": ["https://swapi.dev/api/people/1/"],
                "planets": [],
                "starships": [],
                "vehicles": [],
                "species": []
            }
        ],
        {
            "name": "Luke Skywalker"
        }
    ]

    result = get_film_relations("A New Hope", "characters")

    assert result["film"] == "A New Hope"
    assert result["relation"] == "characters"
    assert result["count"] == 1
    assert result["results"][0]["name"] == "Luke Skywalker"
