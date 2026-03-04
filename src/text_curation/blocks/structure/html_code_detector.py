import re

from text_curation.blocks.base import Block


HTML_CODE_PATTERN = re.compile(
    r"<(pre|code|script|style)[^>]*>.*?</\1>",
    re.IGNORECASE | re.DOTALL
)


class HtmlCodeDetector(Block):
    """
    Detect HTML regions that contain code or non-text content.

    Supported tags:

        <pre>
        <code>
        <script>
        <style>

    Detected regions are stored in:

        document.annotations["html_code_regions"]

    Each region is a tuple:

        (start_offset, end_offset)

    This block does NOT modify text.
    """

    DEFAULT_POLICY = {}

    def __init__(self, policy=None):
        super().__init__(policy or {})

    def apply(self, document):

        text = document.text

        regions = []

        for match in HTML_CODE_PATTERN.finditer(text):
            regions.append((match.start(), match.end()))

        if regions:
            existing = document.annotations.get("html_code_regions", [])
            document.annotations["html_code_regions"] = existing + regions
        else:
            document.annotations.setdefault("html_code_regions", [])

        document.add_signal(
            "document.html_code_blocks",
            len(regions)
        )

        return document
