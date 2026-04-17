from core.math_utils import clamp, vector_add, random_vector


class HypercubeField:
    def __init__(self, dimensions=6):
        self.dimensions = dimensions
        self.dimension_names = [
            "curiosity",
            "stability",
            "abstraction",
            "depth",
            "entropy",
            "coherence",
        ]
        self.global_state = [0.5 for _ in range(dimensions)]
        self.drift_strength = 0.01
        self.history = []
        self.external_forces = []

    def add_external_force(self, vec):
        self.external_forces.append(vec)

    def project(self, agent):
        return [agent.state[k] for k in self.dimension_names]

    def apply_drift(self):
        drift = random_vector(self.dimensions, self.drift_strength)
        self.global_state = vector_add(self.global_state, drift)

    def apply_external_forces(self):
        for force in self.external_forces:
            self.global_state = vector_add(self.global_state, force)
        self.external_forces = []

    def normalize(self):
        self.global_state = [clamp(v, 0.0, 2.0) for v in self.global_state]

    def update(self, agents):
        if not agents:
            return

        avg = [0.0] * self.dimensions
        for agent in agents:
            vec = self.project(agent)
            for i in range(self.dimensions):
                avg[i] += vec[i]

        avg = [v / len(agents) for v in avg]
        self.global_state = avg

        self.apply_drift()
        self.apply_external_forces()
        self.normalize()

        self.history.append(self.global_state.copy())
        if len(self.history) > 1000:
            self.history.pop(0)

    def get_state(self):
        return {
            "dimensions": self.dimension_names,
            "vector": self.global_state,
            "history_length": len(self.history),
        }
