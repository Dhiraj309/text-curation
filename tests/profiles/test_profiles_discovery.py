from text_curation.registry import get_profile

def test_profiles_are_discoverable_deterministically():
    """
    Built-in profiles must always be registered after import,
    regardless of filesystem or environment ordering.
    """
    assert get_profile("web_common_v1").id == "web_common_v1"
    assert get_profile("llm_pretrain_v1").id == "llm_pretrain_v1"