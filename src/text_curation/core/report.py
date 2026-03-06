class CurationReport:
    """
    Immutable, fully-specified report describing how a single
    document was transformed by a curation pipeline.

    The schema is total: all fields are always present.
    """

    __slots__ = (
        "profile_id",
        "blocks",
        "input_stats",
        "output_stats",
        "blocks_stats",
        "signals_summary",
        "extras",
        "dropped",
        "drop_reason",
        "document_id",
    )

    def __init__(
        self,
        *,
        profile_id: str,
        blocks: list[str],
        input_stats: dict,
        output_stats: dict,
        block_stats: dict | None = None,
        signals_summary: dict | None = None,
        extras: dict | None = None,
        dropped: bool = False,
        drop_reason: str | None = None,
        document_id: str | None = None,
    ):

        self.profile_id = profile_id
        self.blocks = list(blocks)
        self.input_stats = dict(input_stats)
        self.output_stats = dict(output_stats)
        self.dropped = bool(dropped)
        self.drop_reason = drop_reason
        self.document_id = document_id

        # Always present — never None
        self.blocks_stats = dict(block_stats or {})
        self.signals_summary = dict(signals_summary or {})
        self.extras = dict(extras or {})

    def to_dict(self) -> dict:
        """
        Return a deterministic, serialization-safe representation.
        """

        return {
            "profile_id": self.profile_id,
            "blocks": list(self.blocks),
            "input_stats": dict(self.input_stats),
            "output_stats": dict(self.output_stats),

            # deterministic ordering
            "block_stats": {
                k: dict(v) for k, v in sorted(self.blocks_stats.items())
            },

            # deterministic ordering
            "signals_summary": dict(sorted(self.signals_summary.items())),

            "extras": dict(self.extras),
            "dropped": self.dropped,
            "drop_reason": self.drop_reason,
            "document_id": self.document_id,
        }
