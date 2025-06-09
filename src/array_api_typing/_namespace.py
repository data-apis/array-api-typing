"""Static typing support for the array API standard."""

__all__ = ["HasArrayNamespace"]

from types import ModuleType
from typing import Protocol, final
from typing_extensions import TypeVar

T = TypeVar("T", bound=object, default=ModuleType)  # PEP 696 default


@final
class HasArrayNamespace(Protocol[T]):  # type: ignore[misc]  # see python/mypy#17288
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

    def __array_namespace__(self, /, *, api_version: str | None = None) -> T: ...  # noqa: PLW3201
