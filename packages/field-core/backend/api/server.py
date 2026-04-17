from fastapi import FastAPI
from pydantic import BaseModel

from core.runtime import Runtime

app = FastAPI(title="field-core")

runtime = Runtime(agent_count=12)


class ConceptInput(BaseModel):
    concept: str
    steps: int = 6
    force_scale: float = 0.15


@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/state")
def get_state():
    return runtime.get_state()


@app.post("/step")
def step():
    runtime.step()
    return {
        "status": "ok",
        "step": runtime.steps,
        "field": runtime.field.get_state(),
    }


@app.post("/seed_concept")
def seed_concept(data: ConceptInput):
    result = runtime.apply_concept(
        concept=data.concept,
        steps=data.steps,
        force_scale=data.force_scale,
    )
    runtime.step()
    return {
        "status": "ok",
        "step": runtime.steps,
        "result": result,
        "field": runtime.field.get_state(),
    }
