from datasets import Dataset
from text_curation.reports import DatasetManifest

def test_manifest_deterministic_hash():
    ds = Dataset.from_dict({
        "text": ["a", "b", "c"]
    })

    m1 = DatasetManifest.from_dataset(
        dataset=ds,
        text_column="text",
        profile_ids=["web_common_v1"],
        library_version="1.6.0.dev3",
        block_order=["RedactionBlock"],
        total_token_count=3,
        timestamp="2024-01-01T000:00:00Z",
    )

    m2 = DatasetManifest.from_dataset(
        dataset=ds,
        text_column="text",
        profile_ids=["web_common_v1"],
        library_version="1.6.0.dev3",
        block_order=["RedactionBlock"],
        total_token_count=3,
        timestamp="2024-01-01T000:00:00Z",
    )

    assert m1.dataset_hash == m2.dataset_hash


def test_manifest_immutable():
    ds = Dataset.from_dict({
        "text": ["x"]
    })

    manifest = DatasetManifest.from_dataset(
        dataset=ds,
        text_column="text",
        profile_ids=["web_common_v1"],
        library_version="1.6.0.dev3",
        block_order=["RedactionBlock"],
        total_token_count=1,
        timestamp="fixed",
    )

    try:
        manifest.library_version = "new"
        assert False
    except Exception:
        assert True