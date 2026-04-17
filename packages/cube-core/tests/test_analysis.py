from cube_explorer.attractors import run_concepts, score_histogram
from cube_explorer.core import CubeGraph
from cube_explorer.hamiltonian import generate_hamiltonian_paths


def test_run_concepts_returns_records():
    concepts = ["a", "b", "c"]
    results = run_concepts(concepts)
    assert len(results) == 3
    assert "concept" in results[0]
    assert "path" in results[0]
    assert "sequence" in results[0]
    assert "score" in results[0]


def test_score_histogram_returns_counter_like():
    concepts = ["a", "b", "c"]
    hist = score_histogram(concepts)
    assert sum(hist.values()) == 3


def test_hamiltonian_paths_from_zero():
    cube = CubeGraph()
    paths = generate_hamiltonian_paths(cube, start=0)
    assert len(paths) > 0
    for path in paths:
        assert len(path) == 8
        assert len(set(path)) == 8
        assert path[0] == 0
