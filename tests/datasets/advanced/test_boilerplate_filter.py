from datasets import Dataset
from text_curation.datasets.advanced.boilerplate_filter import (
    filter_boilerplate_documents,
)


def test_boilerplate_filter():

    data = {
        "text": [
            "Real article text.",
            "Home | About | Contact | Privacy Policy",
        ],
        "document.boilerplate_lines": [0, 1],
        "document.boilerplate_ratio": [0.0, 1.0],
    }

    ds = Dataset.from_dict(data)

    filtered, report = filter_boilerplate_documents(
        ds,
        ratio_threshold=0.5,
        min_boilerplate_lines=1,
    )

    assert len(filtered) == 1
    assert report["removed"]["samples"] == 1
