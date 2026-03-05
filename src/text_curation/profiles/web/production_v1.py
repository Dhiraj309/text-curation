
from text_curation.blocks import (
    UnicodeIntegrityBlock,
    EncodingRepairBlock,
    OCRDigitRepairBlock,
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

from text_curation.blocks.filtering import BoilerplateDetectionBlock

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
        "Repairs encoding corruption, OCR artifacts, and structural noise "
        "while preserving natural language formatting and unicode punctuation."
    ),

    blocks=[
        # ------------------------------------------------------------------
        # Unicode safety layer
        # ------------------------------------------------------------------
        UnicodeIntegrityBlock(),
        EncodingRepairBlock(),

        # ------------------------------------------------------------------
        # OCR artifact repair
        # ------------------------------------------------------------------
        OCRDigitRepairBlock(),
        OCRSpacingRepairBlock(),

        # ------------------------------------------------------------------
        # Security redaction
        # ------------------------------------------------------------------
        RedactionBlock(
            policy={
                "redact_ip_addresses": True
            }
        ),

        # ------------------------------------------------------------------
        # Safe normalization layer
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
        # Boilerplate detection (signal only)
        # ------------------------------------------------------------------
        BoilerplateDetectionBlock(),

        # ------------------------------------------------------------------
        # Quality analysis
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
        "ocr_digit_repair": True,
        "ocr_spacing_repaired": True,
        "secrets_redacted": True,
        "html_layout_removed": True,
        "structure_preserved": True,
        "code_safe": True,
        "analysis_signals_emitted": True,
        "dataset_level_filtering": False,
        "unicode_punctuation_preserved": True,
        "boilerplate_detection": True,
    },
)

register(PROFILE)
