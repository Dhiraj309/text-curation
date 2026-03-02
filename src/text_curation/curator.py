from text_curation.core.pipeline import Pipeline
from text_curation.registry import get_profile


class TextCurator:
    __slots__ = ("_profile", "_collect_reports", "_pipeline")

    def __init__(self, profile, collect_reports: bool = False):
        object.__setattr__(self, "_profile", profile)
        object.__setattr__(self, "_collect_reports", collect_reports)
        object.__setattr__(self, "_pipeline", Pipeline(profile.blocks))

    @classmethod
    def from_profile(cls, profile_id, *, collect_reports: bool = False):
        profile = get_profile(profile_id)
        return cls(profile, collect_reports=collect_reports)

    # 🔒 Runtime immutability
    def __setattr__(self, key, value):
        raise TypeError("TextCurator instances are immutable")

    # 🔁 Multiprocessing / pickle support
    def __getstate__(self):
        """
        Return minimal deterministic state for multiprocessing.
        """
        return {
            "profile_id": self._profile.id,
            "collect_reports": self._collect_reports,
        }

    def __setstate__(self, state):
        """
        Reconstruct instance safely during unpickling.
        """
        profile = get_profile(state["profile_id"])
        object.__setattr__(self, "_profile", profile)
        object.__setattr__(self, "_collect_reports", state["collect_reports"])
        object.__setattr__(self, "_pipeline", Pipeline(profile.blocks))

    @property
    def profile(self):
        return self._profile

    @property
    def collect_reports(self):
        return self._collect_reports

    @property
    def pipeline(self):
        return self._pipeline

    def __call__(self, batch):
        texts = list(batch["text"])

        if not self._collect_reports:
            cleaned = [self._pipeline.run(t) for t in texts]
            return {"text": cleaned}

        cleaned = []
        reports = []

        for t in texts:
            doc, report = self._pipeline.run_document(
                t,
                collect_report=True,
                profile_id=self._profile.id,
            )
            cleaned.append(doc.text)
            reports.append(report.to_dict())

        return {
            "text": cleaned,
            "curation_report": reports,
        }
