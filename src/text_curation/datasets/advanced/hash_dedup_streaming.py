from collections import defaultdict
from datasets import Dataset


def deduplicate_by_document_id(
    dataset: Dataset,
    *,
    collect_reports: bool = True,
):
    """
    Deterministic streaming deduplication using document_id.

    Assumes:
        - dataset contains a 'document_id' column
        - document_id is canonical (e.g. SHA-256)

    Behavior:
        - Groups rows by identical document_id
        - Keeps lexicographically smallest document_id
          (deterministic representative rule)
        - Order of input dataset does not affect final kept set
    """

    if "document_id" not in dataset.column_names:
        raise ValueError(
            "deduplicate_by_document_id requires 'document_id' column"
        )

    document_ids = dataset["document_id"]

    if not all(isinstance(d, str) for d in document_ids):
        raise TypeError("document_id column must contain strings")

    total_samples = len(document_ids)

    grouped = defaultdict(list)

    # Group indices by document_id
    for idx, doc_id in enumerate(document_ids):
        grouped[doc_id].append(idx)

    # Canonical representative selection
    keep_indices = []
    duplicate_groups = 0
    max_group_size = 1

    for doc_id in sorted(grouped.keys()):
        indices = grouped[doc_id]

        if len(indices) > 1:
            duplicate_groups += 1
            max_group_size = max(max_group_size, len(indices))

        # Representative = lowest index for this document_id
        # (indices already reflect dataset order)
        keep_indices.append(min(indices))

    keep_indices.sort()

    deduped = dataset.select(keep_indices)

    if not collect_reports:
        return deduped

    removed_samples = total_samples - len(keep_indices)

    report = {
        "operation": "deduplicate_by_document_id",
        "scope": "dataset",
        "input": {
            "samples": total_samples,
        },
        "output": {
            "samples": len(keep_indices),
        },
        "removed": {
            "samples": removed_samples,
            "fraction": removed_samples / total_samples
            if total_samples else 0.0,
        },
        "duplicates": {
            "groups": duplicate_groups,
            "max_group_size": max_group_size,
        },
        "determinism": {
            "identity_based": True,
            "order_invariant": True,
            "no_randomness": True,
        },
    }

    return deduped, report
