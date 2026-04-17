from fastapi.testclient import TestClient

from api.server import app


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_state():
    response = client.get("/state")
    assert response.status_code == 200
    data = response.json()
    assert "field" in data
    assert "agents" in data
    assert "step" in data


def test_step():
    response = client.post("/step")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
