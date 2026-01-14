class Pipeline:
    """
    Executes an ordered sequence of blocks over input text.

    The pipeline is deterministic: blocks are applied in order
    and operate on a shared Document instance.
    """

    def __init__(self, blocks):
        """
        Create a pipeline from an ordered list of blocks.

        Args:
            blocks: Iterable of Block instances
        """
        self.blocks = blocks

    def run(self, text: str) -> str:
        """
        Run the pipeline on input text and return the final output.

        This method is a thin orchestration layer and intentionally
        hides Document internals from callers.
        """
        from .document import Document

        document = Document(text)

        for block in self.blocks:
            block.apply(document)

        return document.text