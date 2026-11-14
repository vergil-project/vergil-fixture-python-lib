"""Compare two version strings."""

from packaging.version import Version


def compare_versions(left: str, right: str) -> int:
    """Compare two PEP 440 version strings.

    Returns -1 when *left* is lower than *right*, 0 when they are equal
    (``2.0`` equals ``2.0.0``) and 1 when *left* is higher.

    Raises:
        packaging.version.InvalidVersion: either string is not a PEP 440 version.
    """
    left_version = Version(left)
    right_version = Version(right)
    if left_version < right_version:
        return -1
    if left_version > right_version:
        return 1
    return 0
