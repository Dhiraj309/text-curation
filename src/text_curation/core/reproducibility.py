import hashlib
import json

def _stable_serialize(obj) -> str:
    """
    Deterministic JSON serialization.
    """

    return json.dumps(obj, sort_keys=True, separators=(",", ":"))

def compute_pipeline_hash(profile) -> str:
    """
    Compute a deterministic hash of a profile configuration.

    Includes:
    - profile.id
    - block order
    - block class names
    - block policies (sorted)

    Does NOT include:
    - runtime stats
    - signals
    - timestamps
    - dataset content
    """

    block_config = []

    for block in profile.blocks:
        block_config.append({
            "type": block.__class__.__name__,
            "policy": dict(sorted(block.policy.items())),
        })

    payload = {
        "profile_id": profile.id,
        "blocks": block_config,
    }

    serialized = _stable_serialize(payload)

    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()