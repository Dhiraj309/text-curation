from text_curation.blocks import (
    NormalizationBlock,
    CodeSafeFormattingBlock,
    RedactionBlock,
)
from text_curation.profiles.base import Profile
from text_curation.registry import register


# Stable, general-purpose profile for heterogeneous web-derived text.
# This profile prioritizes determinism, safety, and semantic preservation.
PROFILE = Profile(
    name="llm_pretrain",
    version="v1",
    blocks=[
        # Redact sensitive information early to avoid downstream leakage
        RedactionBlock(),

        # Normalize Unicode and remove low-level encoding artifacts
        NormalizationBlock(),

        # Reconstruct readable paragraph and line structure
        CodeSafeFormattingBlock(),   # uses its own DEFAULT_POLICY
    ],
    guarantees = {
        # Reproducibility
        "deterministic": True,
        "order_independent": True,

        # Safety
        "secrets_redacted": True,
        "pii_removed": False,

        # Structure
        "structure_preserved": True,
        "layout_preserved": True,
        "code_safe": True,

        # Content policy
        "content_removed": False,
        "content_rewritten": False,

        # Repetition & dedup
        "deduplication": False,
        "repetition_preserved": True,

        # Semantics
        "semantic_filtering": False,
        "heuristic_scoring": False,
    },
)

# Register the profile at import time.
# This allows resolution via the global profile registry.
register(PROFILE)
