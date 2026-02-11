def test_all_blocks_return_document():
    from text_curation.blocks import (
        NormalizationBlock,
        RedactionBlock,
    )
    from text_curation.core.document import Document

    doc = Document("test")

    for block in [
        NormalizationBlock(),
        RedactionBlock(),
    ]:
        out = block.apply(doc)
        assert out is doc
