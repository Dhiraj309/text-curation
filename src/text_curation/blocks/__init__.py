"""
Public block API.

This module exposes all stable block implementations and defines
the canonical import surface for block composition in profiles.
"""

from .base import Block
from .normalization import (NormalizationBlock, EncodingRepairBlock, UnicodeIntegrityBlock)
from .formatting import (CodeSafeFormattingBlock, ParagraphFormattingBlock, HTMLStructureBlock, PunctuationQuoteRepairBlock)
from .redaction import RedactionBlock
from .structure import (BasicStructureBlock, CodeFenceDetector, HtmlCodeDetector)
from .filtering import (SignalBasedBoilerplateFilteringBlock, BoilerplateDetectionBlock, NavigationDetectionBlock)
from .deduplication import ExactParagraphDeduplicationBlock

# Explicit export list to keep the public API stable
__all__ = [
    "Block",
    "NormalizationBlock", "EncodingRepairBlock", "UnicodeIntegrityBlock",
    "CodeSafeFormattingBlock", "ParagraphFormattingBlock", "HTMLStructureBlock",
    "RedactionBlock",
    "BasicStructureBlock", "CodeFenceDetector", "HtmlCodeDetector",
    "SignalBasedBoilerplateFilteringBlock", "BoilerplateDetectionBlock", "NavigationDetectionBlock",
    "ExactParagraphDeduplicationBlock",
]
