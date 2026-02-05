"""
Profile package initializer.

This module is responsible for discovering and importing all
profile definitions so they can self-register with the global
profile registry.

Profiles rely on import-time side effects (register(PROFILE)),
so explicit discovery is required.
"""

import importlib
from importlib.resources import files

# Dynamically import all profile modules in a deterministic order.
# Profiles rely on import-time registration, so ordering must be stable.

paths = [
    path
    for path in files(__name__).iterdir()
    if path.suffix == ".py" and path.name not in {"__init__.py", "base.py"}
]

for path in sorted(paths, key=lambda p: p.name):
    importlib.import_module(f"{__name__}.{path.stem}")