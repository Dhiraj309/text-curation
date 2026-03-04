import unicodedata
from collections import Counter

from text_curation.blocks.base import Block


class UnicodeIntegrityBlock(Block):
    """
    Ensure Unicode integrity and emit diagnostic signals.

    Responsibilities
    ----------------
    • Apply safe Unicode normalization (default NFC)
    • Detect presence of replacement characters (�)
    • Count emoji occurrences
    • Estimate Unicode script distribution

    This block MUST NOT:
    • remove non-ASCII characters
    • remove emoji
    • filter scripts

    It only repairs encoding inconsistencies and emits signals.
    """

    DEFAULT_POLICY = {
        "normalization": "NFC",
    }

    def __init__(self, policy=None):
        merged = {**self.DEFAULT_POLICY, **(policy or {})}
        super().__init__(merged)

    def apply(self, document):

        original = document.text

        # -----------------------------------------------------
        # Unicode normalization
        # -----------------------------------------------------

        normalized = unicodedata.normalize(
            self.policy["normalization"],
            original,
        )

        # Count how many characters changed
        repair_count = sum(
            1 for a, b in zip(original, normalized) if a != b
        )

        if normalized != original:
            document.set_text(normalized)

        text = normalized

        # -----------------------------------------------------
        # Replacement character detection
        # -----------------------------------------------------

        replacement_count = text.count("\uFFFD")

        # -----------------------------------------------------
        # Emoji detection
        # -----------------------------------------------------

        emoji_count = sum(
            1 for ch in text if ord(ch) > 0xFFFF
        )

        # -----------------------------------------------------
        # Script distribution estimation
        # -----------------------------------------------------

        scripts = []

        for ch in text:
            if ch.isalpha():
                try:
                    name = unicodedata.name(ch)
                    scripts.append(name.split()[0])
                except ValueError:
                    continue

        script_counts = Counter(scripts)

        # -----------------------------------------------------
        # Emit signals
        # -----------------------------------------------------

        document.add_signal(
            "document.unicode_repair_count",
            repair_count,
        )

        document.add_signal(
            "document.unicode_replacement_characters",
            replacement_count,
        )

        document.add_signal(
            "document.emoji_count",
            emoji_count,
        )

        document.add_signal(
            "document.unicode_script_distribution",
            dict(script_counts),
        )

        return document
