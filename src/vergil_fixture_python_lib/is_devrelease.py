"""Tell whether a version string is a development release."""

from packaging.version import Version


def is_devrelease(version: str) -> bool:
    """Return whether *version* is a PEP 440 development release.

    ``1.0.dev3``, ``v2.0.dev0`` and ``1.0rc1.dev2`` are development releases;
    ``1.0``, the pre-release ``1.0rc1`` and the post-release ``1.0.post1``
    are not.

    Raises:
        packaging.version.InvalidVersion: *version* is not a PEP 440 version.
    """
    return Version(version).is_devrelease
