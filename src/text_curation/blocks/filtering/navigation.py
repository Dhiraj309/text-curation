import re

from text_curation.blocks.base import Block


NAV_SEPARATOR_RE = re.compile(r"\s*\|\s*")
NAV_WORD_RE = re.compile(
    r"(home|about|contact|privacy|terms|login|register|blog|docs|help)",
    re.IGNORECASE
)


class NavigationDetectionBlock(Block):
    """
    Detect navigation-style lines commonly found in web menus.

    Example patterns:

        Home | About | Contact
        Products | Pricing | Docs
        Login | Register | Help

    This block emits signals but does not modify text.

    Signals:
        document.navigation_lines
        document.navigation_ratio
    """

    DEFAULT_POLICY = {
        "min_links": 3,
    }

    def __init__(self, policy=None):
        merged = {**self.DEFAULT_POLICY, **(policy or {})}
        super().__init__(merged)

    def apply(self, document):

        text = document.text
        lines = [l.strip() for l in text.split("\n") if l.strip()]

        if not lines:
            document.add_signal("document.navigation_lines", 0)
            document.add_signal("document.navigation_ratio", 0.0)
            return document

        nav_lines = 0

        for line in lines:

            # pattern: link clusters separated by |
            if NAV_SEPARATOR_RE.search(line):
                parts = NAV_SEPARATOR_RE.split(line)

                if len(parts) >= self.policy["min_links"]:
                    nav_lines += 1
                    continue

            # pattern: short navigation keyword lines
            if NAV_WORD_RE.search(line) and len(line.split()) <= 6:
                nav_lines += 1

        ratio = nav_lines / len(lines)

        document.add_signal(
            "document.navigation_lines",
            nav_lines,
        )

        document.add_signal(
            "document.navigation_ratio",
            round(ratio, 6),
        )

        return document
