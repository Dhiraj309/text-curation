"""
Example: web_common_v1 on noisy web text.

This example is intenionally small and ugly.
It demonstrates what is removed and what is preserved.
"""

from text_curation import TextCurator

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

curator = TextCurator.from_profile(profile_name="web_common_v1")

cleaned = curator({
    "text": [RAW_TEXT]
})["text"][0]

print("=== RAW ===")
print(RAW_TEXT)
print("\n=== CLEANED ===")
print(cleaned)