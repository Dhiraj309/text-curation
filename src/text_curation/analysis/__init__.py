"""
Signal-only analysis blocks.

This namespace contains deterministic metadata computation blocks
that emit signals but do not modify document text.
"""

from .base import AnalysisBlock
from .quality import QualitySignalBlock
from .fingerprint import FingerprintBlock
from .token_stats import TokenStatsBlock
from .language import LanguageDetectionBlock
from .extended_quality import ExtendedQualityBlock

__all__ = [
    "AnalysisBlock",
    "QualitySignalBlock",
    "FingerprintBlock",
    "TokenStatsBlock",
    "LanguageDetectionBlock",
    "ExtendedQualityBlock",
]
