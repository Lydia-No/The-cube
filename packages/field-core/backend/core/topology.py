from core.math_utils import vector_distance


class Topology:
    def __init__(self):
        self.graph = {}
        self.threshold = 1.5

    def update(self, agents):
        self.graph = {}
        for a in agents:
            self.graph[a.id] = {}

        for a in agents:
            for b in agents:
                if a.id == b.id:
                    continue
                d = vector_distance(a.vector(), b.vector())
                if d < self.threshold:
                    self.graph[a.id][b.id] = d

    def clusters(self):
        visited = set()
        clusters = []

        for node in self.graph:
            if node in visited:
                continue

            stack = [node]
            group = []

            while stack:
                n = stack.pop()
                if n in visited:
                    continue
                visited.add(n)
                group.append(n)

                for neighbor in self.graph[n]:
                    stack.append(neighbor)

            clusters.append(group)

        return clusters
