"""
Public block API.

This module exposes all stable block implementations and defines
the canonical import surface for block composition in profiles.
"""

from .base import Block
from .normalization import NormalizationBlock
from .formatting import FormattingBlock
from .redaction import RedactionBlock
from .structure import StructureBlock
from .filtering import FilteringBlock
from .deduplication import DeduplicationBlock

# Explicit export list to keep the public API stable
__all__ = [
    "Block",
    "NormalizationBlock",
    "FormattingBlock",
    "RedactionBlock",
    "StructureBlock",
    "FilteringBlock",
    "DeduplicationBlock",
]