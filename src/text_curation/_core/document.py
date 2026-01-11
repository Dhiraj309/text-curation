from text_curation._core.signals import Signal

class Document:
    """
    Container for text and associated processing artifacts.

    A Document holds the mutable text being processed along with
    emitted signals and annotations. Blocks may mutate text,
    emit signals, or both.
    """
        
    def __init__(self, text: str):
        self.text = text
        self.annotations = {}
        self.signals: list[Signal] = []

    def set_text(self, text: str):
        self.text = text

    def add_signal(self, name: str, value):
        self.signals.append(Signal(name, value))