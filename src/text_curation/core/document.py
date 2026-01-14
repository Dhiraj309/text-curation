from text_curation.core.signals import Signal


class Document:
    """
    Container for text and associated processing artifacts.

    A Document holds the mutable text being processed along with
    emitted signals and annotations. It is the shared state passed
    through all blocks in a pipeline.
    """

    def __init__(self, text: str):
        """
        Initialize a new Document.

        Args:
            text: Raw input text to be curated
        """
        self.text = text
        self.annotations = {}
        self.signals: list[Signal] = []

    def set_text(self, text: str):
        """
        Replace the document text.

        Blocks that mutate content must use this method to ensure
        changes are explicit and centralized.
        """
        self.text = text

    def add_signal(self, name: str, value):
        """
        Emit a signal describing an observed property of the text.

        Signals are append-only and are never mutated once emitted.
        """
        self.signals.append(Signal(name, value))