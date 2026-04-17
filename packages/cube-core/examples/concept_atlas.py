from cube_explorer.core import CubeGraph, SymbolicWalker

concepts = [
    "collective intelligence",
    "symbolic AI",
    "graph theory",
    "creative algorithms",
    "recursive storytelling",
    "distributed cognition",
]

cube = CubeGraph()
walker = SymbolicWalker(cube)

for concept in concepts:
    start, path, seq, score = walker.run_concept(concept)
    print(concept)
    print("  start:", start)
    print("  path: ", path)
    print("  seq:  ", seq)
    print("  score:", score)
