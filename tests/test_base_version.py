"""Tests for :func:`vergil_fixture_python_lib.base_version`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import base_version


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("1.2.0", "1.2.0"),
        ("1.2.0rc1", "1.2.0"),
        ("2.0b2", "2.0"),
        ("1.0.dev3", "1.0"),
        ("v1.2.0.post3", "1.2.0"),
        ("1.2.0+local.7", "1.2.0"),
        ("1!2.0a1", "1!2.0"),
    ],
)
def test_base_version_strips_to_the_base_release(version: str, expected: str) -> None:
    assert base_version(version) == expected


def test_base_version_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="banana"):
        base_version("banana")
