"""Read the local segment of a version string."""

from packaging.version import Version


def local_version(version: str) -> str | None:
    """Return the local segment of PEP 440 version *version*.

    The local segment is the part after ``+``, and ``None`` when there is
    none: ``1.0+ubuntu.1`` gives ``ubuntu.1``, while ``v2.0`` gives ``None``.

    Raises:
        packaging.version.InvalidVersion: *version* is not a PEP 440 version.
    """
    return Version(version).local
