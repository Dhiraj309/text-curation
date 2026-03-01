from typing import Callable, Optional, Union

from datasets import Dataset

from text_curation.curator import TextCurator
from text_curation.registry import get_profile
from text_curation.core.reproducibility import compute_pipeline_hash
from text_curation.core.dataset_hash import compute_dataset_hash
from text_curation.reports.manifest import DatasetManifest
from text_curation.datasets import filter_rows
from text_curation.datasets.advanced.hash_dedup_streaming import (
    deduplicate_by_document_id,
)
from text_curation.datasets.advanced.minhash import minhash_deduplicate


class CorpusPipeline:
    """
    Deterministic corpus-level orchestration layer.

    This class composes:
    - Text curation
    - Optional filtering
    - Optional deduplication
    - Canonical dataset identity
    - Manifest generation

    No multiprocessing is performed internally.
    """

    def __init__(
        self,
        *,
        profile: Union[str, object],
        dedup: Optional[str] = None,  # "hash" | "minhash" | None
        filter_fn: Optional[Callable] = None,
        shard_config: Optional[dict] = None,
        strict_manifest: bool = False,
    ):
        if isinstance(profile, str):
            profile_obj = get_profile(profile)
        else:
            profile_obj = profile

        self.profile = profile_obj
        self.dedup = dedup
        self.filter_fn = filter_fn
        self.shard_config = shard_config or {}
        self.strict_manifest = strict_manifest

        self._curator = TextCurator(
            profile_obj,
            collect_reports=False,
        )

    def __call__(self, dataset: Dataset):

        # -------------------------------------------------
        # 1. Apply TextCurator
        # -------------------------------------------------
        dataset = dataset.map(
            self._curator,
            batched=True,
        )

        # -------------------------------------------------
        # 2. Optional Filtering
        # -------------------------------------------------
        if self.filter_fn is not None:
            dataset, _ = filter_rows(
                dataset,
                predicate=self.filter_fn,
                description="CorpusPipeline filter_fn",
                collect_reports=True,
            )

        # -------------------------------------------------
        # 3. Optional Deduplication
        # -------------------------------------------------
        if self.dedup == "hash":
            dataset, _ = deduplicate_by_document_id(dataset)

        elif self.dedup == "minhash":
            if "minhash_config" not in self.shard_config:
                raise ValueError(
                    "minhash dedup requires shard_config['minhash_config']"
                )

            config = self.shard_config["minhash_config"]

            dataset, _ = minhash_deduplicate(
                dataset,
                column="text",
                ngram_size=config["ngram_size"],
                num_hashes=config["num_hashes"],
                threshold=config["threshold"],
                seed=config["seed"],
            )

        elif self.dedup is not None:
            raise ValueError("dedup must be 'hash', 'minhash', or None")

        # -------------------------------------------------
        # 4. Compute Canonical Dataset Hash
        # -------------------------------------------------
        if "document_id" not in dataset.column_names:
            raise ValueError(
                "CorpusPipeline requires 'document_id' column "
                "to compute canonical dataset identity"
            )

        document_ids = dataset["document_id"]
        pipeline_hash = compute_pipeline_hash(self.profile)
        dataset_hash = compute_dataset_hash(document_ids, pipeline_hash)

        # -------------------------------------------------
        # 5. Manifest Generation
        # -------------------------------------------------
        manifest = DatasetManifest(
            profile_ids=[self.profile.id],
            library_version="runtime",
            block_order=[b.__class__.__name__ for b in self.profile.blocks],
            dataset_hash=dataset_hash,
            document_count=len(dataset),
            total_token_count=0,
            timestamp="runtime",
            metadata={},
            strict=self.strict_manifest,
        )

        return dataset, manifest
