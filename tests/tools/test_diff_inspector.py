from text_curation.tools.diff_inspector import inspect_diffs


def test_detects_changes():

    raw = ["Hello..... world"]
    cleaned = ["Hello… world"]

    report = inspect_diffs(raw, cleaned)

    assert len(report) == 1
    assert "Hello..... world" in report[0]["raw"]
    assert "Hello… world" in report[0]["cleaned"]
    assert "-Hello..... world" in report[0]["diff"]
