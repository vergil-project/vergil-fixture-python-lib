"""Tell whether a version string is a post-release."""

from packaging.version import Version


def is_postrelease(version: str) -> bool:
    """Return whether *version* is a PEP 440 post-release.

    ``1.0.post1``, ``v2.0.post0`` and ``1.0rc1.post2`` are post-releases;
    ``1.0``, the pre-release ``1.0rc1`` and the development release
    ``1.0.dev3`` are not.

    Raises:
        packaging.version.InvalidVersion: *version* is not a PEP 440 version.
    """
    return Version(version).is_postrelease
