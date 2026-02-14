from datasets import Dataset
from text_curation.datasets.advanced.hash_dedup import deduplicate_by_hash

def test_hash_dedup_basic():
    ds = Dataset.from_dict({
        "text": ["a", "b", "a", "c"]
    })

    dedup, report = deduplicate_by_hash(
        ds,
        column="text"
    )

    assert len(dedup) == 3
    assert report["deduplicates"]["groups"] == 1

def test_hash_dedup_keep_last():
    ds = Dataset.from_dict({
        "text": ["a", "b", "a"]
    })

    dedup, _ = deduplicate_by_hash(
        ds,
        column="text",
        keep="last"
    )

    assert dedup["text"] == ["b", "a"]

def test_hash_dedup_deterministic():
    ds = Dataset.from_dict({
        "text": ["x", "y", "x"]
    })

    d1, r1 = deduplicate_by_hash(ds, column="text")
    d2, r2 = deduplicate_by_hash(ds, column="text")

    assert d1["text"] == d2["text"]
    assert r1 == r2