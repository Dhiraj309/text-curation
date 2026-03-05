from text_curation.blocks import (
    UnicodeIntegrityBlock,
    EncodingRepairBlock,
    RedactionBlock,
    NormalizationBlock,
    CodeSafeFormattingBlock,
    ParagraphFormattingBlockV2,
    PunctuationQuoteRepairBlock,
    HTMLStructureBlock,
    BasicStructureBlock,
)

from text_curation.analysis import (
    QualitySignalBlock,
    ExtendedQualityBlock,
    TokenStatsBlock,
    FingerprintBlock,
)

from text_curation.profiles.base import Profile
from text_curation.registry import register


PROFILE = Profile(
    domain="web",
    task="pretrain",
    philosophy="production",
    version="v1",

    description=(
        "Production-grade web corpus preprocessing pipeline designed "
        "for large-scale LLM pretraining. Emphasizes unicode integrity, "
        "encoding repair, layout cleanup, structural preservation, and "
        "rich analysis signals."
    ),

    blocks=[
        # --- Unicode and encoding integrity ---
        UnicodeIntegrityBlock(),
        EncodingRepairBlock(),

        # --- Safety ---
        RedactionBlock(),

        # --- Low-level normalization ---
        NormalizationBlock(),

        # --- HTML artifact removal ---
        HTMLStructureBlock(),

        # --- Formatting preservation ---
        ParagraphFormattingBlockV2(),
        CodeSafeFormattingBlock(),

        # --- Repair formatting artifacts introduced by normalization ---
        PunctuationQuoteRepairBlock(),

        # --- Structural signals ---
        BasicStructureBlock(),

        # --- Quality analysis ---
        QualitySignalBlock(),
        ExtendedQualityBlock(),
        TokenStatsBlock(),

        # --- Deterministic document identity ---
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
    },

    behavior={
        "unicode_integrity_enforced": True,
        "encoding_repair": True,
        "secrets_redacted": True,
        "html_layout_removed": True,
        "structure_preserved": True,
        "code_safe": True,
        "analysis_signals_emitted": True,
        "dataset_level_filtering": False,
    },
)

# Register the profile at import time
register(PROFILE)
