from core.runtime import Runtime


def test_runtime_initial_state():
    runtime = Runtime(agent_count=4)
    state = runtime.get_state()
    assert state["step"] == 0
    assert len(state["agents"]) == 4
    assert "field" in state
    assert "clusters" in state


def test_runtime_step_increments():
    runtime = Runtime(agent_count=4)
    runtime.step()
    state = runtime.get_state()
    assert state["step"] == 1
    assert len(state["field"]["vector"]) == 6


def test_agents_have_vectors():
    runtime = Runtime(agent_count=3)
    state = runtime.get_state()
    for agent in state["agents"]:
        assert len(agent["vector"]) == 6
