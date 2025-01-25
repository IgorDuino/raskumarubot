import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_handle_telegram_update_successful(mocker):
    mocker.patch("app.api.routes.webhook.dp.feed_update", return_value={"status": "ok"})
    payload = {"update_id": 123456789, "message": {"message_id": 1, "from": {"id": 12345, "is_bot": False, "first_name": "Test", "username": "testuser"}, "chat": {"id": 12345, "first_name": "Test", "username": "testuser", "type": "private"}, "date": 1609459200, "text": "Hello"}}
    response = client.post(f"/webhook/telegram/{app.settings.TELEGRAM_BOT_TOKEN.get_secret_value()}", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_handle_telegram_update_bad_payload(mocker):
    mocker.patch("app.api.routes.webhook.dp.feed_update", return_value={"status": "ok"})
    payload = {"update_id": 123456789, "message": {"message_id": 1, "from": {"id": 12345, "is_bot": False, "first_name": "Test", "username": "testuser"}, "chat": {"id": 12345, "first_name": "Test", "username": "testuser", "type": "private"}, "date": 1609459200}}
    response = client.post(f"/webhook/telegram/{app.settings.TELEGRAM_BOT_TOKEN.get_secret_value()}", json=payload)
    assert response.status_code == 200
    assert response.json() == {"status": "error"}
