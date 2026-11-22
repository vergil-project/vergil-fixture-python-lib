"""Read the minor release number of a version string."""

from packaging.version import Version


def minor_version(version: str) -> int:
    """Return the minor release number of PEP 440 version *version*.

    The minor number is the second release number, whatever follows it and
    ignoring any epoch and leading ``v``: ``1.2.0``, ``v1.2.0rc1`` and
    ``1!1.2`` all give ``2``. A version with a single release number has a
    minor number of ``0``, so ``3`` gives ``0``.

    Raises:
        packaging.version.InvalidVersion: *version* is not a PEP 440 version.
    """
    return Version(version).minor
