"""
Tests for formatting normalization and structure preservation.

FormattingBlock must:
- Normalize whitespace
- Reconstruct paragraphs
- Preserve code indentation
- Fix punctuation spacing safely
"""

from text_curation.core.document import Document
from text_curation.blocks.formatting import CodeSafeFormmatingBlock, ParagraphFormattingBlock

def format_text(text):
    doc = Document(text)

    CodeSafeFormmatingBlock().apply(doc)
    ParagraphFormattingBlock().apply(doc)
    return doc.text

def test_trailing_whitespace():
    assert format_text("hello   \nworld  ") == "hello\nworld"

def test_blank_line_collapse():
    assert format_text("a\n\n\n\nb") == "a\n\nb"

def test_paragraph_reconstruction():
    text = "This is line one\nthis is line two\n\nNew paragraph"
    out = format_text(text)
    assert out == "This is line one this is line two\n\nNew paragraph"

def test_code_preservation():
    text = "Python Code\n    for i in range(n)\n    print(i)"
    out = format_text(text)

    assert out == "Python Code\n    for i in range(n)\n    print(i)"

def test_punctuation_spacing():
    assert format_text("hello ,world!") == "hello, world!"