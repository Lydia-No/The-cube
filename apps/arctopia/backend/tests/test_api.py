from fastapi.testclient import TestClient
from api.server import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_case_and_event_flow():
    create_case = client.post(
        "/cases",
        json={"title": "Fen Pilot", "description": "Strategic mineral governance case"},
    )
    assert create_case.status_code == 200
    case = create_case.json()
    case_id = case["id"]

    event1 = client.post(
        "/events",
        json={
            "case_id": case_id,
            "stage": "activity",
            "title": "Pilot started",
            "content": "Initial extraction activity registered.",
        },
    )
    assert event1.status_code == 200

    event2 = client.post(
        "/events",
        json={
            "case_id": case_id,
            "stage": "evidence",
            "title": "Sensor upload",
            "content": "Baseline environmental measurements uploaded.",
        },
    )
    assert event2.status_code == 200

    snapshot = client.get(f"/cases/{case_id}/snapshot")
    assert snapshot.status_code == 200
    data = snapshot.json()
    assert data["event_count"] == 2
    assert data["current_stage"] == "evidence"


def test_sequence_violation():
    create_case = client.post(
        "/cases",
        json={"title": "Sequence Test", "description": ""},
    )
    case_id = create_case.json()["id"]

    bad_event = client.post(
        "/events",
        json={
            "case_id": case_id,
            "stage": "verification",
            "title": "Too early",
            "content": "Trying to jump ahead.",
        },
    )
    assert bad_event.status_code == 400
