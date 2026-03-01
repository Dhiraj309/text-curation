import pytest
from text_curation.reports.manifest import DatasetManifest


def test_manifest_non_strict_allows_missing_fields():
    manifest = DatasetManifest(
        profile_ids=[],
        library_version="runtime",
        block_order=[],
        dataset_hash=None,
        document_count=None,
        total_token_count=0,
        timestamp="runtime",
        metadata={},
        strict=False,
    )

    assert manifest.strict is False


def test_manifest_strict_requires_dataset_hash():
    with pytest.raises(ValueError):
        DatasetManifest(
            profile_ids=["profile_v1"],
            library_version="runtime",
            block_order=["BlockA"],
            dataset_hash=None,  # Missing
            document_count=10,
            total_token_count=0,
            timestamp="runtime",
            metadata={},
            strict=True,
        )


def test_manifest_strict_requires_profile_ids():
    with pytest.raises(ValueError):
        DatasetManifest(
            profile_ids=[],  # Missing
            library_version="runtime",
            block_order=["BlockA"],
            dataset_hash="abc",
            document_count=10,
            total_token_count=0,
            timestamp="runtime",
            metadata={},
            strict=True,
        )


def test_manifest_strict_requires_block_order():
    with pytest.raises(ValueError):
        DatasetManifest(
            profile_ids=["profile_v1"],
            library_version="runtime",
            block_order=[],  # Missing
            dataset_hash="abc",
            document_count=10,
            total_token_count=0,
            timestamp="runtime",
            metadata={},
            strict=True,
        )


def test_manifest_strict_valid_case():
    manifest = DatasetManifest(
        profile_ids=["profile_v1"],
        library_version="runtime",
        block_order=["BlockA"],
        dataset_hash="abc",
        document_count=10,
        total_token_count=0,
        timestamp="runtime",
        metadata={},
        strict=True,
    )

    assert manifest.strict is True
    assert manifest.dataset_hash == "abc"
