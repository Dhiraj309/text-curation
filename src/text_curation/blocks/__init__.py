"""
Public block API.

This module exposes all stable block implementations and defines
the canonical import surface for block composition in profiles.
"""

from .base import Block
from .normalization import (NormalizationBlock, EncodingRepairBlock, UnicodeIntegrityBlock, NormalizationBlockV2, OCRSpacingRepairBlock)
from .formatting import (CodeSafeFormattingBlock, ParagraphFormattingBlock, HTMLStructureBlock, PunctuationQuoteRepairBlock, ParagraphFormattingBlockV2, ColonSpacingRepairBlock)
from .redaction import RedactionBlock
from .structure import (BasicStructureBlock, CodeFenceDetector, HtmlCodeDetector)
from .filtering import (SignalBasedBoilerplateFilteringBlock, BoilerplateDetectionBlock, NavigationDetectionBlock)
from .deduplication import ExactParagraphDeduplicationBlock

# Explicit export list to keep the public API stable
__all__ = [
    "Block",
    "NormalizationBlock", "EncodingRepairBlock", "UnicodeIntegrityBlock", "NormalizationBlockV2", "OCRSpacingRepairBlock",
    "CodeSafeFormattingBlock", "ParagraphFormattingBlock", "HTMLStructureBlock", "ParagraphFormattingBlockV2", "ColonSpacingRepairBlock",
    "RedactionBlock",
    "BasicStructureBlock", "CodeFenceDetector", "HtmlCodeDetector",
    "SignalBasedBoilerplateFilteringBlock", "BoilerplateDetectionBlock", "NavigationDetectionBlock",
    "ExactParagraphDeduplicationBlock",
]
