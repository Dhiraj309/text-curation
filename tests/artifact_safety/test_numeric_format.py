from text_curation import TextCurator


PROFILE = "web.pretrain.production_v1"


def test_numeric_format_preserved():

    text = "Population: 10,000 people."

    curator = TextCurator.from_profile(PROFILE)

    result = curator({"text": [text]})

    cleaned = result["text"][0]

    assert "10,000" in cleaned
