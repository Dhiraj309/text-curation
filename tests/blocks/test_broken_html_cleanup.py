from text_curation.blocks.formatting.html_structure import HTMLStructureBlock
from text_curation.core.document import Document


def test_broken_html_removed():

    text = "<div><span>Broken html without closing"

    block = HTMLStructureBlock()

    doc = Document(text)

    result = block.apply(doc)

    assert "<div>" not in result.text
    assert "Broken html without closing" in result.text
