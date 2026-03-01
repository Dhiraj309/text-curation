import hashlib
from dataclasses import dataclass, asdict
from typing import List, Dict, Any

def _stable_dataset_hash(values: List[str])-> str:
    """
    Deterministic dataset hash computed from ordered text values.
    """
    hasher = hashlib.sha256()
    for value in values:
        hasher.update(value.encode("utf-8"))
    return hasher.hexdigest()

@dataclass(frozen=True)
class DatasetManifest:
    """
    Immutable dataset lineage manifest.

    All fields must be explicitely provided.
    """

    profile_ids: List[str]
    library_version: str
    block_order: List[str]
    total_token_count: int
    timestamp: str
    metadata: Dict[str, Any]

    dataset_hash: str | None = None
    document_count: int | None = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)
    
    @classmethod
    def from_dataset(
        cls,
        *,
        dataset,
        text_column: str,
        profile_ids: List[str],
        library_version: str,
        block_order: List[str],
        total_token_count: int,
        timestamp: str,
        metadata: Dict[str, Any] | None = None,
    ):
        if text_column not in dataset.column_names:
            raise ValueError(f"Column '{text_column}' not found in dataset")
        
        texts = dataset[text_column]

        if not all(isinstance(t, str) for t in texts):
            raise TypeError("Dataset must contain string text values")
        
        dataset_hash = _stable_dataset_hash(texts)

        return cls(
            profile_ids=list(profile_ids),
            library_version=library_version,
            block_order=list(block_order),
            dataset_hash=dataset_hash,
            document_count=len(texts),
            total_token_count=int(total_token_count),
            timestamp=str(timestamp),
            metadata=dict(metadata or {}),
        )
