"""Read the epoch of a version string."""

from packaging.version import Version


def epoch_version(version: str) -> int:
    """Return the epoch of PEP 440 version *version*.

    The epoch is the number before ``!``, and ``0`` when there is none:
    ``1!2.0`` gives ``1``, while ``2.0`` and ``v1.10.0rc1`` give ``0``.

    Raises:
        packaging.version.InvalidVersion: *version* is not a PEP 440 version.
    """
    return Version(version).epoch
