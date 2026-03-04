from datasets import Dataset

from text_curation.datasets.advanced.dedup_clusters import (
    analyze_duplicate_clusters
)


def test_duplicate_cluster_detection():

    ds = Dataset.from_dict(
        {
            "text": [
                "a",
                "a",
                "b",
                "c",
                "c",
                "c",
            ]
        }
    )

    result = analyze_duplicate_clusters(ds)

    assert result["duplicate_clusters"] == 2


def test_duplicate_density():

    ds = Dataset.from_dict(
        {
            "text": ["a", "a", "b"]
        }
    )

    result = analyze_duplicate_clusters(ds)

    assert result["duplicate_density"] > 0


def test_cluster_distribution():

    ds = Dataset.from_dict(
        {
            "text": ["x", "x", "x"]
        }
    )

    result = analyze_duplicate_clusters(ds)

    assert result["cluster_size_distribution"][3] == 1
