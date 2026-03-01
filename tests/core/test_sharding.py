import pytest

from text_curation.core.sharding import assign_shard


def test_assign_shard_deterministic():
    doc_id = "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"

    shard1 = assign_shard(doc_id, 16)
    shard2 = assign_shard(doc_id, 16)

    assert shard1 == shard2


def test_assign_shard_range():
    doc_id = "ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff"

    shard = assign_shard(doc_id, 8)

    assert 0 <= shard < 8


def test_assign_shard_different_shard_counts():
    doc_id = "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"

    shard_8 = assign_shard(doc_id, 8)
    shard_16 = assign_shard(doc_id, 16)

    # Same prefix, different modulo → possibly different shard
    assert shard_8 == shard_16 % 8


def test_assign_shard_invalid_document_id():
    with pytest.raises(TypeError):
        assign_shard("", 8)

    with pytest.raises(TypeError):
        assign_shard(None, 8)


def test_assign_shard_invalid_num_shards():
    doc_id = "abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890"

    with pytest.raises(ValueError):
        assign_shard(doc_id, 0)

    with pytest.raises(ValueError):
        assign_shard(doc_id, -1)

    with pytest.raises(ValueError):
        assign_shard(doc_id, "not-int")
