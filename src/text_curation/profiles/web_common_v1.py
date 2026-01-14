from text_curation.blocks import (
    NormalizationBlock,
    FormattingBlock,
    RedactionBlock,
    StructureBlock,
    FilteringBlock,
    DeduplicationBlock,
)
from text_curation.profiles.base import Profile
from text_curation.registry import register


# Stable, general-purpose profile for heterogeneous web-derived text.
# This profile prioritizes determinism, safety, and semantic preservation.
PROFILE = Profile(
    name="web_common",
    version="v1",
    blocks=[
        # Redact sensitive information early to avoid downstream leakage
        RedactionBlock(),

        # Normalize Unicode and remove low-level encoding artifacts
        NormalizationBlock(),

        # Reconstruct readable paragraph and line structure
        FormattingBlock(),   # uses its own DEFAULT_POLICY

        # Emit structural signals without mutating text
        StructureBlock(
            policy={
                "detect_headers": True,
                "detect_lists": True,
                "detect_all_caps": True,
                "short_line_threshold": 20,
                "list_block_threshold": 0.5,
                "min_repetition_for_boilerplate": 2,
            }
        ),

        # Conservatively drop empty or repeated short boilerplate paragraphs
        FilteringBlock(
            policy={
                "drop_empty": True,
                "preserve_headers": True,
                "drop_repeated_boilerplate": True,
                "min_repetition": 2,
                "max_boilerplate_length": 200,
            }
        ),

        # Remove exact duplicate paragraphs while preserving order
        DeduplicationBlock(
            policy={
                "scope": "paragraph",
                "normalize_case": True,
                "collapse_whitespace": True,
                "drop_empty": True,
            }
        ),
    ],
    guarantees={
        # Behavioral guarantees exposed to users
        "deterministic": True,
        "secrets_redacted": True,
        "layout_preserved": False,
        "code_safe": False,
        "semantic_filtering": False,
    },
)

# Register the profile at import time.
# This allows resolution via the global profile registry.
register(PROFILE)