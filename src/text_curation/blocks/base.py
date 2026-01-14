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
        self.policy = policy or {}

    def apply(self, document):
        """
        Apply the block to a Document.

        Subclasses must implement this method.
        """
        raise NotImplementedError