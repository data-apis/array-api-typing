__all__ = (
    "Array",
    "HasArrayNamespace",
)

from types import ModuleType
from typing import Literal, Protocol
from typing_extensions import TypeVar

NS_co = TypeVar("NS_co", covariant=True, default=ModuleType)


class HasArrayNamespace(Protocol[NS_co]):
    """Protocol for classes that have an `__array_namespace__` method.

    Example:
    >>> import array_api_typing as xpt
    >>>
    >>> class MyArray:
    ...     def __array_namespace__(self):
    ...         return object()
    >>>
    >>> x = MyArray()
    >>> def has_array_namespace(x: xpt.HasArrayNamespace) -> bool:
    ...     return hasattr(x, "__array_namespace__")
    >>> has_array_namespace(x)
    True

    """

    def __array_namespace__(
        self, /, *, api_version: Literal["2021.12"] | None = None
    ) -> NS_co: ...


class Array(
    HasArrayNamespace[NS_co],
    Protocol[NS_co],
):
    """Array API specification for array object attributes and methods."""
