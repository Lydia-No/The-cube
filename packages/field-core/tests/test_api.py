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


def test_seed_concept():
    response = client.post(
        "/seed_concept",
        json={"concept": "symbolic AI", "steps": 6, "force_scale": 0.15},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"
    assert data["result"]["concept"] == "symbolic AI"
    assert len(data["result"]["raw_vector"]) == 6
