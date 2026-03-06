from text_curation.blocks import (
    NormalizationBlock,
    CodeSafeFormattingBlock,
    RedactionBlock,
)

from text_curation.analysis import FingerprintBlock

from text_curation.profiles.base import Profile
from text_curation.registry import register


PROFILE = Profile(
    domain="llm",
    task="pretrain",
    philosophy="minimal",
    version="v1",

    description="Minimal preprocessing profile for LLM pretraining pipelines",

    legacy_names=["llm_pretrain_v1"],

    blocks=[
        RedactionBlock(),
        NormalizationBlock(),
        CodeSafeFormattingBlock(),

        # Deterministic identity for corpus pipelines
        FingerprintBlock(),
    ],

    guarantees={
        "deterministic": True,
        "explicit_block_order": True,
        "profile_id_fully_specifies_behavior": True,
        "no_hidden_global_state": True,
        "document_local_transforms_only": True,
    },

    behavior={
        "secrets_redacted": True,
        "structure_preserved": True,
        "layout_preserved": True,
        "code_safe": True,
        "content_filtering_applied": False,
        "repetition_preserved": True,
        "semantic_filtering": False,
    },
)

register(PROFILE)
