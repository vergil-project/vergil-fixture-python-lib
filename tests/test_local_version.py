"""Tests for :func:`vergil_fixture_python_lib.local_version`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import local_version


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("1.0+ubuntu.1", "ubuntu.1"),
        ("1!2.0+local.7", "local.7"),
        ("v1.2.0.post3+abc", "abc"),
        ("2.0", None),
        ("v2.0", None),
        ("1.0rc1", None),
    ],
)
def test_local_version_reads_the_local_segment(version: str, expected: str | None) -> None:
    assert local_version(version) == expected


def test_local_version_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="banana"):
        local_version("banana")
