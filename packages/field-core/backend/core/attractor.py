class Attractor:
    def __init__(self, position, strength=0.01):
        self.position = position
        self.strength = strength

    def influence(self, agent, dim_names):
        vec = agent.vector()
        for i, key in enumerate(dim_names):
            delta = self.position[i] - vec[i]
            agent.state[key] += delta * self.strength
