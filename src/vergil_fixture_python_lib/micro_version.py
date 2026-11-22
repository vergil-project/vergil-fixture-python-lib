"""Read the micro release number of a version string."""

from packaging.version import Version


def micro_version(version: str) -> int:
    """Return the micro release number of PEP 440 version *version*.

    The micro number is the third release number, whatever follows it and
    ignoring any epoch and leading ``v``: ``1.2.3``, ``v1.2.3rc1`` and
    ``1!1.2.3`` all give ``3``. A version with fewer than three release
    numbers has a micro number of ``0``, so ``1.2`` gives ``0``.

    Raises:
        packaging.version.InvalidVersion: *version* is not a PEP 440 version.
    """
    return Version(version).micro
