import random

from core.hypercube import HypercubeField
from core.agent import Agent
from core.attractor import Attractor
from core.topology import Topology
from core.cube_bridge import CubeBridge
from core.timeline import Timeline


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

        self.bridge = CubeBridge()
        self.timeline = Timeline()

        self.last_concept = None
        self.last_cube_payload = None

    def choose_action(self, agent):
        coherence = agent.state["coherence"]
        entropy = agent.state["entropy"]

        if entropy > coherence + 0.1:
            return "stabilize"
        if coherence > entropy + 0.1:
            return "explore"
        return "expand"

    def apply_concept(self, concept, steps=6, force_scale=0.15):
        result = self.bridge.concept_vector(concept, steps=steps)
        vector = result["vector"]

        scaled = [v * force_scale for v in vector]
        self.field.add_external_force(scaled)

        self.last_concept = concept
        self.last_cube_payload = result["payload"]

        return {
            "concept": concept,
            "raw_vector": vector,
            "scaled_force": scaled,
            "cube": result["payload"],
        }

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

        # NEW: log timeline
        self.timeline.log(self.get_state())

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
            "last_concept": self.last_concept,
            "last_cube_payload": self.last_cube_payload,
        }
