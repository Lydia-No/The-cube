from pprint import pprint

from cube_explorer.attractors import group_by_start, score_histogram

concepts = [
    "collective intelligence",
    "symbolic AI",
    "graph theory",
    "creative algorithms",
    "recursive storytelling",
    "distributed cognition",
    "field memory",
    "hypercube ethics",
    "governance geometry",
    "state space resonance",
]

print("Score histogram:")
pprint(score_histogram(concepts))

print("\nGrouped by start vertex:")
grouped = group_by_start(concepts)
for start, items in grouped.items():
    print(f"\nStart {start}:")
    for item in items:
        print(" ", item["concept"], "| score:", item["score"], "| seq:", item["sequence"])
