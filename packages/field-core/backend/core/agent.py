import random

from core.math_utils import clamp


class Agent:
    def __init__(self, agent_id, field):
        self.id = agent_id
        self.field = field

        self.state = {
            "curiosity": random.random(),
            "stability": random.random(),
            "abstraction": random.random(),
            "depth": random.random(),
            "entropy": random.random(),
            "coherence": random.random(),
        }

        self.policy = {
            "expand": 0.5,
            "stabilize": 0.5,
            "explore": 0.5,
        }

        self.history = []

    def vector(self):
        return [self.state[k] for k in self.field.dimension_names]

    def apply_action(self, action):
        if action == "expand":
            self.state["entropy"] += 0.02
            self.state["curiosity"] += 0.01
        elif action == "stabilize":
            self.state["coherence"] += 0.02
            self.state["stability"] += 0.01
        elif action == "explore":
            self.state["abstraction"] += 0.02
            self.state["depth"] += 0.01

        for key in self.state:
            self.state[key] = clamp(self.state[key], 0.0, 2.0)

    def record(self):
        self.history.append(self.vector())
        if len(self.history) > 2000:
            self.history.pop(0)
