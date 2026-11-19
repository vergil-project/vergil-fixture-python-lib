"""Tests for :func:`vergil_fixture_python_lib.major_version`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import major_version


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("1.2.0", 1),
        ("0.1.3", 0),
        ("v1.10.0rc1", 1),
        ("3", 3),
        ("2026.11", 2026),
        ("1!1.0", 1),
        ("4.0.post2+local.1", 4),
    ],
)
def test_major_version_reads_the_first_release_number(version: str, expected: int) -> None:
    assert major_version(version) == expected


def test_major_version_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="banana"):
        major_version("banana")
