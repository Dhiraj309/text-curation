from text_curation.blocks import (
    NormalizationBlock,
    CodeSafeFormattingBlock,
    RedactionBlock,
)
from text_curation.profiles.base import Profile
from text_curation.registry import register

PROFILE = Profile(
    name="llm_pretrain",
    version="v1",
    blocks=[
        RedactionBlock(),
        NormalizationBlock(),
        CodeSafeFormattingBlock(),
    ],
    guarantees={
        "deterministic": True,
        "explicit_block_order": True,
        "profile_id_fully_specifies_behavior": True,
        "no_hidden_global_state": True,
        "document_local_transforms_only": True,
    },
    behavior = {
        "secrets_redacted": True,
        "structure_preserved": True,
        "layout_preserved": True,
        "code_safe": True,
        "content_filtering_applied": False,
        "repetition_preserved": True,
        "semantic_filtering": False,
    },
)

# Register the profile at import time.
# This allows resolution via the global profile registry.
register(PROFILE)
