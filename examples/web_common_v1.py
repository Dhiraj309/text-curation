"""
Example: web_common_v1 on noisy web text.

This example demonstrates how the web_common_v1 profile cleans
typical navigation-heavy and repetitive web content, and how to
inspect the results using the reporting utilities introduced in v1.2.0.
"""

from text_curation import TextCurator
from text_curation.reports import summary


RAW_TEXT = """
MENU | ABOUT | CONTACT

Welcome to Example Corp.
We build things.

- Home
- Products
- Careers
- Blog

FOOTER
FOOTER
"""


# Create a curator using the stable web_common_v1 profile
# and enable report collection.
curator = TextCurator.from_profile(
    "web_common_v1",
    collect_reports=True,
)

# Apply the curator to a small in-memory batch
cleaned = curator({
    "text": [RAW_TEXT]
})

print("=== RAW ===")
print(RAW_TEXT)

print("\n=== CLEANED ===")
print(cleaned["text"][0])

print("\n=== CURATION SUMMARY ===")
summary(cleaned)
