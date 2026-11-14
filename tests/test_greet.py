"""Tests for :func:`vergil_fixture_python_lib.greet`."""

import pytest

from vergil_fixture_python_lib import greet


def test_greet_names_the_person() -> None:
    assert greet("Ada") == "Hello, Ada"


def test_greet_strips_surrounding_whitespace() -> None:
    assert greet("  Grace \n") == "Hello, Grace"


@pytest.mark.parametrize("name", ["", "   ", "\t\n"])
def test_greet_refuses_a_blank_name(name: str) -> None:
    with pytest.raises(ValueError, match="name must not be blank"):
        greet(name)
