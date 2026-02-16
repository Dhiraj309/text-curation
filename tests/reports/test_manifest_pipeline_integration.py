from datasets import Dataset
from text_curation.reports.manifest import DatasetManifest

def test_manifest_creation_with_profile():
    ds = Dataset.from_dict({
        "text": ["hello world"]
    })

    manifest = DatasetManifest.from_dataset(
        dataset=ds,
        text_column="text",
        profile_ids=["web_pretrain_v1"],
        library_version="1.6.0",
        block_order=["RedactionBlock"],
        total_token_count=2,
        timestamp="fixed",
    )

    assert manifest.dataset_hash is not None