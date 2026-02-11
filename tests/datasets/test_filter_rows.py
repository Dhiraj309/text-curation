from text_curation.datasets import filter_rows
from datasets import Dataset

def test_filter_rows_min_len():
    dataset = Dataset.from_dict({
        "id": [1, 2, 3, 4, 5, 6],
        "text": [
            "",  # empty
            "Hello world",  # 2 words
            "This is a short sentence with exactly seven words.",  # 7 words
            (
                "This text has exactly twenty words which makes it useful "
                "for testing the filtering logic in our pipeline system today."
            ),  # >= 20 words
            (
                "This is a longer piece of text that clearly exceeds the "
                "twenty word threshold and should always be retained by the filter."
            ),  # > 20 words
            (
                "Another long valid example sentence that comfortably clears the "
                "minimum word requirement for dataset level filtering and validation for filter rows test cases."
            ),  # >= 20 words
        ],
    })

    filtered, report = filter_rows(
            dataset,
            predicate=lambda r: len(r["text"].split()) >= 20,
            description="drop samples with fewer than 20 words",
            collect_reports=True
        )

    # Dataset behavior
    assert len(dataset) == 6
    assert len(filtered) == 3

    # Order preserved
    assert filtered["id"] == [4, 5, 6]

    # Report correctness
    assert report["operation"] == "filter_rows"
    assert report["scope"] == "dataset"
    assert report["input"]["samples"] == 6
    assert report["output"]["samples"] == 3
    assert report["removed"]["samples"] == 3
    assert report["removed"]["fraction"] == 0.5

def test_filter_rows_is_deterministic():
    from datasets import Dataset
    from text_curation.datasets.filtering import filter_rows

    ds = Dataset.from_dict({"x": list(range(10))})

    def pred(row):
        return row["x"] % 2 == 0

    out1, _ = filter_rows(ds, predicate=pred, description="even")
    out2, _ = filter_rows(ds, predicate=pred, description="even")

    assert out1["x"] == out2["x"]
