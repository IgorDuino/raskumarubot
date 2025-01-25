import pytest
from httpx import AsyncClient
from app.main import app

@pytest.mark.asyncio
async def test_health_endpoint_success():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "health": "ok",
        "status": {
            "database": True,
            "redis": True,
            "api": True
        }
    }

@pytest.mark.asyncio
async def test_health_endpoint_partial():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert response.status_code == 200
    assert response.json() == {
        "health": "partial",
        "status": {
            "database": False,
            "redis": True,
            "api": True
        }
    }
