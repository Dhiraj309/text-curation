"""
Public package interface for text-curation.

This module exposes the primary entry points intended for external use.
"""

from importlib.metadata import version

from .curator import TextCurator

__version__ = version("text_curation")

__all__ = ["TextCurator", "__version__ "]