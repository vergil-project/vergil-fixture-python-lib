"""Strip a version string down to its base release."""

from packaging.version import Version


def base_version(version: str) -> str:
    """Return the base release of PEP 440 version *version*.

    The base release drops any pre-release, post-release, development or
    local segment and any leading ``v``, but keeps the epoch: ``1.2.0rc1``,
    ``v1.2.0.post3`` and ``1.2.0+local`` all give ``1.2.0``, and ``1!2.0a1``
    gives ``1!2.0``.

    Raises:
        packaging.version.InvalidVersion: *version* is not a PEP 440 version.
    """
    return Version(version).base_version
