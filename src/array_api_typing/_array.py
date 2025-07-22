__all__ = ("HasArrayNamespace",)

from types import ModuleType
from typing import Literal, Protocol
from typing_extensions import TypeVar

NamespaceT_co = TypeVar("NamespaceT_co", covariant=True, default=ModuleType)


class HasArrayNamespace(Protocol[NamespaceT_co]):
    """Protocol for classes that have an `__array_namespace__` method.

    This `Protocol` is intended for use in static typing to ensure that an
    object has an `__array_namespace__` method that returns a namespace for
    array operations. This `Protocol` should not be used at runtime, for type
    checking or as a base class.

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
    ) -> NamespaceT_co:
        """Returns an object that has all the array API functions on it.

        Args:
            api_version: string representing the version of the array API
                specification to be returned, in 'YYYY.MM' form, for example,
                '2020.10'. If it is `None`, it should return the namespace
                corresponding to latest version of the array API specification.
                If the given version is invalid or not implemented for the given
                module, an error should be raised. Default: `None`.

        Returns:
            NamespaceT_co: An object representing the array API namespace. It
                should have every top-level function defined in the
                specification as an attribute. It may contain other public names
                as well, but it is recommended to only include those names that
                are part of the specification.

        """
        ...
