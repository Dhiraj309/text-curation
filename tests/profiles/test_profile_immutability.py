import pytest
from text_curation.registry import get_profile

def test_profile_blocks_are_immutable():
    profile = get_profile("web_common_v1")

    with pytest.raises(TypeError):
        profile.blocks[0] = profile.blocks[0]

    with pytest.raises(AttributeError):
        profile.blocks.append(None)