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
    return runtime.get_state()


@app.post("/seed_concept")
def seed_concept(data: ConceptInput):
    result = runtime.apply_concept(
        concept=data.concept,
        steps=data.steps,
        force_scale=data.force_scale,
    )
    runtime.step()
    return {
        "result": result,
        "state": runtime.get_state(),
    }


@app.get("/timeline")
def timeline():
    return runtime.timeline.history


@app.get("/timeline/latest")
def timeline_latest(n: int = 10):
    return runtime.timeline.latest(n)
