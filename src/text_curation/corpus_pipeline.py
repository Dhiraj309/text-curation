
from typing import Callable, Optional, Union
import json
import hashlib

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

    Composes:
    - Text curation
    - Optional filtering
    - Optional deduplication
    - Canonical dataset identity
    - Manifest generation

    Parallelism (num_proc) applies ONLY to document-level
    TextCurator transforms. Canonical identity resolution
    remains single-threaded and deterministic.
    """

    def __init__(
        self,
        *,
        profile: Union[str, object],
        dedup: Optional[str] = None,
        filter_fn: Optional[Callable] = None,
        shard_config: Optional[dict] = None,
        strict_manifest: bool = False,
        num_proc: int | None = None,
    ):
        if isinstance(profile, str):
            profile_obj = get_profile(profile)
        else:
            profile_obj = profile

        if num_proc is not None:
            if not isinstance(num_proc, int) or num_proc <= 0:
                raise ValueError("num_proc must be a positive integer or None")

        self.profile = profile_obj
        self.dedup = dedup
        self.filter_fn = filter_fn
        self.shard_config = shard_config or {}
        self.strict_manifest = strict_manifest
        self._num_proc = num_proc

        self._curator = TextCurator(
            profile_obj,
            collect_reports=True,
        )

    def __call__(self, dataset: Dataset):

        # -------------------------------------------------
        # 1. Run TextCurator if dataset not already curated
        # -------------------------------------------------
        if "curation_report" not in dataset.column_names:

            if self._num_proc is not None:
                dataset = dataset.map(
                    self._curator,
                    batched=True,
                    num_proc=self._num_proc,
                )
            else:
                dataset = dataset.map(
                    self._curator,
                    batched=True,
                )

        # -------------------------------------------------
        # 2. Resolve document identity
        # -------------------------------------------------

        if "document_id" in dataset.column_names:

            # Use existing IDs
            document_ids = [str(x) for x in dataset["document_id"]]

        else:

            reports = dataset["curation_report"]
            texts = dataset["text"]

            document_ids = []

            for r, text in zip(reports, texts):

                if isinstance(r, str):
                    r = json.loads(r)

                doc_id = None

                if isinstance(r, dict):
                    doc_id = r.get("document_id")

                if not doc_id:
                    # deterministic fallback
                    doc_id = hashlib.sha256(
                        text.encode("utf-8")
                    ).hexdigest()

                document_ids.append(str(doc_id))

            dataset = dataset.add_column("document_id", document_ids)

        # Remove report column if present
        if "curation_report" in dataset.column_names:
            dataset = dataset.remove_columns(["curation_report"])

        # -------------------------------------------------
        # 3. Optional filtering
        # -------------------------------------------------
        if self.filter_fn is not None:

            dataset, _ = filter_rows(
                dataset,
                predicate=self.filter_fn,
                description="CorpusPipeline filter_fn",
                collect_reports=True,
            )

        # -------------------------------------------------
        # 4. Optional deduplication
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
        # 5. Compute canonical dataset hash
        # -------------------------------------------------
        if "document_id" not in dataset.column_names:

            raise ValueError(
                "CorpusPipeline requires 'document_id' column "
                "to compute canonical dataset identity"
            )

        document_ids = list(dataset["document_id"])

        pipeline_hash = compute_pipeline_hash(self.profile)

        dataset_hash = compute_dataset_hash(
            document_ids,
            pipeline_hash,
        )

        # -------------------------------------------------
        # 6. Manifest generation
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
