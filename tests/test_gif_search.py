import pytest
from fastapi.testclient import TestClient
from app.api.routes.v1.gif_search import search_gifs
from app.core.db.models import GIF

client = TestClient(search_gifs)

@pytest.fixture
def gif_data():
    return [
        GIF(id=1, tags=["funny", "cat"]),
        GIF(id=2, tags=["funny", "dog"]),
        GIF(id=3, tags=["sad", "cat"]),
    ]

def test_successful_gif_search(gif_data, mocker):
    mocker.patch("app.api.routes.v1.gif_search.GIF.filter", return_value=gif_data)
    response = client.get("/search", params={"tags": ["funny"]})
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_no_gifs_found(gif_data, mocker):
    mocker.patch("app.api.routes.v1.gif_search.GIF.filter", return_value=[])
    response = client.get("/search", params={"tags": ["nonexistent"]})
    assert response.status_code == 404
    assert response.json() == {"detail": "No GIFs found for the given tags"}
