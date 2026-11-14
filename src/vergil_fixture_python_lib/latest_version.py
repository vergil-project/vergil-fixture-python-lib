"""Pick the highest of several version strings."""

from __future__ import annotations

from typing import TYPE_CHECKING

from packaging.version import Version

if TYPE_CHECKING:
    from collections.abc import Iterable


def latest_version(versions: Iterable[str]) -> str:
    """Return the highest PEP 440 version in *versions*, spelt as given.

    Of equal versions (``2.0`` and ``2.0.0``) the first one wins.

    Raises:
        ValueError: *versions* is empty.
        packaging.version.InvalidVersion: a string is not a PEP 440 version.
    """
    parsed = [(Version(text), text) for text in versions]
    if not parsed:
        msg = "no versions given"
        raise ValueError(msg)
    return max(parsed, key=lambda pair: pair[0])[1]
