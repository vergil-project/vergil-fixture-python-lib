# Getting Started

The library is not on PyPI. Depend on a release tag (`v<version>`) straight
from GitHub:

```bash
uv add 'vergil-fixture-python-lib @ git+https://github.com/vergil-project/vergil-fixture-python-lib@<tag>'
```

It needs Python 3.12 or later, and installs `rich` and `packaging` with it.

## Validating a change

Work in a worktree of the repo and run the one validation command:

```bash
vrg-container-run -- vrg-validate
```

It runs lint, type checks, the tests at 100% branch coverage and the
dependency audit in the Python dev container.

## Adding a function

Each fixture run adds one function:

1. Write `tests/test_<name>.py` with the expected values.
2. Add `src/vergil_fixture_python_lib/<name>.py` holding the function.
3. Import it in `src/vergil_fixture_python_lib/__init__.py` and add it to
   `__all__`, and to the list in `tests/test_public_api.py`.
4. Document it on the [API](api.md) page.
