"""Static typing support for the array API standard."""

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol
from typing_extensions import TypeVar

if TYPE_CHECKING:
    from ._array import Array
    from ._device import Device
    from ._dtype import DType
    from .signature_types import NestedSequence, SupportsBufferProtocol

    A = TypeVar("A", bound=Array, default=Array)  # PEP 696 default
else:
    A = TypeVar("A")


class ArrayNamespace(Protocol[A]):
    """An Array API namespace."""

    def asarray(
        self,
        obj: Array | complex | NestedSequence[complex] | SupportsBufferProtocol,
        /,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
        copy: bool | None = None,
        **kwargs: object,
    ) -> A: ...

    def astype(
        self,
        x: A,
        dtype: DType,
        /,
        *,
        copy: bool = True,
        device: Device | None = None,
    ) -> A: ...


T = TypeVar("T", bound=ArrayNamespace, default=ArrayNamespace)  # PEP 696 default


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
