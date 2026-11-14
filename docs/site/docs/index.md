# vergil-fixture-python-lib

This is a Vergil test fixture. It has no users. It is a small, real Python
library that Vergil manages exactly as it manages any other library repo, so
that a change to Vergil can be driven through it end to end before the change
reaches a repo that matters.

## What it exercises

A fixture run takes the repo through Vergil's full cycle: a change, its PR
and CI, the merge, a release, and a check of the result. On the way it
exercises:

- the Python `vrg-validate` gate: ruff, mypy, ty, pytest at 100% branch
  coverage, pip-audit and the license check;
- CI on every Python version in the version window, as a library gets;
- the dependency updater, Dependabot alerts and the vulnerability audit,
  through two real runtime dependencies, `rich` and `packaging`;
- the tagged release and this documentation site.

Nothing it does reaches a package registry: it is never published to PyPI.

The program grows by one small function per fixture run. Each public function
lives in a module of its own name, so a new one is a new module, a new test
file and one line in the package's `__init__.py`.

## Why it exists

The design is in the
[language fixture repos spec](https://github.com/vergil-project/.github/blob/develop/epics/1091-language-fixture-repos/spec.md)
(epic vergil-project/.github#1091).

## Where next

- [Getting Started](getting-started.md): depend on it and validate it.
- [API](api.md): the public functions and how to call them.
