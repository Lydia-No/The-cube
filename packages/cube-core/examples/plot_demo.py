from cube_explorer.core import CubeGraph, SymbolicWalker
from cube_explorer.visualization import plot_cube_walk

cube = CubeGraph()
walker = SymbolicWalker(cube)

start, path, seq, score = walker.run_concept("symbolic AI")

print("Start:", start)
print("Path:", path)
print("Sequence:", seq)
print("Score:", score)

fig = plot_cube_walk(path, title="Symbolic AI Walk")
fig.write_html("cube_walk.html")
print("Wrote cube_walk.html")
