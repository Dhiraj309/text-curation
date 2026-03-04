import re
from text_curation.blocks.base import Block


FENCE_START_RE = re.compile(r"^\s*(```|~~~)")


class CodeFenceDetector(Block):
    """
    Detect Markdown-style fenced code blocks.

    Supports:
        ```code fences
        ~~~code fences

    Regions are recorded as:

        document.annotations["code_regions"]

    Each region is a tuple:
        (start_offset, end_offset)

    The detector is tolerant to missing closing fences,
    which commonly occur in scraped web text.
    """

    DEFAULT_POLICY = {}

    def __init__(self, policy=None):
        super().__init__(policy or {})

    def apply(self, document):

        text = document.text
        lines = text.splitlines(keepends=True)

        regions = []

        inside_fence = False
        fence_start = None
        current_offset = 0

        for line in lines:

            if FENCE_START_RE.match(line):

                if not inside_fence:
                    # Opening fence
                    inside_fence = True
                    fence_start = current_offset

                else:
                    # Closing fence
                    regions.append((fence_start, current_offset + len(line)))
                    inside_fence = False
                    fence_start = None

            current_offset += len(line)

        # Handle truncated fences (common in web scrapes)
        if inside_fence and fence_start is not None:
            regions.append((fence_start, len(text)))

        if regions:
            existing = document.annotations.get("code_regions", [])
            document.annotations["code_regions"] = existing + regions
        else:
            document.annotations.setdefault("code_regions", [])

        document.add_signal(
            "document.code_fence_blocks",
            len(regions)
        )

        return document
