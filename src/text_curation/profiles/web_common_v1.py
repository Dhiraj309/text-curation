"""
web_common_v1 profile.

This profile defines a conservative, general-purpose text curation
pipeline for web-scraped content. It is designed to improve readability,
remove sensitive data, and reduce obvious boilerplate while preserving
semantic content.

The pipeline is deterministic and suitable for large-scale dataset
processing.
"""

from text_curation._blocks import (
    NormalizationBlock,
    FilteringBlock,
    FormattingBlock,
    StructureBlock,
    RedactionBlock,
    DeduplicationBlock,
)

from text_curation._core.pipeline import Pipeline

PIPELINE = Pipeline(
    blocks = [
        RedactionBlock(),
        NormalizationBlock(),
        FormattingBlock(),
        StructureBlock(),
        FilteringBlock(),
        DeduplicationBlock(),
    ]
)