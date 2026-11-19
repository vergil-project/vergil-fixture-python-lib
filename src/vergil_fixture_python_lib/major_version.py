"""Read the major release number of a version string."""

from packaging.version import Version


def major_version(version: str) -> int:
    """Return the major release number of PEP 440 version *version*.

    The major number is the first release number, whatever follows it and
    ignoring any epoch and leading ``v``: ``1.2.0``, ``v1.10.0rc1`` and
    ``1!1.0`` all give ``1``, and ``2026.11`` gives ``2026``.

    Raises:
        packaging.version.InvalidVersion: *version* is not a PEP 440 version.
    """
    return Version(version).major
