class Region:
    """
    Represents a span or region of text with associated metadata.

    Regions are intended to support future annotation and span-based
    processing (e.g. highlights, detected entities, or structural spans).
    """
    
    def __init__(self, kind: str, start: str, end: str, data: None):
        self.kind = kind
        self.start = start
        self.end = end
        self.data = data or {}