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
    assert "field" in data
    assert "agents" in data
    assert "step" in data


def test_seed_concept():
    response = client.post(
        "/seed_concept",
        json={"concept": "symbolic AI", "steps": 6, "force_scale": 0.15},
    )
    assert response.status_code == 200
    data = response.json()
    assert "result" in data
    assert "state" in data
    assert data["result"]["concept"] == "symbolic AI"
    assert len(data["result"]["raw_vector"]) == 6
    assert "field" in data["state"]


def test_timeline_latest():
    client.post("/step")
    client.post("/step")
    response = client.get("/timeline/latest?n=2")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) <= 2
