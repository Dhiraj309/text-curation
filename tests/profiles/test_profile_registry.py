import pytest

from text_curation.registry import register
from text_curation.profiles.base import Profile

def test_duplicate_profile_registration_raises():
    """
    Profile IDs must be globally unique.

    Registering two profiles with the same (name, version)
    must be immediately to prevent silent overrides.
    """
    profile1 = Profile(
        name="test_profile",
        version="v1",
        blocks=[],
    )

    profile2 = Profile(
        name="test_profile",
        version="v1",
        blocks=[],
    )

    register(profile1)

    with pytest.raises(ValueError):
        register(profile2)