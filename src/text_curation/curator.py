from text_curation.core.pipeline import Pipeline
from text_curation.registry import get_profile


class TextCurator:
    """
    High-level wrapper for applying text curation pipelines to datasets.

    `TextCurator` is designed to integrate with Hugging Face Datasets and
    provides a stateless, pure-function interface suitable for
    `dataset.map(batched=True)` workflows.
    """

    def __init__(self, profile):
        """
        Create a curator from a resolved Profile.

        Args:
            profile: A registered Profile instance
        """
        self.pipeline = Pipeline(profile.blocks)

    @classmethod
    def from_profile(cls, profile_id):
        """
        Construct a curator from a registered profile identifier.

        Args:
            profile_id: Canonical profile ID (e.g. "web_common_v1")
        """
        return cls(get_profile(profile_id))

    def __call__(self, batch):
        """
        Apply the curation pipeline to a batch of examples.

        Expects a dictionary containing a `text` field with a list of
        strings. Returns a dictionary with the same schema.

        This method is intentionally pure and side-effect free.
        """
        texts = batch["text"]
        cleaned = [self.pipeline.run(t) for t in texts]

        return {"text": cleaned}