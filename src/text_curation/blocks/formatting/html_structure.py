import re

from text_curation.blocks.base import Block


# Tags that typically contain layout or scripting rather than natural language.
REMOVE_TAG_PATTERN = re.compile(
    r"<(script|style|nav|footer|aside)[^>]*>.*?</\1>",
    re.IGNORECASE | re.DOTALL
)


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

    This block performs minimal structural cleanup and does not attempt
    to render or fully parse HTML.

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

        cleaned = REMOVE_TAG_PATTERN.sub(_replacement, text)

        if cleaned != text:
            document.set_text(cleaned)

        document.add_signal(
            "document.html_tags_removed",
            removed
        )

        return document
