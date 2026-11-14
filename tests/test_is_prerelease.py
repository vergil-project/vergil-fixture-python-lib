"""Tests for :func:`vergil_fixture_python_lib.is_prerelease`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import is_prerelease


@pytest.mark.parametrize("version", ["1.0a1", "2.0.0b2", "3.1rc1", "1.0.dev3", "v2.0rc1"])
def test_is_prerelease_accepts_a_pre_release(version: str) -> None:
    assert is_prerelease(version) is True


@pytest.mark.parametrize("version", ["1.0", "2.0.0", "1.0.post1", "v3.1"])
def test_is_prerelease_refuses_a_final_release(version: str) -> None:
    assert is_prerelease(version) is False


def test_is_prerelease_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="banana"):
        is_prerelease("banana")
