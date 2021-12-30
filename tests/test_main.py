from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Application Running!"}

def test_query():
    response = client.get("/test")
    assert response.status_code == 200