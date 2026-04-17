from cube_explorer.core import CubeGraph, SymbolicWalker

cube = CubeGraph()
walker = SymbolicWalker(cube)

start, path, seq, score = walker.run_concept("test")

print("Start:", start)
print("Path:", path)
print("Sequence:", seq)
print("Score:", score)
