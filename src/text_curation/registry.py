# Global registry mapping profile IDs to Profile instances.
# This registry is populated via import-time registration.
_PROFILES = {}


def register(profile):
    """
    Register a Profile instance globally.

    Profile IDs must be globally unique. Duplicate registration is a fatal error
    to preserve determinism and reproducibility.
    """
    if profile.id in _PROFILES:
        raise ValueError(
            f"Profile '{profile.id}' is already registered."
            "Profile IDs must be globally unique."
        )
    _PROFILES[profile.id] = profile


def get_profile(profile_id: str):
    """
    Retrieve a registered profile by its canonical ID.

    Profile resolution is trict:
    - IDs must match exactly
    - No fallbacks
    - No aliases
    - No defaults
    """

    if not isinstance(profile_id, str) or not profile_id.strip():
        raise TypeError("profile_id must br a non-empty string")

    try:
        return _PROFILES[profile_id]
    except KeyError:
        raise KeyError(
            f"Unknown profile: '{profile_id}'."
            "Profile IDs must be registered explicitly"
            )