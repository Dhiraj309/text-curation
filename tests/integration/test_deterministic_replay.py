import copy
from text_curation import TextCurator

def test_deterministic_replay_no_reports():
    curator = TextCurator.from_profile("web_common_v1", collect_reports=False)

    sample = {
        "text": ["Hello world.\n\nHello world"]
    }

    out1 = curator(copy.deepcopy(sample))
    out2 = curator(copy.deepcopy(sample))

    assert out1 == out2

def test_deterministic_replay_with_reports():
    curator = TextCurator.from_profile("web_common_v1", collect_reports=True)

    sample = {"text": ["Hello world.\n\nHello world."]}

    out1 = curator(copy.deepcopy(sample))
    out2 = curator(copy.deepcopy(sample))

    assert out1 == out2

def test_full_pipeline_replay_is_identical():
    curator = TextCurator.from_profile("web_pretrain_v1", collect_reports=True)

    batch = {
        "text": [
            "This is a test.",
            "Another example text."
        ]
    }

    run1 = curator(batch)
    run2 = curator(batch)

    assert run1 == run2