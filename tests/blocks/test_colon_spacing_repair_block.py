from text_curation.blocks.formatting.colon_spacing_repair import ColonSpacingRepairBlock
from text_curation.core.document import Document


def test_colon_spacing_repair():

    text = "Matthew 25:23More text follows."

    block = ColonSpacingRepairBlock()

    doc = Document(text)

    result = block.apply(doc)

    assert "25:23 More" in result.text
