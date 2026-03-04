from datasets import Dataset

from text_curation.tools.artifact_scanner import artifact_scan


def test_detect_space_before_punctuation():

    ds = Dataset.from_dict(
        {"text": ["Hello , world"]}
    )

    result = artifact_scan(ds)

    assert result["artifact_counts"]["space_before_punctuation"] > 0


def test_detect_number_format():

    ds = Dataset.from_dict(
        {"text": ["10 , 000"]}
    )

    result = artifact_scan(ds)

    assert result["artifact_counts"]["broken_number_format"] > 0


def test_no_artifacts():

    ds = Dataset.from_dict(
        {"text": ["Hello world."]}
    )

    result = artifact_scan(ds)

    assert result["artifact_counts"] == {}
