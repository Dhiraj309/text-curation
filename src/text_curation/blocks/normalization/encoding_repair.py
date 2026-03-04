import ftfy

from text_curation.blocks.base import Block


class EncodingRepairBlock(Block):
    """
    Repair common encoding corruption (mojibake) found in web corpora.

    Examples repaired:

        FranÃ§ais → Français
        cafÃ© → café
        MÃ¼nchen → München

    This block is deterministic and does not remove characters.
    It only repairs encoding artifacts.

    Signals emitted:
        document.encoding_repair_count
    """

    DEFAULT_POLICY = {
        "use_ftfy": True,
    }

    def __init__(self, policy=None):
        merged = {**self.DEFAULT_POLICY, **(policy or {})}
        super().__init__(merged)

    def apply(self, document):

        text = document.text

        repaired = text

        if self.policy["use_ftfy"]:
            repaired = ftfy.fix_text(text)

        if repaired != text:
            document.set_text(repaired)
            document.add_signal("document.encoding_repair_count", 1)
        else:
            document.add_signal("document.encoding_repair_count", 0)

        return document
