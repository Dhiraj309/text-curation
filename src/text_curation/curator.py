from text_curation.profiles.web_common_v1 import PIPELINE

class TextCurator:
    """
    High-level wrapper for applying text curation pipelines to datasets.

    `TextCurator` is designed to integrate with Hugging Face Datasets and
    provides a stateless, pure-function interface suitable for
    `dataset.map(batched=True)` workflows.
    """
        
    def __init__(self, pipeline):
        """
        Initialize a curator with a specific pipeline.
        """
        self.pipeline = pipeline

    @classmethod
    def from_profiles(cls, profile_name: str, dataset: str | None = None):
        """
        Construct a curator from a named built-in profile.

        Profiles define a fixed, versioned pipeline contract.
        """
                
        if profile_name != "web_common_v1":
            raise ValueError(f"Unknown Profile: {profile_name}")
        return cls(PIPELINE)
    
    def __call__(self, batch):
        """
        Apply the curation pipeline to a batch of examples.

        Expects a dictionary containing a `text` field with a list of
        strings. Returns a dictionary with the same schema.
        """
         
        texts = batch["text"]
        cleaned = [self.pipeline.run(t) for t in texts]

        return {"text": cleaned}