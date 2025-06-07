"""Tests for the HasArrayNamespace protocol."""

from types import SimpleNamespace
from typing import Protocol, runtime_checkable

import array_api_typing as xpt


@runtime_checkable
class CheckableHasArrayNamespace(xpt.HasArrayNamespace, Protocol):  # type: ignore[misc]
    """Runtime checkable version of HasArrayNamespace."""


class GoodArray:
    """Example class that implements the HasArrayNamespace protocol."""

    def __array_namespace__(self) -> object:  # noqa: PLW3201
        return SimpleNamespace()


class BadArray:
    """Example class that does not implement the HasArrayNamespace protocol."""


def test_has_namespace_class():
    """Test that GoodArray is a subclass of HasArrayNamespace."""
    assert issubclass(GoodArray, CheckableHasArrayNamespace)


def test_has_namespace_instance():
    """Test that an instance of GoodArray is recognized as HasArrayNamespace."""
    x = GoodArray()
    assert isinstance(x, CheckableHasArrayNamespace)


def test_not_has_namespace_class():
    """Test that BadArray is not a subclass of HasArrayNamespace."""
    assert not issubclass(BadArray, CheckableHasArrayNamespace)


def test_not_has_namespace_instance():
    """Test that an instance of BadArray is not recognized as HasArrayNamespace."""
    y = BadArray()
    assert not isinstance(y, CheckableHasArrayNamespace)
