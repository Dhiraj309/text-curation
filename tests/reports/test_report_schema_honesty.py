from text_curation.core.report import CurationReport

def test_report_omits_empty_optional_fields():
    report = CurationReport(
        profile_id="test_v1",
        blocks=["BlockA"],
        input_stats={"chars": 10},
        output_stats={"chars": 10},
        block_stats={},
        signals_summary={},
    )

    data = report.to_dict()

    assert "block_stats" not in data
    assert "signals_summary" not in data

def test_report_preserves_present_optional_fields():
    report = CurationReport(
        profile_id="test_v1",
        blocks=["BlockA"],
        input_stats={"chars": 10},
        output_stats={"chars": 5},
        block_stats={"BlockA": {"removed": 5}},
        signals_summary={"is_header": 2}
    )

    data = report.to_dict()

    assert "block_stats" in data
    assert "signals_summary" in data