"""Tests for :func:`vergil_fixture_python_lib.is_postrelease`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import is_postrelease


@pytest.mark.parametrize(
    "version", ["1.0.post1", "v2.0.post0", "1.0rc1.post2", "1.0-1", "3.1.post4.dev1"]
)
def test_is_postrelease_accepts_a_post_release(version: str) -> None:
    assert is_postrelease(version) is True


@pytest.mark.parametrize("version", ["1.0", "2.0.0", "1.0rc1", "1.0.dev3", "v3.1+local.1"])
def test_is_postrelease_refuses_a_non_post_release(version: str) -> None:
    assert is_postrelease(version) is False


def test_is_postrelease_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="banana"):
        is_postrelease("banana")
