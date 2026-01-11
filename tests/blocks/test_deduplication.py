"""
Tests for paragraph-level exact deduplication.

These tests define the contract for DeduplicationBlock:
- Deduplication is paragraph-based
- Whitespace-normalized and case-insensitive
- First occurrence is preserved verbatim
"""

from text_curation._core.document import Document
from text_curation._blocks.deduplication import DeduplicationBlock

def dedupe(text):
    doc = Document(text)
    DeduplicationBlock().apply(doc)
    return doc.text

def text_exact_duplicate_paragraph_removed():
    text = "A paragraph.\n\nA paragraph."
    out = dedupe(text)

    assert out == "A paragraph."

def test_whitespace_variation_deduped():
    text = "A  paragraph.\n\nA paragraph."
    out = dedupe(text)

    assert out == "A  paragraph."

def test_case_insesitive_dedupe():
    text = "Hello World\n\nhello world"
    out = dedupe(text)

    assert out == "Hello World"

def test_non_duplicate_paragraphs_preserved():
    text = "Para one.\n\nPara two."
    out = dedupe(text)

    assert out == text

def test_empty_paragraphs_ignored():
    text = "\n\nA paragraph.\n\n\nA paragraph."
    out = dedupe(text)

    assert out == "A paragraph."