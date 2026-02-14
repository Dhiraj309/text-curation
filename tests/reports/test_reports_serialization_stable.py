import json
from text_curation import TextCurator

def test_report_serialization_is_stable():
    curator = TextCurator.from_profile("web_common_v1", collect_reports=True)

    sample = {"text": ["Example text."]}
    out = curator(sample)

    serialized = json.dumps(out["curation_report"], sort_keys = True)

    serialized_again = json.dumps(out["curation_report"], sort_keys = True)

    assert serialized == serialized_again