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


class CanArrayAdd(Protocol):
    """Protocol for array classes that support the addition operator."""

    def __add__(self, other: Self | int | float, /) -> Self:
        """Calculates the sum for each element of an array instance with the respective element of the array `other`.

        Args:
            other: addend array. Must be compatible with `self` (see
            Broadcasting). Should have a numeric data type.

        Returns:
            Self: an array containing the element-wise sums. The returned array
            must have a data type determined by Type Promotion Rules.

        See Also:
            array_api_typing.Add

        """  # noqa: E501
        ...


class CanArraySub(Protocol):
    """Protocol for array classes that support the subtraction operator."""

    def __sub__(self, other: Self | int | float, /) -> Self:
        """Calculates the difference for each element of an array instance with the respective element of the array other.

        The result of `self_i - other_i` must be the same as `self_i +
        (-other_i)` and must be governed by the same floating-point rules as
        addition (see `CanArrayAdd`).

        Args:
            other: subtrahend array. Must be compatible with self (see
            Broadcasting). Should have a numeric data type.

        Returns:
            Self: an array containing the element-wise differences. The returned
            array must have a data type determined by Type Promotion Rules.

        See Also:
            array_api_typing.Subtract

        """  # noqa: E501
        ...


class CanArrayMul(Protocol):
    """Protocol for array classes that support the multiplication operator."""

    def __mul__(self, other: Self | int | float, /) -> Self:
        """Calculates the product for each element of an array instance with the respective element of the array `other`.

        Args:
            other: multiplicand array. Must be compatible with self (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: an array containing the element-wise products. The returned
            array must have a data type determined by Type Promotion Rules.

        See Also:
            array_api_typing.Multiply

        """  # noqa: E501
        ...


class Array(
    HasArrayNamespace[NS_co],
    CanArrayPos,
    CanArrayNeg,
    CanArrayAdd,
    CanArraySub,
    CanArrayMul,
    Protocol,
):
    """Array API specification for array object attributes and methods."""
