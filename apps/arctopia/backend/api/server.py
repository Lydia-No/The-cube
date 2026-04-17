from fastapi import FastAPI, HTTPException

from core.models import CreateCaseInput, CreateEventInput
from core.service import ArcService

app = FastAPI(title="ArcTopia")
service = ArcService()


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/cases")
def list_cases():
    return [case.model_dump() for case in service.list_cases()]


@app.post("/cases")
def create_case(data: CreateCaseInput):
    try:
        case = service.create_case(data)
        return case.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/cases/{case_id}")
def get_case(case_id: str):
    case = service.get_case(case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found.")
    return case.model_dump()


@app.get("/cases/{case_id}/events")
def list_case_events(case_id: str):
    case = service.get_case(case_id)
    if not case:
        raise HTTPException(status_code=404, detail="Case not found.")
    return [event.model_dump() for event in service.list_case_events(case_id)]


@app.post("/events")
def create_event(data: CreateEventInput):
    try:
        event = service.create_event(data)
        return event.model_dump()
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


@app.get("/cases/{case_id}/snapshot")
def case_snapshot(case_id: str):
    try:
        return service.case_snapshot(case_id)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
