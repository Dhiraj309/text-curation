class Block:
    """
    Base class for all text curation blocks.

    A Block is a deterministic transformation or analysis step
    that operates on a Document. Blocks may mutate text, emit
    signals, or both.

    Blocks must be stateless and configurable only via policy
    to ensure reproducibility and safe reuse.
    """

    def __init__(self, policy=None):
        """
        Initialize the block with an optional policy dict.

        Policy contains explicit configuration knobs.
        Defaults are defined by concrete block implementations.
        """
        # Copy policy to prevent external mutation
        self.policy = dict(policy or {})
        self._stats: dict[str, int] = {}

    def apply(self, document):
        """
        Apply the block to a Document.

        Subclasses must implement this method.
        """
        raise NotImplementedError

    def reset_stats(self):
        """
        Reset block-local statistics.
        Called by Pipeline at the start of each run.
        """
        self._stats.clear()

    def inc(self, key: str, value: int = 1):
        """
        Increment a statistic deterministically.

        This helper avoids inconsistent stat update patterns
        across blocks.
        """
        self._stats[key] = self._stats.get(key, 0) + value

    def get_stats(self) -> dict:
        """
        Return deterministic, JSON-safe block statistics.

        Keys are sorted to ensure stable ordering across
        multiprocessing workers.
        """
        return {k: int(v) for k, v in sorted(self._stats.items())}
