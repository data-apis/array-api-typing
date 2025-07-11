"""Utility functions."""

from collections.abc import Callable
from enum import Enum, auto
from typing import Literal, TypeVar

ClassT = TypeVar("ClassT")
DocstringTypes = str | None


class _Sentinel(Enum):
    SKIP = auto()


def set_docstrings(
    obj: type[ClassT],
    main: DocstringTypes | Literal[_Sentinel.SKIP] = _Sentinel.SKIP,
    /,
    **method_docs: DocstringTypes,
) -> type[ClassT]:
    """Set the docstring for a class and its methods.

    Args:
        obj: The class to set the docstring for.
        main: The main docstring for the class. If not provided, the
            class docstring will not be modified.
        method_docs: A mapping of method names to their docstrings. If a method
            is not provided, its docstring will not be modified.

    Returns:
        The class with updated docstrings.

    """
    if main is not _Sentinel.SKIP:
        obj.__doc__ = main

    for name, doc in method_docs.items():
        method = getattr(obj, name)
        method.__doc__ = doc
    return obj


def docstring_setter(
    main: DocstringTypes | Literal[_Sentinel.SKIP] = _Sentinel.SKIP,
    /,
    **method_docs: DocstringTypes,
) -> Callable[[type[ClassT]], type[ClassT]]:
    """Decorator to set docstrings for a class and its methods.

    Args:
        main: The main docstring for the class. If not provided, the
            class docstring will not be modified.
        method_docs: A mapping of method names to their docstrings. If a method
            is not provided, its docstring will not be modified.

    Returns:
        A decorator that sets the docstrings for the class and its methods.

    """

    def decorator(cls: type[ClassT]) -> type[ClassT]:
        return set_docstrings(cls, main, **method_docs)

    return decorator
