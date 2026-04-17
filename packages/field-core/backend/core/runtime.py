import random

from core.hypercube import HypercubeField
from core.agent import Agent
from core.attractor import Attractor
from core.topology import Topology


class Runtime:
    def __init__(self, agent_count=12):
        self.field = HypercubeField()
        self.agents = [Agent(i, self.field) for i in range(agent_count)]
        self.attractors = [
            Attractor(
                [random.random() for _ in range(self.field.dimensions)],
                strength=0.01,
            )
        ]
        self.topology = Topology()
        self.steps = 0

    def choose_action(self, agent):
        coherence = agent.state["coherence"]
        entropy = agent.state["entropy"]

        if entropy > coherence + 0.1:
            return "stabilize"
        if coherence > entropy + 0.1:
            return "explore"
        return "expand"

    def step(self):
        for agent in self.agents:
            action = self.choose_action(agent)
            agent.apply_action(action)

            for attractor in self.attractors:
                attractor.influence(agent, self.field.dimension_names)

            agent.record()

        self.field.update(self.agents)
        self.topology.update(self.agents)
        self.steps += 1

    def get_state(self):
        return {
            "step": self.steps,
            "field": self.field.get_state(),
            "agents": [
                {
                    "id": a.id,
                    "state": a.state,
                    "vector": a.vector(),
                    "history_length": len(a.history),
                }
                for a in self.agents
            ],
            "topology": self.topology.graph,
            "clusters": self.topology.clusters(),
        }
