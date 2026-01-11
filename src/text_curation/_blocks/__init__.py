"""
Public block interfaces for text-curation.

This module exposes the canonical set of transformation blocks
used to construct curation pipelines and profiles.
"""

from .deduplication import DeduplicationBlock
from .filtering import FilteringBlock
from . formatting import FormattingBlock
from .normalization import NormalizationBlock
from .redaction import RedactionBlock
from .structure import StructureBlock