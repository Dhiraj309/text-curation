from text_curation.core.signals import Signal

class Document:
    """
    Container for text and associated processing artifacts.

    A Document holds the mutable text being processed along with
    emitted signals and annotations. It is the shared state passed
    through all blocks in a pipeline.

    Mutation rules:
    - Text may only be modified via set_text()
    - Signals are append-only
    """

    __slots__ = (
        "_text", 
        "annotations",
        "signals",
        "_dropped",
        "_drop_reason"
        )

    def __init__(self, text: str):
        """
        Initialize a new Document.

        Args:
            text: Raw input text to be curated
        """
        self._text = text
        self.annotations = {}
        self.signals: list[Signal] = []
        self._dropped = False
        self._drop_reason = None

    @property
    def text(self) -> str:
        return self._text

    def set_text(self, text: str):
        """
        Replace the document text.

        Blocks that mutate content must use this method to ensure
        changes are explicit and centralized.
        """
        self._text = text

    def add_signal(self, name: str, value):
        """
        Emit a signal describing an observed property of the text.

        Signals are append-only and are never mutated once emitted.
        """
        self.signals.append(Signal(name, value))

    def summarize_signals(self) -> dict:
        summary = {}

        for sig in self.signals:
            key = sig.name.split(".", 1)[-1]
            summary[key] = summary.get(key, 0) + 1

        return summary
    
    @property
    def is_dropped(self) -> bool:
        return self._dropped
    
    @property
    def drop_reason(self):
        return self._drop_reason
    
    def drop(self, reason: str):
        """
        Mark document as dropped.

        Dropping is idempotent.
        Reason must be explicit.
        """

        if not self._dropped:
            self._dropped = True
            self._drop_reason = str(reason)

            # Emit explicit signals for auditability
            self.add_signal("document.dropped", True)
            self.add_signal("document.drop_reason", str(reason))

def compute_basic_stats(text: str) -> dict:
    if not text:
        return {
            "chars": 0,
            "words": 0,
            "lines": 0,
            "paragraphs": 0
        }
    
    words = text.split()
    lines = text.split("\n")
    paragraphs = [p for p in text.split("\n\n") if p.strip()]

    return {
        "chars": len(text),
        "words": len(words),
        "lines": len(lines),
        "paragraphs": len(paragraphs)
    }