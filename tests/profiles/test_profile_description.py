from text_curation.registry import get_profile


def test_profile_description_is_deterministic_and_complete():
    profile = get_profile("web_common_v1")
    desc = profile.describe()

    # Canonical profile ID
    assert desc["id"] == "web.pretrain.structure_v1"

    assert desc["domain"] == "web"
    assert desc["task"] == "pretrain"
    assert desc["philosophy"] == "structure"
    assert desc["version"] == "v1"

    assert isinstance(desc["blocks"], list)
    assert len(desc["blocks"]) > 0

    for block in desc["blocks"]:
        assert "type" in block
        assert "policy" in block
        assert isinstance(block["policy"], dict)


def test_profile_description_are_deterministic_and_comparable():
    """
    Profiles with identical definitions must produce identical
    descriptions, regardless of construction order.
    """
    from text_curation.profiles.base import Profile
    from text_curation.blocks import NormalizationBlock, RedactionBlock

    p1 = Profile(
        domain="test",
        task="test",
        philosophy="determinism",
        version="v1",
        blocks=[
            RedactionBlock(policy={"a": 1, "b": 2}),
            NormalizationBlock(policy={"x": 9, "y": 8}),
        ],
        guarantees={"deterministic": True, "explicit": True},
        behavior={"semantic": False, "filtering": False},
    )

    p2 = Profile(
        domain="test",
        task="test",
        philosophy="determinism",
        version="v1",
        blocks=[
            RedactionBlock(policy={"b": 2, "a": 1}),
            NormalizationBlock(policy={"y": 8, "x": 9}),
        ],
        guarantees={"explicit": True, "deterministic": True},
        behavior={"filtering": False, "semantic": False},
    )

    assert p1.describe() == p2.describe()
