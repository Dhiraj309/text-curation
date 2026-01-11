"""
Tests for paragraph-level filtering behavior.

FilteringBlock:
- Drops empty documents
- Drops short repeated boilerplate paragraphs
- Never drops header-led structural sections
"""

from text_curation._core.document import Document
from text_curation._blocks.filtering import FilteringBlock

def run_filter(text, signals):
    """Apply filtering with pre-attached signals."""
    doc = Document(text)
    doc.signals = signals
    FilteringBlock().apply(doc)

    return doc.text

def test_drops_empty_document():
    text = "  \n\n  "
    out = run_filter(text, [])

    assert out == ""

def test_drops_boilerplate_paragraphs():
    text = "Menu Home About\n\nReal content here."
    signals = [
        type("S", (), {
            "name": "paragraph[0].is_boilerplate_candidate",
            "value": True
        }),
        type("S", (), {
            "name": "paragraph[0].repetition_count",
            "value": 3
        }),
    ]

    out = run_filter(text, signals)
    assert out.strip() == "Real content here."

def test_keeps_non_boilerplate_paragraph():
    text = "IMport article paragraphs."
    signals = [
        type("S", (), {
            "name": "paragraph[0].is_biolerplate_candidate",
            "value": False
           }),
    ]

    out = run_filter(text, signals)
    assert out.strip() == text

def text_drops_list_block():
    text = "- item one\n- item two\n- item three\n\nMain article text"
    signals = [
        type("S", (), {
            "name": "paragraph[0].is_list_block",
            "value": True
        }),
    ]

    out = run_filter(text, signals)
    assert out.strip() == "Main article text."