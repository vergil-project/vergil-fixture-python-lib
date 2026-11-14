"""Tests for :func:`vergil_fixture_python_lib.render_table`."""

import pytest

from vergil_fixture_python_lib import render_table


def test_render_table_draws_a_two_column_table() -> None:
    expected = (
        "     Versions     \n"
        "+----------------+\n"
        "| Name | Version |\n"
        "|------+---------|\n"
        "| rich | 14.0    |\n"
        "| uv   | 0.13    |\n"
        "+----------------+\n"
    )
    rendered = render_table("Versions", ("Name", "Version"), {"rich": "14.0", "uv": "0.13"})
    assert rendered == expected


def test_render_table_keeps_the_row_order() -> None:
    rendered = render_table("T", ("K", "V"), {"b": "2", "a": "1"})
    assert rendered.index("| b ") < rendered.index("| a ")


def test_render_table_has_no_terminal_escapes() -> None:
    assert "\x1b" not in render_table("T", ("K", "V"), {"k": "v"})


def test_render_table_refuses_no_rows() -> None:
    with pytest.raises(ValueError, match="rows must not be empty"):
        render_table("T", ("K", "V"), {})
