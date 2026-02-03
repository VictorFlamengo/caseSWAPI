from app.services.search import search_resource
from unittest.mock import patch


@patch("app.services.search.fetch_resource")
def test_search_resource_without_name(mock_fetch):
    mock_fetch.return_value = {
        "results": [
            {"name": "Luke Skywalker"},
            {"name": "Leia Organa"}
        ]
    }

    result = search_resource("people")

    assert result["count"] == 2
    assert result["results"][0]["name"] == "Luke Skywalker"
