from fastapi import FastAPI
from core.runtime import Runtime

app = FastAPI(title="field-core")

runtime = Runtime(agent_count=12)


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
