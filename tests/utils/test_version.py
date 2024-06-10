from unittest.mock import patch

import pytest

from bilibili.utils.version import get_complete_version, get_version


@pytest.mark.parametrize(
    "version, result",
    [
        ((0, 1, 0, "final", 0), "0.1"),
        ((1, 0, 1, "final", 0), "1.0.1"),
        ((1, 0, 1, "final", 1), "1.0.1"),
        ((1, 0, 0, "dev", 1), "1.0.dev1"),
        ((1, 0, 1, "dev", 1), "1.0.1.dev1"),
    ],
)
def test_get_version(version, result):
    assert get_version(version) == result


@patch("bilibili.VERSION", (0, 1, 0, "final", 0))
def test_module_version():
    assert get_version() == "0.1"


@pytest.mark.parametrize(
    "version",
    [
        (0, 1, 0, "hello", 0),
        (0, 1, 0, "final"),
        (0, 1, 0),
    ],
)
def test_invalid_version(version: tuple[int, int, int, str, int]):
    with pytest.raises(AssertionError):
        get_complete_version(version)
