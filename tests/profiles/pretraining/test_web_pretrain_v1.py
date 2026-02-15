from text_curation import TextCurator
from text_curation.core.reproducibility import compute_pipeline_hash

def test_web_pretrain_deterministic():
    curator = TextCurator.from_profile("web_pretrain_v1", collect_reports=True)

    text = "This is a test. This is only a test."

    output1 = curator({"text": [text]})
    output2 = curator({"text": [text]})

    assert output1 == output2

def test_web_pretrain_pipeline_hash_stable():
    from text_curation.registry import get_profile

    profile = get_profile("web_pretrain_v1")

    h1 = compute_pipeline_hash(profile)
    h2 = compute_pipeline_hash(profile)

    assert h1 == h2