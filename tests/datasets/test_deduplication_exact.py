import pytest
from datasets import Dataset
from text_curation.datasets import deduplicate_exact


def test_deduplicate_exact_basic():
    dataset = Dataset.from_dict({
        "text": [
            "hello world",
            "hello world",
            "unique text",
            "hello world",
        ]
    })

    deduped, report = deduplicate_exact(
        dataset,
        column="text",
        keep="first",
        collect_reports=True,
    )

    assert len(deduped) == 2
    assert deduped["text"] == ["hello world", "unique text"]

    assert report["operation"] == "deduplicate_exact"
    assert report["input"]["samples"] == 4
    assert report["output"]["samples"] == 2
    assert report["removed"]["samples"] == 2
    assert report["duplicates"]["groups"] == 1
    assert report["duplicates"]["max_group_size"] == 3

def test_deduplication_requires_string_column():
    ds = Dataset.from_dict({"text": [{"a": 1}, {"a": 1}]})

    with pytest.raises(TypeError):
        deduplicate_exact(ds, column="text")
