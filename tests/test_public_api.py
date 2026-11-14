"""The package's public API is exactly what ``__all__`` names."""

import vergil_fixture_python_lib


def test_public_api_names() -> None:
    assert sorted(vergil_fixture_python_lib.__all__) == [
        "compare_versions",
        "greet",
        "latest_version",
        "render_table",
    ]


def test_public_api_names_resolve() -> None:
    for name in vergil_fixture_python_lib.__all__:
        assert callable(getattr(vergil_fixture_python_lib, name))
