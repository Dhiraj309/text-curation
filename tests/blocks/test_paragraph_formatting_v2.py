from text_curation.blocks.formatting.paragraph_v2 import ParagraphFormattingBlockV2
from text_curation.core.document import Document


def run(text):
    block = ParagraphFormattingBlockV2()
    doc = Document(text)
    return block.apply(doc).text


def test_preserves_paragraph_boundary():
    text = "Sentence.\n\n\"Quote\""
    out = run(text)

    assert out.split("\n\n")[1].startswith('"')


def test_preserves_colon_spacing():
    text = "Matthew 25:23More..."
    out = run(text)

    assert "25:23" in out


def test_preserves_em_dash():
    text = "— Defense Secretary"
    out = run(text)

    assert "—" in out


def test_ellipsis_repair():
    text = "Wait..... what?"
    out = run(text)

    assert "…" in out
