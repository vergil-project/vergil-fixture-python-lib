"""Tests for :func:`vergil_fixture_python_lib.is_devrelease`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import is_devrelease


@pytest.mark.parametrize(
    "version", ["1.0.dev3", "v2.0.dev0", "1.0rc1.dev2", "1.0.post1.dev4", "1.0-dev"]
)
def test_is_devrelease_accepts_a_development_release(version: str) -> None:
    assert is_devrelease(version) is True


@pytest.mark.parametrize("version", ["1.0", "2.0.0", "1.0rc1", "1.0.post1", "v3.1+local.1"])
def test_is_devrelease_refuses_a_non_development_release(version: str) -> None:
    assert is_devrelease(version) is False


def test_is_devrelease_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="banana"):
        is_devrelease("banana")
