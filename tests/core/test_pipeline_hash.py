from text_curation.profiles.llm_pretrain_v1 import PROFILE as P1
from text_curation.core.reproducibility import compute_pipeline_hash

def test_pipeline_hash_deterministic():
    h1 = compute_pipeline_hash(P1)
    h2 = compute_pipeline_hash(P1)

    assert h1 == h2

def test_pipeline_hash_changes_with_policy():
    from text_curation.profiles.base import Profile
    from text_curation.blocks import RedactionBlock

    profile_a = Profile(
        name="test",
        version="v1",
        blocks=[RedactionBlock(policy={"a": 1})],
    )

    profile_b = Profile(
        name="test",
        version="v1",
        blocks=[RedactionBlock(policy={"a": 2})],
    )

    h1 = compute_pipeline_hash(profile_a)
    h2 = compute_pipeline_hash(profile_b)

    h1 != h2
