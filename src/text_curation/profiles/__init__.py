"""
Profile package initializer.

This module discovers and imports all profile definitions
recursively so they can self-register with the global
profile registry.

Profiles rely on import-time side effects (register(PROFILE)),
so explicit discovery is required.
"""

import importlib
from importlib.resources import files

package_root = files(__name__)

# Recursively find all .py files
paths = [
    path
    for path in package_root.rglob("*.py")
    if path.name not in {"__init__.py", "base.py"}
]

# Import in deterministic order
for path in sorted(paths, key=lambda p: str(p)):
    # Convert filesystem path to module path
    relative = path.relative_to(package_root)
    module_name = ".".join(relative.with_suffix("").parts)
    importlib.import_module(f"{__name__}.{module_name}")