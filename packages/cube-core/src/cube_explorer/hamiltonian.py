class HamiltonianExplorer:
    def __init__(self, adjacency):
        self.adjacency = adjacency

    def find_paths(self, start=None):
        starts = [start] if start is not None else list(self.adjacency.keys())
        all_paths = []

        for s in starts:
            self._dfs([s], {s}, all_paths)

        unique = []
        seen = set()

        for path in all_paths:
            key = tuple(path)
            if key not in seen:
                seen.add(key)
                unique.append(path)

        return unique

    def _dfs(self, path, visited, all_paths):
        if len(path) == len(self.adjacency):
            all_paths.append(path[:])
            return

        current = path[-1]
        for neighbor in self.adjacency[current]:
            if neighbor not in visited:
                visited.add(neighbor)
                path.append(neighbor)
                self._dfs(path, visited, all_paths)
                path.pop()
                visited.remove(neighbor)


def generate_hamiltonian_paths(cube, start=None):
    explorer = HamiltonianExplorer(cube.vertex_neighbors)
    return explorer.find_paths(start=start)
