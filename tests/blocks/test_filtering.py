"""
Tests for paragraph-level filtering behavior.

SignalBasedBoilerplateFilteringBlock:
- Drops empty documents (configurable)
- Drops short repeated boilerplate paragraphs (configurable)
- Never drops header-led structural sections (configurable)
- All behavior must be driven by explicit policy
"""

from text_curation.core.document import Document
from text_curation.blocks.filtering import SignalBasedBoilerplateFilteringBlock


class FakeSignal:
    """Minimal stand-in for core.signals.Signal"""
    def __init__(self, name, value):
        self.name = name
        self.value = value


def run_filter(text, signals, *, policy=None):
    """Apply filtering with pre-attached signals and optional policy."""
    doc = Document(text)
    doc.signals = signals

    block = SignalBasedBoilerplateFilteringBlock(policy=policy)
    block.apply(doc)

    return doc.text


# ──────────────────────────────
# Baseline behavior tests
# ──────────────────────────────

def test_drops_empty_document_by_default():
    text = "  \n\n  "
    out = run_filter(text, [])

    assert out == ""


def test_drops_boilerplate_paragraphs():
    text = "Menu Home About\n\nReal content here."
    signals = [
        FakeSignal("paragraph[0].is_boilerplate_candidate", True),
        FakeSignal("paragraph[0].repetition_count", 3),
    ]

    out = run_filter(text, signals)
    assert out.strip() == "Real content here."


def test_keeps_non_boilerplate_paragraph():
    text = "Important article paragraph."
    signals = [
        FakeSignal("paragraph[0].is_boilerplate_candidate", False),
    ]

    out = run_filter(text, signals)
    assert out.strip() == text


def test_preserves_list_block_by_default():
    text = "- item one\n- item two\n- item three\n\nMain article text"
    signals = [
        FakeSignal("paragraph[0].is_list_block", True),
    ]

    out = run_filter(text, signals)

    assert out.strip() == (
        "- item one\n- item two\n- item three\n\nMain article text"
    )


# ──────────────────────────────
# Policy honesty tests
# Each test must FAIL if policy
# wiring is removed
# ──────────────────────────────

def test_respects_min_repetition_policy():
    text = "Nav Menu\n\nMain content"
    signals = [
        FakeSignal("paragraph[0].is_boilerplate_candidate", True),
        FakeSignal("paragraph[0].repetition_count", 2),
    ]

    out = run_filter(
        text,
        signals,
        policy={"min_repetition": 3},
    )

    # repetition < min_repetition → should NOT drop
    assert out.strip() == text


def test_respects_max_boilerplate_length_policy():
    text = "Short boilerplate\n\nMain content"
    signals = [
        FakeSignal("paragraph[0].is_boilerplate_candidate", True),
        FakeSignal("paragraph[0].repetition_count", 5),
    ]

    out = run_filter(
        text,
        signals,
        policy={"max_boilerplate_length": 5},
    )

    # paragraph too long to be considered boilerplate under policy
    assert out.strip() == text


def test_respects_drop_empty_policy():
    text = "   \n\nMain content"

    out = run_filter(
        text,
        [],
        policy={"drop_empty": False},
    )

    # empty paragraph should be preserved
    assert out.startswith("   ")


def test_respects_preserve_headers_policy():
    text = "HEADER TITLE\n\nMain content"
    signals = [
        FakeSignal("paragraph[0].starts_with_header", True),
        FakeSignal("paragraph[0].is_boilerplate_candidate", True),
        FakeSignal("paragraph[0].repetition_count", 10),
    ]

    out = run_filter(
        text,
        signals,
        policy={"preserve_headers": True},
    )

    assert out.strip() == text
