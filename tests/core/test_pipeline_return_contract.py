def test_run_document_always_returns_tuple():
    from text_curation.core.pipeline import Pipeline
    from text_curation.blocks import NormalizationBlock

    pipeline = Pipeline([NormalizationBlock()])
    doc, report = pipeline.run_document("hello")

    assert doc.text == "hello"
    assert report is None
