from datasets import Dataset
from text_curation.datasets.advanced.boilerplate_filter import boilerplate_filter


def test_pipe_navigation_removed():

    ds = Dataset.from_dict({
        "text": [
            "Home | About | Contact | Privacy Policy",
            "This is a real article sentence."
        ]
    })

    cleaned, report = boilerplate_filter(ds, column="text")

    assert len(cleaned) == 1
    assert "article sentence" in cleaned["text"][0]
