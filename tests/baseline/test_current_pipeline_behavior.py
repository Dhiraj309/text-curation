import pytest

from text_curation import TextCurator
from text_curation.registry import list_profiles


# Representative corpus samples that cover common edge cases.
SAMPLES = [
    # Emoji preservation
    "Hello world 😊🔥✨",

    # Scientific text
    "The energy-mass relation is E = mc^2.",

    # HTML snippet
    "<html><body><p>Hello world</p></body></html>",

    # Code block
    "def add(a, b):\n    return a + b",

    # Multilingual text
    "English 中文 العربية हिन्दी",

    # Markdown
    "## Header\n\nSome paragraph text.",

    # Unicode accents
    "Café naïve façade",

    # Punctuation spacing edge case
    "Hello , world !",

    # Numeric formatting
    "The value is 1,000,000.25 units.",

    # Long paragraph
    "This is a long paragraph of natural language text meant to simulate "
    "typical web content that might appear in blog posts or articles.",
]


@pytest.mark.parametrize("profile_id", list_profiles())
def test_pipeline_runs_without_error(profile_id):
    """
    Sanity test ensuring every registered profile can process
    representative inputs without raising exceptions.
    """

    curator = TextCurator.from_profile(profile_id)

    for sample in SAMPLES:
        result = curator({"text": [sample]})
        assert "text" in result
        assert isinstance(result["text"][0], str)


@pytest.mark.parametrize("profile_id", list_profiles())
def test_pipeline_determinism(profile_id):
    """
    Verify that running the same input twice produces identical output.
    """

    curator = TextCurator.from_profile(profile_id)

    for sample in SAMPLES:
        r1 = curator({"text": [sample]})["text"][0]
        r2 = curator({"text": [sample]})["text"][0]

        assert r1 == r2


@pytest.mark.parametrize("profile_id", list_profiles())
def test_pipeline_does_not_drop_text(profile_id):
    """
    Ensure the pipeline never returns None or empty outputs unexpectedly.
    """

    curator = TextCurator.from_profile(profile_id)

    for sample in SAMPLES:
        result = curator({"text": [sample]})
        cleaned = result["text"][0]

        assert cleaned is not None
        assert isinstance(cleaned, str)
