import pytest
from datasets import Dataset

from text_curation import CorpusPipeline
from text_curation.registry import get_profile


def _make_dataset(texts):
    return Dataset.from_dict({
        "text": texts
    })


def test_corpus_pipeline_deterministic_hash():
    dataset = _make_dataset([
        "Hello world",
        "Another document",
        "Hello world",
    ])

    pipeline = CorpusPipeline(
        profile="web_pretrain_v1",
        dedup="hash",
        strict_manifest=True,
    )

    ds1, manifest1 = pipeline(dataset)
    ds2, manifest2 = pipeline(dataset)

    assert manifest1.dataset_hash == manifest2.dataset_hash
    assert len(ds1) == len(ds2)


def test_corpus_pipeline_order_invariant():
    dataset_a = _make_dataset([
        "A",
        "B",
        "A",
    ])

    dataset_b = _make_dataset([
        "A",
        "A",
        "B",
    ])

    pipeline = CorpusPipeline(
        profile="web_pretrain_v1",
        dedup="hash",
        strict_manifest=True,
    )

    _, manifest_a = pipeline(dataset_a)
    _, manifest_b = pipeline(dataset_b)

    assert manifest_a.dataset_hash == manifest_b.dataset_hash


def test_corpus_pipeline_dedup_changes_size():
    dataset = _make_dataset([
        "repeat",
        "repeat",
        "unique",
    ])

    pipeline_no_dedup = CorpusPipeline(
        profile="web_pretrain_v1",
        dedup=None,
    )

    pipeline_with_dedup = CorpusPipeline(
        profile="web_pretrain_v1",
        dedup="hash",
    )

    ds_no, _ = pipeline_no_dedup(dataset)
    ds_yes, _ = pipeline_with_dedup(dataset)

    assert len(ds_yes) < len(ds_no)


def test_corpus_pipeline_strict_enforced():
    dataset = _make_dataset(["single doc"])

    pipeline = CorpusPipeline(
        profile="web_pretrain_v1",
        dedup=None,
        strict_manifest=True,
    )

    # Should not raise because required fields are set
    ds, manifest = pipeline(dataset)

    assert manifest.strict is True
    assert manifest.dataset_hash is not None
