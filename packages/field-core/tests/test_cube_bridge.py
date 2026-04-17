from core.cube_bridge import CubeBridge


def test_concept_payload_shape():
    bridge = CubeBridge()
    payload = bridge.concept_payload("symbolic AI")
    assert payload["concept"] == "symbolic AI"
    assert len(payload["path"]) == 7
    assert len(payload["sequence"]) == 6
    assert isinstance(payload["score"], int)


def test_concept_vector_shape():
    bridge = CubeBridge()
    result = bridge.concept_vector("symbolic AI")
    assert "payload" in result
    assert "vector" in result
    assert len(result["vector"]) == 6
