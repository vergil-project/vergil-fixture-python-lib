# vergil-fixture-python-lib

This is a Vergil test fixture, a small Python library with no users. It exists
to exercise Vergil's management of a Python library repo end to end: the
`vrg-validate` gate, CI across the Python version window, the dependency
updater and audit, the tagged release and the docs site. The design is in the
[language fixture repos spec](https://github.com/vergil-project/.github/blob/develop/epics/1091-language-fixture-repos/spec.md).

## Table of Contents

- [Status](#status)
- [Overview](#overview)
- [Getting Started](#getting-started)
- [License](#license)

## Status

A test fixture. Nothing here is published to a package registry.

## Overview

The library is a few small public functions, listed on the
[API](https://vergil-project.github.io/vergil-fixture-python-lib/api/) page. Its
runtime dependencies are `rich` and `packaging`. Each fixture run adds one
function, each in a module of its own name under `src/vergil_fixture_python_lib/`.

## Getting Started

See the [documentation](https://vergil-project.github.io/vergil-fixture-python-lib/).
Validate a change with `vrg-container-run -- vrg-validate`.

## License

MIT — see [LICENSE](LICENSE).
