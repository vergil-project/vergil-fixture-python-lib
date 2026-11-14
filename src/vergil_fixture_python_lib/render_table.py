"""Render a two-column table as plain text."""

from __future__ import annotations

import io
from typing import TYPE_CHECKING

from rich import box
from rich.console import Console
from rich.table import Table

if TYPE_CHECKING:
    from collections.abc import Mapping


def render_table(title: str, headers: tuple[str, str], rows: Mapping[str, str]) -> str:
    """Render *rows* as an ASCII table under *title*, with no terminal escapes.

    Each key of *rows* is one row, in the mapping's order: the key in the
    first column and its value in the second. The table is sized to its
    content, so the output is the same on every terminal.

    Raises:
        ValueError: *rows* is empty.
    """
    if not rows:
        msg = "rows must not be empty"
        raise ValueError(msg)
    table = Table(*headers, title=title, box=box.ASCII)
    for key, value in rows.items():
        table.add_row(key, value)
    buffer = io.StringIO()
    console = Console(file=buffer, color_system=None, width=1_000, highlight=False)
    console.print(table)
    return buffer.getvalue()
