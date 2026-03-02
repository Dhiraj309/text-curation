from importlib.metadata import version as _version

# Ensure profiles are registered att import
import text_curation.profiles  # noqa: F401

from text_curation._api import TextCurator
from text_curation._api import CorpusPipeline

# Package version as published on PyPI
__version__ = _version("text_curation")

# Public API surface
__all__ = ["TextCurator", "CorpusPipeline", "__version__",]
