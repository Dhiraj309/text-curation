"""
Example: web_common_v1 on noisy web text.

This example is intenionally small and ugly.
It demonstrates what is removed and what is preserved.
"""

from text_curation import TextCurator, reports
from datasets import Dataset

RAW_TEXT = """
MENU | ABOUT | CONTACT

Welcon to Example Corp.

We build things.
- Home
- Prodcuts
- Careers
- Blog

FOOTER
FOOTER
"""

dataset = Dataset.from_dict({
    "text": [RAW_TEXT]
})

curator = TextCurator.from_profile(profile_id="web_common_v1", collect_reports=True)

cleaned = dataset.map(curator, batched=True)

print("=== RAW ===")
print(RAW_TEXT)
print("\n=== CLEANED ===")
print(cleaned)

reports.summary(cleaned)