from fastapi.testclient import TestClient
from main import app
import requests
from unittest.mock import patch

client = TestClient(app)

def test_read_status():
    response = client.get("/status")
    assert response.status_code, 200
    assert response.json, {"status":"ok"}