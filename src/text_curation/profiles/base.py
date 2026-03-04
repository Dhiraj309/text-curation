class Profile:
    """
    Immutable description of a text curation profile.

    Profiles now support structured identifiers:

        domain.task.philosophy_vN

    Example:
        web.pretrain.structure_v1

    Backward compatibility with legacy profiles is preserved.
    """

    _FROZEN_FIELDS = {
        "domain",
        "task",
        "philosophy",
        "version",
        "blocks",
    }

    def __init__(
        self,
        *,
        # New structured metadata
        domain: str | None = None,
        task: str | None = None,
        philosophy: str | None = None,
        version: str,

        description: str | None = None,

        # Legacy compatibility
        name: str | None = None,

        # Core definition
        blocks: list,

        # Optional metadata
        guarantees: dict | None = None,
        behavior: dict | None = None,
        legacy_names: list[str] | None = None,
    ):
        """
        Create a new profile definition.

        Two modes are supported:

        1) Structured identifier (new)
            domain="web"
            task="pretrain"
            philosophy="structure"
            version="v1"

        2) Legacy identifier (old)
            name="web_common"
            version="v1"
        """

        # ------------------------------------------------------------------
        # Structured identifier mode
        # ------------------------------------------------------------------
        if domain and task and philosophy:
            self.domain = domain
            self.task = task
            self.philosophy = philosophy

        # ------------------------------------------------------------------
        # Legacy mode
        # ------------------------------------------------------------------
        elif name:
            # Map legacy name into structured namespace
            self.domain = "legacy"
            self.task = "legacy"
            self.philosophy = name

        else:
            raise ValueError(
                "Profile requires either structured fields "
                "(domain, task, philosophy) or legacy name."
            )

        self.version = version
        self.description = description or ""

        # Freeze block sequence
        self.blocks = tuple(blocks)

        self.guarantees = dict(guarantees or {})
        self.behavior = dict(behavior or {})

        self.legacy_names = list(legacy_names or [])

        object.__setattr__(self, "_frozen", True)

    def __setattr__(self, key, value):
        if getattr(self, "_frozen", False) and key in self._FROZEN_FIELDS:
            raise TypeError(f"Profile attribute '{key}' is immutable")

        super().__setattr__(key, value)

    @property
    def id(self) -> str:
        """
        Canonical profile identifier.

        Format:
            domain.task.philosophy_vN
        """

        return f"{self.domain}.{self.task}.{self.philosophy}_{self.version}"

    def __repr__(self) -> str:
        return f"<Profile {self.id}>"

    def describe(self) -> dict:
        """
        Deterministic profile description used for auditing.
        """

        return {
            "id": self.id,
            "domain": self.domain,
            "task": self.task,
            "philosophy": self.philosophy,
            "version": self.version,
            "description": self.description,
            "blocks": [
                {
                    "type": block.__class__.__name__,
                    "policy": dict(block.policy),
                }
                for block in self.blocks
            ],
            "guarantees": dict(sorted(self.guarantees.items())),
            "behavior": dict(sorted(self.behavior.items())),
        }
