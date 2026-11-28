"""Steps of the live run chain."""


def step_1() -> int:
    """Return the first chain step's value, 1."""
    return 1


def step_2() -> int:
    """Return the second step, built on `step_1`."""
    return step_1() + 1


def step_3() -> int:
    """Return step three."""
    return step_2() + 1


def step_4() -> int:
    """Return the fourth step."""
    return step_3() + 1


def step_5() -> int:
    return step_4() + 1
