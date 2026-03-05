from text_curation.blocks import (
    UnicodeIntegrityBlock,
    EncodingRepairBlock,
    OCRSpacingRepairBlock,
    ColonSpacingRepairBlock,
    RedactionBlock,
    NormalizationBlockV2,
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
        "Production-grade web preprocessing pipeline. "
        "Preserves unicode punctuation, avoids stylistic punctuation "
        "rewriting, repairs OCR spacing artifacts, and uses safer "
        "paragraph reconstruction."
    ),

    blocks=[
        # ------------------------------------------------------------------
        # Unicode safety layer
        # ------------------------------------------------------------------
        UnicodeIntegrityBlock(),
        EncodingRepairBlock(),

        # OCR repair BEFORE whitespace normalization
        OCRSpacingRepairBlock(),

        # ------------------------------------------------------------------
        # Security redaction
        # ------------------------------------------------------------------
        RedactionBlock(),

        # ------------------------------------------------------------------
        # Safer normalization
        # ------------------------------------------------------------------
        NormalizationBlockV2(),

        # ------------------------------------------------------------------
        # HTML cleanup
        # ------------------------------------------------------------------
        HTMLStructureBlock(),

        # ------------------------------------------------------------------
        # Protect code formatting before paragraph logic
        # ------------------------------------------------------------------
        CodeSafeFormattingBlock(),

        # ------------------------------------------------------------------
        # Formatting repairs
        # ------------------------------------------------------------------
        ColonSpacingRepairBlock(),
        ParagraphFormattingBlockV2(),
        PunctuationQuoteRepairBlock(),

        # ------------------------------------------------------------------
        # Structural analysis
        # ------------------------------------------------------------------
        BasicStructureBlock(),

        # ------------------------------------------------------------------
        # Quality signals
        # ------------------------------------------------------------------
        QualitySignalBlock(),
        ExtendedQualityBlock(),
        TokenStatsBlock(),

        # ------------------------------------------------------------------
        # Deterministic document identity
        # ------------------------------------------------------------------
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
        "ocr_spacing_repaired": True,
        "secrets_redacted": True,
        "html_layout_removed": True,
        "structure_preserved": True,
        "code_safe": True,
        "analysis_signals_emitted": True,
        "dataset_level_filtering": False,
        "unicode_punctuation_preserved": True,
    },
)

register(PROFILE)
