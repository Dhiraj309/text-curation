from text_curation.blocks.base import Block

class AnalysisBlock(Block):
    """
    Base class for deterministic, signal-only analysis blocks.

    AnalysisBlocks are allowed to emit signals but must NOT:
    - mutate document text
    - call document.set_text()
    - mutate document.annotations()

    They exist purely to compute ispectable metadata.
    """

    def apply(self, document):
        """
        Subclasses must implement this method.

        They must not mutate document.text.
        """

    def _forbid_text_mutation(self, document):
        """
        Defensive helper to assert text immutability.
        """
        raise RuntimeError(
            "AnalysisBlock attempted to mutate document text."
            "Analysis blocks must be signal-only."
        )