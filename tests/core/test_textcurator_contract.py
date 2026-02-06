import pytest
import copy

from text_curation import TextCurator

def test_textcurator_is_immutable():
    curator = TextCurator.from_profile("web_common_v1")

    with pytest.raises(TypeError):
        curator.profile = None

    with pytest.raises(TypeError):
        curator.pipeline = None

    with pytest.raises(TypeError):
        curator.collect_reports = True

def test_textcurator_does_not_mutate_input_batch():
    curator = TextCurator.from_profile("web_common_v1")

    batch = {"text": ["Hello world"]}
    original = copy.deepcopy(batch)

    curator(batch)

    assert batch == original

def test_textcurator_output_schema_with_reports():
    curator = TextCurator.from_profile("web_common_v1")

    out = curator({"text": ["Hello"]})

    assert set(out.keys()) == {"text"}

def test_textcurator_output_schema_with_reports():
    curator = TextCurator.from_profile("web_common_v1", collect_reports=True)

    out = curator({"text": ["Heloo"]})

    assert set(out.keys()) == {"text", "curation_report"}
    assert len(out["text"]) == 1
    assert len(out["curation_report"]) == 1


def test_textcurator_is_deterministic():
    curator = TextCurator.from_profile("web_common_v1")

    out1 = curator({"text": ["Hello\n\nHello"]})
    out2 = curator({"text": ["Hello\n\nHello"]})

    assert out1 == out2