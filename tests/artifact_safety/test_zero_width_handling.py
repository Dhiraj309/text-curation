from text_curation.curator import TextCurator


PROFILE = "web.pretrain.production_v1"


def test_zero_width_replaced_with_space():

    text = "This text\u200Bcontains zero width characters."

    curator = TextCurator.from_profile(PROFILE)

    result = curator({"text": [text]})
    cleaned = result["text"][0]

    assert "text contains" in cleaned
