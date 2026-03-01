import hashlib
from typing import List, Set, Tuple
from datasets import Dataset


def _stable_hash(value: str) -> int:
    return int(hashlib.sha1(value.encode("utf-8")).hexdigest(), 16)


def _extract_ngrams(text: str, n: int) -> Set[str]:
    tokens = text.split()
    if len(tokens) < n:
        return set()

    return {
        " ".join(tokens[i:i + n])
        for i in range(len(tokens) - n + 1)
    }


def _minhash_signature(ngrams: Set[str], num_hashes: int, seed: int) -> List[int]:
    signature = []

    for i in range(num_hashes):
        min_val = None
        salt = f"{seed}_{i}"

        for ng in ngrams:
            combined = salt + ng
            hv = _stable_hash(combined)
            if min_val is None or hv < min_val:
                min_val = hv

        signature.append(min_val if min_val is not None else 0)

    return signature


def _jaccard_from_signature(sig1: List[int], sig2: List[int]) -> float:
    matches = sum(1 for a, b in zip(sig1, sig2) if a == b)
    return matches / len(sig1)


def minhash_deduplicate(
    dataset: Dataset,
    *,
    column: str,
    ngram_size: int,
    num_hashes: int,
    threshold: float,
    seed: int,
    collect_reports: bool = True,
) -> Tuple[Dataset, dict]:

    if column not in dataset.column_names:
        raise ValueError(f"Column '{column}' not found in dataset")

    if "document_id" not in dataset.column_names:
        raise ValueError(
            "minhash_deduplicate requires 'document_id' column "
            "for canonical representative selection"
        )

    if not (0.0 <= threshold <= 1.0):
        raise ValueError("threshold must be between 0 and 1")

    texts = dataset[column]
    document_ids = dataset["document_id"]

    total_samples = len(texts)

    signatures = []

    # Deterministic signature computation
    for value in texts:
        if not isinstance(value, str):
            raise TypeError("All values must be strings")

        ngrams = _extract_ngrams(value, ngram_size)
        sig = _minhash_signature(ngrams, num_hashes, seed)
        signatures.append(sig)

    keep = [True] * total_samples
    clusters = []

    # Deterministic pairwise clustering
    for i in range(total_samples):
        if not keep[i]:
            continue

        cluster = [i]

        for j in range(i + 1, total_samples):
            if not keep[j]:
                continue

            sim = _jaccard_from_signature(signatures[i], signatures[j])
            if sim >= threshold:
                cluster.append(j)

        if len(cluster) > 1:
            # Canonical representative: lowest document_id
            cluster_sorted = sorted(
                cluster,
                key=lambda idx: document_ids[idx]
            )

            clusters.append(cluster_sorted)

            for idx in cluster_sorted[1:]:
                keep[idx] = False

    keep_indices = [i for i, k in enumerate(keep) if k]

    deduped = dataset.select(keep_indices)

    if not collect_reports:
        return deduped

    report = {
        "operation": "minhash_deduplication",
        "scope": "dataset",
        "column": column,
        "ngram_size": ngram_size,
        "num_hashes": num_hashes,
        "threshold": threshold,
        "seed": seed,
        "input": {
            "samples": total_samples,
        },
        "output": {
            "samples": len(keep_indices),
        },
        "clusters": {
            "count": len(clusters),
        },
        "determinism": {
            "seed_controlled": True,
            "order_preserving": True,
            "canonical_representative": "lowest_document_id",
        },
    }

    return deduped, report
