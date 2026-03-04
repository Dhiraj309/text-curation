import pytest

from text_curation.registry import register, get_profile
from text_curation.profiles.base import Profile


def test_duplicate_profile_registration_raises():
    """
    Profile canonical IDs must be globally unique.

    Registering two profiles with the same
    (domain, task, philosophy, version) must fail.
    """

    profile1 = Profile(
        domain="test",
        task="pretrain",
        philosophy="minimal",
        version="v1",
        blocks=[],
    )

    profile2 = Profile(
        domain="test",
        task="pretrain",
        philosophy="minimal",
        version="v1",
        blocks=[],
    )

    register(profile1)

    with pytest.raises(ValueError):
        register(profile2)


def test_profile_blocks_are_immutable():
    profile = Profile(
        domain="test",
        task="test",
        philosophy="test",
        version="v1",
        blocks=[],
    )

    with pytest.raises((TypeError, AttributeError)):
        profile.blocks.append("illegal")


def test_profile_name_is_immutable():
    """
    Canonical identifier components must be immutable.
    """

    profile = Profile(
        domain="test",
        task="test",
        philosophy="test",
        version="v1",
        blocks=[],
    )

    with pytest.raises(TypeError):
        profile.domain = "evil"


def test_profile_version_is_immutable():
    profile = Profile(
        domain="test",
        task="test",
        philosophy="test",
        version="v1",
        blocks=[],
    )

    with pytest.raises(TypeError):
        profile.version = "v999"
