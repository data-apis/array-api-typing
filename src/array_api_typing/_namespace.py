__all__ = ("HasArrayNamespace",)

from __future__ import annotations

from typing import TYPE_CHECKING, Protocol
from typing_extensions import TypeVar

if TYPE_CHECKING:
    # This condition exists to prevent a circular import: _array imports _namespace for
    # HasArrayNamespace. Therefore, _namespace cannot import _array except when
    # type-checking. The type variable depends on Array, so we create a dummy type
    # variable without the same bounds and default for this case.  In Python 3.13, this
    # is no longer be necessary.
    from typing_extensions import Buffer

    from ._array import Array
    from ._misc_objects import Device, DType
    from .signature_types import NestedSequence

    A = TypeVar("A", bound=Array, default=Array)  # PEP 696 default
else:
    A = TypeVar("A")


class ArrayNamespace(Protocol[A]):
    """An Array API namespace."""

    def asarray(
        self,
        obj: Array | complex | NestedSequence[complex] | Buffer,
        /,
        *,
        dtype: DType | None = None,
        device: Device | None = None,
        copy: bool | None = None,
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
