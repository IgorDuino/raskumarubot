import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_successful_ping():
    response = client.get("/ping", headers={"X-TG-INIT-DATA": "valid_init_data"})
    assert response.status_code == 200
    assert response.json() == {"ping": "pong!"}

def test_unauthorized_ping():
    response = client.get("/ping", headers={"X-TG-INIT-DATA": "invalid_init_data"})
    assert response.status_code == 401
    assert response.json() == {"detail": "User unauthorized"}
