class Signal:
    """
    Represents an inspectable observation emitted during text processing.

    Signals capture structural or statistical properties of text
    without directly modifying content. They are consumed explicitly
    by downstream blocks.
    """
        
    def __init__(self, name: str, value):
        self.name = name
        self.value = value