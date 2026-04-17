from cube_explorer.core import CubeGraph
from cube_explorer.hamiltonian import generate_hamiltonian_paths

cube = CubeGraph()
paths = generate_hamiltonian_paths(cube, start=0)

print("Hamiltonian path count from 0:", len(paths))
print("First 10 paths:")
for path in paths[:10]:
    print(path)
