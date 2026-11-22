"""Vergil test fixture: a small Python library with no users.

Each public function lives in a module of its own name and is re-exported
here, so adding one means one new module, one import and one ``__all__``
entry.
"""

from vergil_fixture_python_lib.base_version import base_version
from vergil_fixture_python_lib.compare_versions import compare_versions
from vergil_fixture_python_lib.greet import greet
from vergil_fixture_python_lib.is_prerelease import is_prerelease
from vergil_fixture_python_lib.latest_version import latest_version
from vergil_fixture_python_lib.major_version import major_version
from vergil_fixture_python_lib.minor_version import minor_version
from vergil_fixture_python_lib.render_table import render_table

__all__ = [
    "base_version",
    "compare_versions",
    "greet",
    "is_prerelease",
    "latest_version",
    "major_version",
    "minor_version",
    "render_table",
]
