from cube_explorer.core import CubeGraph, SymbolicWalker


def test_walk_lengths():
    cube = CubeGraph()
    walker = SymbolicWalker(cube)
    path, seq = walker.walk(0)
    assert len(path) == 7
    assert len(seq) == 6


def test_run_concept_shape():
    cube = CubeGraph()
    walker = SymbolicWalker(cube)
    start, path, seq, score = walker.run_concept("test")
    assert isinstance(start, int)
    assert len(path) == 7
    assert len(seq) == 6
    assert isinstance(score, int)
