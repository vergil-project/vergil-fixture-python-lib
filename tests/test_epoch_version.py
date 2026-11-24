"""Tests for :func:`vergil_fixture_python_lib.epoch_version`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import epoch_version


@pytest.mark.parametrize(
    ("version", "expected"),
    [
        ("1!2.0", 1),
        ("2!1.0rc1", 2),
        ("v3!1.0.post1+local.1", 3),
        ("0!1.0", 0),
        ("2.0", 0),
        ("v1.10.0rc1", 0),
    ],
)
def test_epoch_version_reads_the_epoch(version: str, expected: int) -> None:
    assert epoch_version(version) == expected


def test_epoch_version_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="banana"):
        epoch_version("banana")
