from cube_explorer.core import CubeGraph, SymbolicWalker


class CubeBridge:
    def __init__(self):
        self.cube = CubeGraph()
        self.walker = SymbolicWalker(self.cube)

    def concept_payload(self, concept, steps=6):
        start, path, sequence, score = self.walker.run_concept(concept, steps=steps)
        return {
            "concept": concept,
            "start": start,
            "path": path,
            "sequence": sequence,
            "score": score,
        }

    def concept_vector(self, concept, steps=6):
        payload = self.concept_payload(concept, steps=steps)

        path = payload["path"]
        score = payload["score"]
        unique_vertices = len(set(path))
        path_len = len(path)
        sequence_len = len(payload["sequence"])

        curiosity = min(2.0, unique_vertices / 4.0)
        stability = min(2.0, 1.0 + (score / 10.0))
        abstraction = min(2.0, (sum(path) / max(1, path_len)) / 3.5)
        depth = min(2.0, sequence_len / 6.0)
        entropy = min(2.0, (path_len - unique_vertices) / 3.0)
        coherence = min(2.0, score / 5.0)

        return {
            "payload": payload,
            "vector": [
                curiosity,
                stability,
                abstraction,
                depth,
                entropy,
                coherence,
            ],
        }
