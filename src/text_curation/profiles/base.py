class Profile:
    """
    Immutable description of a text curation profile.

    A Profile defines:
    - a stable name and version
    - an ordered list of configured Blocks
    - declarative guarantees about behavior

    Profiles are treated as behavioral contracts.
    Once released, their semantics must not change.
    """

    _FROZEN_FIELDS = {"name", "version", "blocks"}

    def __init__(
        self,
        name: str,
        version: str,
        blocks: list,
        guarantees: dict | None = None,
        behavior: dict | None = None,
    ):
        """
        Create a new profile definition.

        Args:
            name: Logical profile name (e.g. "web_common")
            version: Explicit profile version (e.g. "v1")
            blocks: Ordered list of configured Block instances
            guarantees: Declarative, user-facing behavior guarantees
        """
        self.name = name
        self.version = version
        # Freeze block sequence to prevent mutation
        self.blocks = tuple(blocks)

        # Hard, encoded properties
        self.guarantees = dict(guarantees or {})

        # Descriptive, non-contractual properties
        self.behavior = dict(behavior or {})

        object.__setattr__(self, "_frozen", True)



    def __setattr__(self, key, value):
        if getattr(self, "_frozen", False) and key in self._FROZEN_FIELDS:
            raise TypeError(f"Profile attribute '{key}' is immutable")
        
        super().__setattr__(key, value)


    @property
    def id(self) -> str:
        """
        Canonical profile identifier.

        Combines name and version to ensure reproducibility
        (e.g. "web_common_v1").
        """
        return f"{self.name}_{self.version}"
    

    def __repr__(self) -> str:
        """
        Developer-friendly representation for debugging and logs.
        """
        return f"<Profile {self.id}>"
    
    
    def describe(self) -> dict:
        """
        Return a deterministic, insoectable description of the profile.

        This description is intended for auditing and provenance tracking.
        It does not affect execution behavior
        """
        return {
            "id": self.id,
            "name": self.name,
            "version": self.version,
            "blocks": [
                {
                    "type": block.__class__.__name__,
                    "policy": dict(block.policy)
                }
                for block in self.blocks
            ],
            "guarantees": dict(sorted(self.guarantees.items())),
            "behavior": dict(sorted(self.behavior.items()))
        }
