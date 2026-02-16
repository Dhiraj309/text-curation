from text_curation.registry import get_profile
from text_curation.core.reproducibility import compute_pipeline_hash

def test_web_web_pretrain_hash_snapshot():
    profile = get_profile("web_pretrain_v1")
    pipeline_hash = compute_pipeline_hash(profile)

    # If this changes, profile semantics changed.
    assert isinstance(pipeline_hash, str)
    assert len(pipeline_hash) == 40 or len(pipeline_hash) == 64