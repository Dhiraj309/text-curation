from text_curation.core.report import CurationReport

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

def test_curation_report_schema_is_total():
    report = CurationReport(
        profile_id="test_v1",
        blocks=[],
        input_stats={},
        output_stats={},
    )

    d = report.to_dict()

    assert "block_stats" in d
    assert "signals_summary" in d
    assert "extras" in d

    assert d["block_stats"] == {}
    assert d["signals_summary"] == {}
    assert d["extras"] == {}