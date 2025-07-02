__all__ = ("HasArrayNamespace",)

from types import ModuleType
from typing import Protocol
from typing_extensions import TypeVar

T_co = TypeVar("T_co", covariant=True, default=ModuleType)


class HasArrayNamespace(Protocol[T_co]):
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

    def __array_namespace__(self, /, *, api_version: str | None = None) -> T_co: ...  # noqa: PLW3201
