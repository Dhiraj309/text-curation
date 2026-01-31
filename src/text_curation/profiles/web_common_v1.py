from text_curation.blocks import (
    NormalizationBlock,
    CodeSafeFormattingBlock,
    ParagraphFormattingBlock,
    RedactionBlock,
    BasicStructureBlock,
    ExactParagraphDeduplicationBlock,
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

        # Maintains the code indenatation format
        CodeSafeFormattingBlock(),
        
        # Reconstruct readable paragraph and line structure
        ParagraphFormattingBlock(),

        # Emit structural signals without mutating text
        BasicStructureBlock(
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
        ExactParagraphDeduplicationBlock(
            policy={
        "scope": "paragraph",
        "normalize_case": True,
        "collapse_whitespace": True,
        "drop_empty": True,
    }
        ),
    ],
    guarantees = {
        "deterministic": True,
        "explicit_block_order": True,
        "profile_id_fully_specifies_behavior": True,
        "no_hidden_global_state": True,
        "document_local_transforms_only": True,
    },

    behavior = {
        "secrets_redacted": True,
        "structure_preserved": True,
        "layout_preserved": False,
        "code_safe": True,
        "content_filtering_applied": True,
        "repetition_preserved": False,
        "semantic_filtering": False,
    },
)

# Register the profile at import time.
# This allows resolution via the global profile registry.
register(PROFILE)
