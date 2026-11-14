"""Greet a person by name."""


def greet(name: str) -> str:
    """Return a greeting for *name*, with surrounding whitespace stripped.

    Raises:
        ValueError: *name* is empty or only whitespace.
    """
    stripped = name.strip()
    if not stripped:
        msg = "name must not be blank"
        raise ValueError(msg)
    return f"Hello, {stripped}"
