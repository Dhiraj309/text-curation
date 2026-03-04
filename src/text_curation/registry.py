# Global registry mapping canonical profile IDs to Profile instances.
# Also supports legacy alias resolution.

_PROFILES = {}
_ALIASES = {}


def register(profile):
    """
    Register a Profile instance globally.

    Canonical profile IDs must be unique.
    Legacy aliases may map to canonical IDs.

    Re-registering the *same* profile object is allowed and ignored.
    """

    canonical_id = profile.id

    existing = _PROFILES.get(canonical_id)

    # Allow harmless duplicate imports of the same module
    if existing is profile:
        return

    # Detect real conflicts (two different objects with same ID)
    if existing is not None:
        raise ValueError(
            f"Profile '{canonical_id}' is already registered. "
            "Profile IDs must be globally unique."
        )

    _PROFILES[canonical_id] = profile

    # Register legacy aliases if present
    for alias in getattr(profile, "legacy_names", []):
        existing_alias = _ALIASES.get(alias)

        if existing_alias is not None and existing_alias != canonical_id:
            raise ValueError(
                f"Alias '{alias}' is already registered "
                f"for profile '{existing_alias}'."
            )

        _ALIASES[alias] = canonical_id


def get_profile(profile_id: str):
    """
    Retrieve a registered profile by ID.

    Resolution order:
    1) canonical profile ID
    2) legacy alias
    """

    if not isinstance(profile_id, str) or not profile_id.strip():
        raise TypeError("profile_id must be a non-empty string")

    # Canonical lookup
    profile = _PROFILES.get(profile_id)
    if profile is not None:
        return profile

    # Alias lookup
    canonical = _ALIASES.get(profile_id)
    if canonical is not None:
        return _PROFILES[canonical]

    raise KeyError(
        f"Unknown profile: '{profile_id}'. "
        "Profile IDs must be registered explicitly."
    )


def list_profiles():
    """
    Return sorted list of canonical profile IDs.
    """
    return sorted(_PROFILES.keys())


def describe_profile(profile_id: str):
    """
    Return deterministic metadata description of a profile.
    """
    profile = get_profile(profile_id)
    return profile.describe()
