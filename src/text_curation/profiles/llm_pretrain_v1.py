"""
Backward compatibility shim for legacy import path.

Old:
    text_curation.profiles.llm_pretrain_v1

New:
    text_curation.profiles.llm.minimal_v1
"""

from text_curation.profiles.llm.minimal_v1 import PROFILE

__all__ = ["PROFILE"]
