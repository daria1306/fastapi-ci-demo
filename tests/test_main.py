from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert r.json() == {"message": "Hello, CI!"}


def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"


def test_sum():
    r = client.get("/sum?a=2&b=3")
    assert r.status_code == 200
    assert r.json()["result"] == 5