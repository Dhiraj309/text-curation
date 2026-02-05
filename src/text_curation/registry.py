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

    Raises:
        KeyError: if the profile is unknown or not registered
    """
    try:
        return _PROFILES[profile_id]
    except KeyError:
        raise KeyError(f"Unknown profile: {profile_id}")