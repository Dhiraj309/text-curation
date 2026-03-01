
import hashlib


def compute_dataset_hash(document_ids: list[str], pipeline_hash: str) -> str:
    """
    Compute a canonical, order-invariant dataset hash.

    Dataset identity is derived from:
    - Sorted document_ids
    - Deterministic pipeline_hash

    This ensures:
    - Shard invariance
    - Order independence
    - Reproducibility across environments
    """

    if not isinstance(document_ids, list):
        raise TypeError("document_ids must be a list of strings")

    if not all(isinstance(d, str) for d in document_ids):
        raise TypeError("document_ids must contain only strings")

    if not isinstance(pipeline_hash, str) or not pipeline_hash:
        raise TypeError("pipeline_hash must be a non-empty string")

    sorted_ids = sorted(document_ids)

    hasher = hashlib.sha256()

    for doc_id in sorted_ids:
        hasher.update(doc_id.encode("utf-8"))

    hasher.update(pipeline_hash.encode("utf-8"))

    return hasher.hexdigest()
