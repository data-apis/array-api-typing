"""Static typing support for the array API standard."""

__all__ = ["HasNamespace"]

from types import ModuleType
from typing import Protocol, final
from typing_extensions import TypeVar

T = TypeVar("T", bound=object, default=ModuleType)  # PEP 696 default


@final
class HasNamespace(Protocol[T]):  # type: ignore[misc]  # see python/mypy#17288
    """Protocol for classes that have an `__array_namespace__` method.

    This is for type-annotating objects that should

    Example:
    >>> import array_api_typing as xpt
    >>>
    >>> class MyArray:
    ...     def __array_namespace__(self):
    ...         return object()
    >>>
    >>> x = MyArray()
    >>> def has_namespace(x: xpt.HasNamespace) -> bool:
    ...     return hasattr(x, "__array_namespace__")
    >>> has_namespace(x)
    True

    """

    def __array_namespace__(self, /, *, api_version: str | None = None) -> T: ...  # noqa: PLW3201
