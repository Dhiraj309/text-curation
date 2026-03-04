from text_curation.blocks import (
    RedactionBlock,
    NormalizationBlock,
    CodeSafeFormattingBlock,
    ParagraphFormattingBlock,
    BasicStructureBlock,
)

from text_curation.analysis import (
    QualitySignalBlock,
    TokenStatsBlock,
    FingerprintBlock,
)

from text_curation.profiles.base import Profile
from text_curation.registry import register


PROFILE = Profile(
    domain="web",
    task="pretrain",
    philosophy="minimal",
    version="v1",

    description="Minimal preprocessing pipeline for large-scale web pretraining",

    legacy_names=["web_pretrain_v1"],

    blocks=[
        # Safety
        RedactionBlock(),

        # Low-level normalization
        NormalizationBlock(),

        # Structural preservation
        CodeSafeFormattingBlock(),
        ParagraphFormattingBlock(),

        # Structural signals
        BasicStructureBlock(),

        # Quality analysis
        QualitySignalBlock(),
        TokenStatsBlock(),

        # Deterministic fingerprint
        FingerprintBlock(
            policy={
                "normalize_whitespace": False,
                "strip": False,
            }
        ),
    ],

    guarantees={
        "deterministic": True,
        "explicit_block_order": True,
        "profile_id_fully_specifies_behavior": True,
        "no_hidden_global_state": True,
        "document_local_transforms_only": True,
        "analysis_signal_only": True,
        "no_implicit_filtering": True,
    },

    behavior={
        "secrets_redacted": True,
        "structure_preserved": True,
        "layout_preserved": False,
        "code_safe": True,
        "analysis_signals_emitted": True,
        "dataset_level_filtering": False,
    },
)

register(PROFILE)
