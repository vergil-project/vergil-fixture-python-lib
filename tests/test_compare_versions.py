"""Tests for :func:`vergil_fixture_python_lib.compare_versions`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import compare_versions


@pytest.mark.parametrize(
    ("left", "right", "expected"),
    [
        ("1.2.0", "1.10.0", -1),
        ("2.0.0", "2.0", 0),
        ("1.0.0", "1.0.0rc1", 1),
        ("v3.1", "3.1.0", 0),
    ],
)
def test_compare_versions_orders_by_pep_440(left: str, right: str, expected: int) -> None:
    assert compare_versions(left, right) == expected


def test_compare_versions_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="not-a-version"):
        compare_versions("not-a-version", "1.0")
