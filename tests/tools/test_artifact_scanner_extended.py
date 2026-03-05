from text_curation.tools.artifact_scanner import scan_artifacts


def test_detects_colon_spacing():
    texts = ["Matthew 25: 23"]
    report = scan_artifacts(texts)

    assert report["colon_spacing_changes"] == 1


def test_detects_quote_merge():
    texts = ['Sentence."Quote']
    report = scan_artifacts(texts)

    assert report["merged_quotes"] == 1
