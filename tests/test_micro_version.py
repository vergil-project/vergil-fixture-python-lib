"""Tests for :func:`vergil_fixture_python_lib.micro_version`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import micro_version


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("1.2.3", 3),
        ("0.1.5", 5),
        ("v1.10.12rc1", 12),
        ("1.2", 0),
        ("3", 0),
        ("1!1.2.3", 3),
        ("4.7.9.1", 9),
        ("4.7.2.post2+local.1", 2),
    ],
)
def test_micro_version_reads_the_third_release_number(version: str, expected: int) -> None:
    assert micro_version(version) == expected


def test_micro_version_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="banana"):
        micro_version("banana")
