__all__ = (
    "Array",
    "HasArrayNamespace",
)

from types import ModuleType
from typing import Literal, Protocol
from typing_extensions import Self, TypeVar

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


class CanArrayPos(Protocol):
    """Protocol for array classes that support the unary plus operator."""

    def __pos__(self) -> Self:
        """Evaluates `+self_i` for each element of an array instance.

        Returns:
            Self: An array containing the evaluated result for each element.
            The returned array must have the same data type as self.

        See Also:
            array_api_typing.Positive

        """
        ...


class CanArrayNeg(Protocol):
    """Protocol for array classes that support the unary minus operator."""

    def __neg__(self) -> Self:
        """Evaluates `-self_i` for each element of an array instance.

        Returns:
            Self: an array containing the evaluated result for each element in
            self. The returned array must have a data type determined by Type
            Promotion Rules.

        See Also:
            array_api_typing.Negative

        """
        ...


class Array(
    HasArrayNamespace[NS_co],
    CanArrayPos,
    CanArrayNeg,
    Protocol,
):
    """Array API specification for array object attributes and methods."""
