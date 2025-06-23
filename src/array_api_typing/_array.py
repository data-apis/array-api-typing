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


class CanArrayIAdd(Protocol):
    """Protocol for array classes that support the in-place addition operator."""

    def __iadd__(self, other: Self | int | float, /) -> Self:
        """Calculates the in-place sum for each element of an array instance with the respective element of the array `other`.

        Args:
            other: addend array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: `self`, after performing the in-place addition. The returned array must have a data type determined by Type Promotion Rules.

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


class CanArrayISub(Protocol):
    """Protocol for array classes that support the in-place subtraction operator."""

    def __isub__(self, other: Self | int | float, /) -> Self:
        """Calculates the in-place difference for each element of an array instance with the respective element of the array `other`.

        Args:
            other: subtrahend array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: `self`, after performing the in-place subtraction. The returned array must have a data type determined by Type Promotion Rules.

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


class CanArrayIMul(Protocol):
    """Protocol for array classes that support the in-place multiplication operator."""

    def __imul__(self, other: Self | int | float, /) -> Self:
        """Calculates the in-place product for each element of an array instance with the respective element of the array `other`.

        Args:
            other: multiplicand array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: `self`, after performing the in-place multiplication. The returned array must have a data type determined by Type Promotion Rules.

        See Also:
            array_api_typing.Multiply

        """  # noqa: E501
        ...


class CanArrayTrueDiv(Protocol):
    """Protocol for array classes that support the true division operator."""

    def __truediv__(self, other: Self | int | float, /) -> Self:
        """Evaluates `self_i / other_i` for each element of an array instance with the respective element of the array `other`.

        Args:
            other: Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: an array containing the element-wise results. The returned array should have a floating-point data type determined by Type Promotion Rules.

        See Also:
            array_api_typing.TrueDiv

        """  # noqa: E501
        ...


class CanArrayITruediv(Protocol):
    """Protocol for array classes that support the in-place true division operator."""

    def __itruediv__(self, other: Self | int | float, /) -> Self:
        """Calculates the in-place quotient for each element of an array instance with the respective element of the array `other`.

        Args:
            other: divisor array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: `self`, after performing the in-place true division. The returned array must have a data type determined by Type Promotion Rules.

        See Also:
            array_api_typing.TrueDiv

        """  # noqa: E501
        ...


class CanArrayFloorDiv(Protocol):
    """Protocol for array classes that support the floor division operator."""

    def __floordiv__(self, other: Self | int | float, /) -> Self:
        """Evaluates `self_i // other_i` for each element of an array instance with the respective element of the array `other`.

        Args:
            other: Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: an array containing the element-wise results. The returned array must have a data type determined by Type Promotion Rules.

        See Also:
            array_api_typing.FloorDiv

        """  # noqa: E501
        ...


class CanArrayIFloorDiv(Protocol):
    """Protocol for array classes that support the in-place floor division operator."""

    def __ifloordiv__(self, other: Self | int | float, /) -> Self:
        """Calculates the in-place floor division for each element of an array instance with the respective element of the array `other`.

        Args:
            other: divisor array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: `self`, after performing the in-place floor division. The returned array must have a data type determined by Type Promotion Rules.

        See Also:
            array_api_typing.FloorDiv

        """  # noqa: E501
        ...


class CanArrayMod(Protocol):
    """Protocol for array classes that support the modulo operator."""

    def __mod__(self, other: Self | int | float, /) -> Self:
        """Evaluates `self_i % other_i` for each element of an array instance with the respective element of the array `other`.

        Args:
            other: Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: an array containing the element-wise results. Each element-wise result must have the same sign as the respective element `other_i`. The returned array must have a floating-point data type determined by Type Promotion Rules.

        See Also:
            array_api_typing.Remainder

        """  # noqa: E501
        ...


class CanArrayPow(Protocol):
    """Protocol for array classes that support the power operator."""

    def __pow__(self, other: Self | int | float, /) -> Self:
        """Calculates an implementation-dependent approximation of exponentiation by raising each element (the base) of an array instance to the power of `other_i` (the exponent), where `other_i` is the corresponding element of the array `other`.

        Args:
            other: array whose elements correspond to the exponentiation exponent. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: an array containing the element-wise results. The returned array must have a data type determined by Type Promotion Rules.

        """  # noqa: E501
        ...


class CanArrayIPow(Protocol):
    """Protocol for array classes that support the in-place power operator."""

    def __ipow__(self, other: Self | int | float, /) -> Self:
        """Calculates the in-place power for each element of an array instance with the respective element of the array `other`.

        Args:
            other: exponent array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

        Returns:
            Self: `self`, after performing the in-place power operation. The returned array must have a data type determined by Type Promotion Rules.

        See Also:
            array_api_typing.Power

        """  # noqa: E501
        ...


class Array(
    HasArrayNamespace[NS_co],
    CanArrayPos,
    CanArrayNeg,
    CanArrayAdd,
    CanArrayIAdd,
    CanArraySub,
    CanArrayISub,
    CanArrayMul,
    CanArrayIMul,
    CanArrayTrueDiv,
    CanArrayFloorDiv,
    CanArrayIFloorDiv,
    CanArrayMod,
    CanArrayPow,
    CanArrayIPow,
    Protocol,
):
    """Array API specification for array object attributes and methods."""
