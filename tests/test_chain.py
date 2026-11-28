"""Tests for :func:`vergil_fixture_python_lib.chain.step_1`."""

from vergil_fixture_python_lib.chain import step_1, step_2


def test_step_1() -> None:
    assert step_1() == 1


def test_step_2() -> None:
    assert step_2() == 2
