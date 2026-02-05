from text_curation.registry import get_profile

def test_profile_description_is_deterministic_and_complete():
    profile = get_profile("web_common_v1")
    desc = profile.describe()

    assert desc["id"] == "web_common_v1"
    assert desc["name"] == "web_common"
    assert desc["version"] == "v1"

    assert isinstance(desc["blocks"], list)
    assert len(desc["blocks"]) > 0

    for block in desc["blocks"]:
        assert "type" in block
        assert "policy" in block
        assert isinstance(block["policy"], dict)