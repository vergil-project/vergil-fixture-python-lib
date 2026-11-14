"""Tell whether a version string is a pre-release."""

from packaging.version import Version


def is_prerelease(version: str) -> bool:
    """Return whether *version* is a PEP 440 pre-release or development release.

    ``1.0a1``, ``1.0rc2`` and ``1.0.dev3`` are pre-releases; ``1.0`` and the
    post-release ``1.0.post1`` are not.

    Raises:
        packaging.version.InvalidVersion: *version* is not a PEP 440 version.
    """
    return Version(version).is_prerelease
