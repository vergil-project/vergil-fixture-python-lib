# API

Every public function is importable from the package itself:

```python
from vergil_fixture_python_lib import compare_versions, greet, latest_version, render_table
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
