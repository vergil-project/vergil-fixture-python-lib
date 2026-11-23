# API

Every public function is importable from the package itself:

```python
from vergil_fixture_python_lib import (
    base_version,
    compare_versions,
    greet,
    is_postrelease,
    is_prerelease,
    latest_version,
    major_version,
    micro_version,
    minor_version,
    render_table,
)
```

Each function raises on bad input rather than returning a placeholder.

## `greet(name)`

Returns a greeting, with the name's surrounding whitespace stripped.

```python
>>> greet("Ada")
'Hello, Ada'
```

Raises `ValueError` when the name is empty or only whitespace.

## `compare_versions(left, right)`

Compares two [PEP 440](https://peps.python.org/pep-0440/) version strings,
using `packaging`. Returns `-1`, `0` or `1` as `left` is lower than, equal to
or higher than `right`.

```python
>>> compare_versions("1.2.0", "1.10.0")
-1
>>> compare_versions("2.0", "2.0.0")
0
```

Raises `packaging.version.InvalidVersion` when either string is not a PEP 440
version.

## `latest_version(versions)`

Returns the highest PEP 440 version in an iterable of strings, spelt as given.
Of equal versions, the first one wins.

```python
>>> latest_version(["1.2.0", "1.10.0", "1.9.9"])
'1.10.0'
```

Raises `ValueError` when there are no versions, and
`packaging.version.InvalidVersion` when a string is not a PEP 440 version.

## `is_prerelease(version)`

Returns whether a PEP 440 version string is a pre-release (alpha, beta or
release candidate) or a development release. A final release and a
post-release are not.

```python
>>> is_prerelease("2.0.0rc1")
True
>>> is_prerelease("1.0.post1")
False
```

Raises `packaging.version.InvalidVersion` when the string is not a PEP 440
version.

## `is_postrelease(version)`

Returns whether a PEP 440 version string is a post-release. A final release,
a pre-release and a development release are not, unless they also carry a
post-release segment.

```python
>>> is_postrelease("1.0.post1")
True
>>> is_postrelease("2.0.0rc1")
False
```

Raises `packaging.version.InvalidVersion` when the string is not a PEP 440
version.

## `base_version(version)`

Returns the base release of a PEP 440 version string: its release numbers,
with any pre-release, post-release, development or local segment and any
leading `v` dropped. An epoch is kept.

```python
>>> base_version("1.2.0rc1")
'1.2.0'
>>> base_version("v1.2.0.post3")
'1.2.0'
```

Raises `packaging.version.InvalidVersion` when the string is not a PEP 440
version.

## `major_version(version)`

Returns the major release number of a PEP 440 version string, as an `int`:
its first release number, ignoring any epoch, leading `v` and anything after
the release numbers.

```python
>>> major_version("v1.10.0rc1")
1
>>> major_version("2026.11")
2026
```

Raises `packaging.version.InvalidVersion` when the string is not a PEP 440
version.

## `micro_version(version)`

Returns the micro release number of a PEP 440 version string, as an `int`:
its third release number, ignoring any epoch, leading `v` and anything after
the release numbers. A version with fewer than three release numbers has a
micro number of `0`.

```python
>>> micro_version("v1.10.12rc1")
12
>>> micro_version("1.2")
0
```

Raises `packaging.version.InvalidVersion` when the string is not a PEP 440
version.

## `minor_version(version)`

Returns the minor release number of a PEP 440 version string, as an `int`:
its second release number, ignoring any epoch, leading `v` and anything after
the release numbers. A version with one release number has a minor number of
`0`.

```python
>>> minor_version("v1.10.0rc1")
10
>>> minor_version("3")
0
```

Raises `packaging.version.InvalidVersion` when the string is not a PEP 440
version.

## `render_table(title, headers, rows)`

Renders a mapping as a two-column ASCII table with `rich`, as plain text with
no terminal escapes. Each key is one row, in the mapping's order.

```python
>>> print(render_table("Versions", ("Name", "Version"), {"rich": "14.0", "uv": "0.13"}), end="")
     Versions
+----------------+
| Name | Version |
|------+---------|
| rich | 14.0    |
| uv   | 0.13    |
+----------------+
```

Raises `ValueError` when `rows` is empty.
