"""
Signal-only analysis blocks.

This namespace contains deterministic metadata computation blocks
that emit signals but do not modify document text.
"""

from .base import AnalysisBlock
from .quality import QualitySignalBlock
from .fingerprint import FingerprintBlock

__all__ = [
    "AnalysisBlock",
    "QualitySignalBlock",
    "FingerprintBlock",
]