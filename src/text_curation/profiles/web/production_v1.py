
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
        # 1. Text integrity layer
        # ------------------------------------------------------------------
        UnicodeIntegrityBlock(),
        EncodingRepairBlock(),

        # ------------------------------------------------------------------
        # 2. OCR artifact repair
        # ------------------------------------------------------------------
        OCRDigitRepairBlock(),
        OCRSpacingRepairBlock(),

        # ------------------------------------------------------------------
        # 3. Safe normalization
        # ------------------------------------------------------------------
        NormalizationBlockV2(),

        # ------------------------------------------------------------------
        # 4. Structural cleanup
        # HTML must be cleaned BEFORE redaction so placeholders
        # like <EMAIL> are not interpreted as HTML tags.
        # ------------------------------------------------------------------
        HTMLStructureBlock(),

        # ------------------------------------------------------------------
        # 5. Sensitive information redaction
        # ------------------------------------------------------------------
        RedactionBlock(
            policy={
                "redact_ip_addresses": True
            }
        ),

        # ------------------------------------------------------------------
        # 6. Code-safe formatting protection
        # ------------------------------------------------------------------
        CodeSafeFormattingBlock(),

        # ------------------------------------------------------------------
        # 7. Formatting repairs
        # ------------------------------------------------------------------
        ColonSpacingRepairBlock(),
        ParagraphFormattingBlockV2(),
        PunctuationQuoteRepairBlock(),

        # ------------------------------------------------------------------
        # 8. Structural analysis
        # ------------------------------------------------------------------
        BasicStructureBlock(),

        # ------------------------------------------------------------------
        # 9. Boilerplate detection (signals only)
        # ------------------------------------------------------------------
        BoilerplateDetectionBlock(),

        # ------------------------------------------------------------------
        # 10. Quality analysis
        # ------------------------------------------------------------------
        QualitySignalBlock(),
        ExtendedQualityBlock(),
        TokenStatsBlock(),

        # ------------------------------------------------------------------
        # 11. Deterministic fingerprinting
        # Must run last to guarantee reproducibility.
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
