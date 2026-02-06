from dataclasses import dataclass, field, asdict
from typing import Dict, Any, List

class CurationReport:
    """
    Immutable, fully-specified report describing how a single
    document was transformed by a curation pipeline.

    The schema is total: all fields are always present
    """
    __slots__ = (
        "profile_id",
        "blocks",
        "input_stats",
        "output_stats",
        "blocks_stats",
        "signals_summary",
        "extras"
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
            ):
        
        self.profile_id = profile_id
        self.blocks = list(blocks)
        self.input_stats = dict(input_stats)
        self.output_stats = dict(output_stats)

        # Always present never None
        self.blocks_stats = dict(block_stats or {})
        self.signals_summary = dict(signals_summary or {})
        self.extras = dict(extras or {})
    
    def to_dict(self) -> dict:
        """
        Return a serialization-safe representation
        """
        return {
            "profile_id": self.profile_id,
            "blocks": list(self.blocks),
            "input_stats": dict(self.input_stats),
            "output_stats": dict(self.output_stats),
            "block_stats": dict(self.blocks_stats),
            "signals_summary": dict(self.signals_summary),
            "extras": dict(self.extras),
        }