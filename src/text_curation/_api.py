"""
Public API surface for text-curation.
Only symbols re-eported here are considered stable and supported.
All other imports are internal implementation details.
"""

from .curator import TextCurator
__all__ = [
    "TextCurator"
]