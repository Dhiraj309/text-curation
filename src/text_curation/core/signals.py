class Signal:
    """
    Immutable, inspectable signal emitted during document processing.

    Signals represent observed facs about text structure or content.
    Once created, they must never change.
    """

    __slots__ = ("name", "value")

    def __init__(self, name: str, value):
        """
        Create a new signal.

        Args:
            name: Fully-qualified signal name (e.g. "paragraph[3].is_header")
            value: Observed value associated with the signal
        """
        self.name = name
        self.value = value

    def __setattr__(self, key, value):
        if hasattr(self, key):
            raise TypeError(f"Signal attribute '{key}' is immutable")
        
        super().__setattr__(key, value)

    def __repr__(self) -> str:
        return f"Signa(name={self.name!r}, value={self.value!r})"