"""Tests for :func:`vergil_fixture_python_lib.minor_version`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import minor_version


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("1.2.0", 2),
        ("0.1.3", 1),
        ("v1.10.0rc1", 10),
        ("3", 0),
        ("2026.11", 11),
        ("1!1.2", 2),
        ("4.7.post2+local.1", 7),
    ],
)
def test_minor_version_reads_the_second_release_number(version: str, expected: int) -> None:
    assert minor_version(version) == expected


def test_minor_version_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="banana"):
        minor_version("banana")
