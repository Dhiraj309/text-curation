import pytest
from text_curation.registry import get_profile


def test_profile_resolution_requires_exact_id():
    profile = get_profile("web_common_v1")

    # Alias resolves correctly but canonical ID is returned
    assert profile.id == "web.pretrain.structure_v1"


def test_profile_resolution_rejects_unknown_profile():
    with pytest.raises(KeyError):
        get_profile("web_common")


def test_profile_resolution_rejects_empty_string():
    with pytest.raises(TypeError):
        get_profile("")


def test_profile_resolution_rejects_non_string():
    with pytest.raises(TypeError):
        get_profile(None)
