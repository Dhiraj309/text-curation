from text_curation import TextCurator


PROFILE = "web.pretrain.production_v1"


def test_emoji_preserved():

    text = "I love this 😊🔥🚀"

    curator = TextCurator.from_profile(PROFILE)

    result = curator({"text": [text]})

    cleaned = result["text"][0]

    assert "😊" in cleaned
    assert "🔥" in cleaned
    assert "🚀" in cleaned
