import re

from text_curation.blocks.base import Block


# Tags that typically contain layout or scripting rather than natural language
REMOVE_TAG_PATTERN = re.compile(
    r"<(script|style|nav|footer|aside)[^>]*>.*?</\1>",
    re.IGNORECASE | re.DOTALL
)

# Generic HTML tag pattern
_TAG = re.compile(r"<[^>]+>")


class HTMLStructureBlock(Block):
    """
    Remove HTML layout artifacts while preserving textual structure.

    Removed tags:
        <script>
        <style>
        <nav>
        <footer>
        <aside>

    Preserved tags:
        <p>
        <article>
        <pre>
        <code>

    Also strips malformed HTML fragments such as:

        <div><span>Broken html without closing

    Signals emitted:
        document.html_tags_removed
    """

    DEFAULT_POLICY = {}

    def __init__(self, policy=None):
        super().__init__(policy or {})

    def apply(self, document):

        text = document.text

        removed = 0

        def _replacement(match):
            nonlocal removed
            removed += 1
            return ""

        # Remove layout/script tags
        cleaned = REMOVE_TAG_PATTERN.sub(_replacement, text)

        # Strip malformed HTML fragments
        cleaned = self._strip_broken_html(cleaned)

        if cleaned != text:
            document.set_text(cleaned)

        document.add_signal(
            "document.html_tags_removed",
            removed
        )

        return document

    def _strip_broken_html(self, text):
        """
        Remove malformed HTML fragments such as:

            <div><span>Broken html without closing

        while preserving the underlying text.
        """

        lines = text.split("\n")
        out = []

        for line in lines:

            tags = re.findall(r"<[^>]+>", line)

            if not tags:
                out.append(line)
                continue

            # Detect if any closing tags exist
            has_closing = any(tag.startswith("</") for tag in tags)

            # If only opening tags exist → likely broken fragment
            if not has_closing:
                cleaned = _TAG.sub("", line)
                out.append(cleaned.strip())
                continue

            out.append(line)

        return "\n".join(out)
