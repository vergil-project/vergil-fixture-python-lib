"""Tests for :func:`vergil_fixture_python_lib.latest_version`."""

import pytest
from packaging.version import InvalidVersion

from vergil_fixture_python_lib import latest_version


def test_latest_version_picks_the_highest() -> None:
    assert latest_version(["1.2.0", "1.10.0", "1.9.9"]) == "1.10.0"


def test_latest_version_returns_the_input_spelling() -> None:
    assert latest_version(["v2.0", "1.0"]) == "v2.0"


def test_latest_version_ranks_a_final_above_its_pre_release() -> None:
    assert latest_version(["2.0.0rc1", "2.0.0", "1.9"]) == "2.0.0"


def test_latest_version_keeps_the_first_of_equal_versions() -> None:
    assert latest_version(["2.0", "2.0.0"]) == "2.0"


def test_latest_version_accepts_any_iterable() -> None:
    assert latest_version(iter(("0.1", "0.2"))) == "0.2"


def test_latest_version_refuses_no_versions() -> None:
    with pytest.raises(ValueError, match="no versions given"):
        latest_version([])


def test_latest_version_refuses_an_invalid_version() -> None:
    with pytest.raises(InvalidVersion, match="banana"):
        latest_version(["1.0", "banana"])
