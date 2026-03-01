def assign_shard(document_id: str, num_shards: int) -> int:
    """
    Deterministically assign a document to a shard.

    Shard assignment is derived from the first 8 hex characters
    of the document_id (assumed SHA-256 hex digest).

    This ensures:
    - Stable assignment across machines
    - Shard invariance
    - No randomness
    """

    if not isinstance(document_id, str) or not document_id:
        raise TypeError("document_id must be a non-empty string")

    if not isinstance(num_shards, int) or num_shards <= 0:
        raise ValueError("num_shards must be a positive integer")

    # First 8 hex chars → 32-bit deterministic integer
    prefix = document_id[:8]
    value = int(prefix, 16)

    return value % num_shards
