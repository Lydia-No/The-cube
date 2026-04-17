from collections import Counter

from .core import CubeGraph, SymbolicWalker


def run_concepts(concepts, steps=6):
    cube = CubeGraph()
    walker = SymbolicWalker(cube)

    results = []
    for concept in concepts:
        start = walker.concept_seed(concept)
        path, seq = walker.walk(start, steps=steps)
        score = walker.run_concept(concept, steps=steps)[3]
        results.append(
            {
                "concept": concept,
                "start": start,
                "path": path,
                "sequence": seq,
                "score": score,
            }
        )
    return results


def group_by_start(concepts, steps=6):
    grouped = {}
    for result in run_concepts(concepts, steps=steps):
        grouped.setdefault(result["start"], []).append(result)
    return grouped


def score_histogram(concepts, steps=6):
    results = run_concepts(concepts, steps=steps)
    return Counter(r["score"] for r in results)


def path_histogram(concepts, steps=6):
    results = run_concepts(concepts, steps=steps)
    return Counter(tuple(r["path"]) for r in results)
