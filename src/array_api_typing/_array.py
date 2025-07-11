__all__ = (
    "Array",
    "BoolArray",
    "HasArrayNamespace",
    "NumericArray",
)

from types import ModuleType
from typing import Literal, Protocol, TypeAlias
from typing_extensions import TypeVar

import optype as op

from ._utils import docstring_setter

NS_co = TypeVar("NS_co", covariant=True, default=ModuleType)
InputT = TypeVar("InputT")


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


@docstring_setter(
    __pos__="""Evaluates `+self_i` for each element of an array instance.

    Returns:
        Self: An array containing the evaluated result for each element.
        The returned array must have the same data type as self.

    See Also:
        array_api_typing.Positive

    """,
    __neg__="""Evaluates `-self_i` for each element of an array instance.

    Returns:
        Self: an array containing the evaluated result for each element in
        self. The returned array must have a data type determined by Type
        Promotion Rules.

    See Also:
        array_api_typing.Negative

    """,
    __add__="""Calculates the sum for each element of an array instance with the respective element of the array `other`.

    Args:
        other: addend array. Must be compatible with `self` (see
        Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise sums. The returned array
        must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Add

    """,  # noqa: E501
    __iadd__="""Calculates the in-place sum for each element of an array instance with the respective element of the array `other`.

    Args:
        other: addend array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: `self`, after performing the in-place addition. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Add

    """,  # noqa: E501
    __radd__="""Calculates the sum for each element of the array `other` with the respective element of an array instance.

    Args:
        other: addend array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise sums. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Add

    """,  # noqa: E501
    __sub__="""Calculates the difference for each element of an array instance with the respective element of the array other.

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

    """,  # noqa: E501
    __isub__="""Calculates the in-place difference for each element of an array instance with the respective element of the array `other`.

    Args:
        other: subtrahend array. Must be compatible with `self` (see
            Broadcasting). Should have a numeric data type.

    Returns:
        Self: `self`, after performing the in-place subtraction. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Subtract

    """,  # noqa: E501
    __rsub__="""Calculates the difference for each element of the array `other` with the respective element of an array instance.

    The result of `other_i - self_i` must be the same as `other_i + (-self_i)`
    and must be governed by the same floating-point rules as addition (see
    `CanArrayAdd`).

    Args:
        other: minuend array. Must be compatible with `self` (see Broadcasting).
            Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise differences. The returned
            array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Subtract

    """,  # noqa: E501
    __mul__="""Calculates the product for each element of an array instance with the respective element of the array `other`.

    Args:
        other: multiplicand array. Must be compatible with self (see
            Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise products. The returned
        array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Multiply

    """,
    __imul__="""Calculates the in-place product for each element of an array instance with the respective element of the array `other`.

    Args:
        other: multiplicand array. Must be compatible with `self` (see
            Broadcasting). Should have a numeric data type.

    Returns:
        Self: `self`, after performing the in-place multiplication. The returned
            array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Multiply

    """,
    __rmul__="""Calculates the product for each element of the array `other` with the respective element of an array instance.

    Args:
        other: multiplicand array. Must be compatible with `self` (see
            Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise products. The returned array
            must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Multiply

    """,
    __truediv__="""Evaluates `self_i / other_i` for each element of an array instance with the respective element of the array `other`.

    Args:
        other: Must be compatible with `self` (see Broadcasting). Should have a
            numeric data type.

    Returns:
        Self: an array containing the element-wise results. The returned array
            should have a floating-point data type determined by Type Promotion
            Rules.

    See Also:
        array_api_typing.TrueDiv

    """,
    __itruediv__="""Calculates the in-place quotient for each element of an array instance with the respective element of the array `other`.

    Args:
        other: divisor array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: `self`, after performing the in-place true division. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.TrueDiv

    """,
    __rtruediv__="""Calculates the quotient for each element of the array `other` with the respective element of an array instance.

    Args:
        other: dividend array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise quotients. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.TrueDiv

    """,
    __floordiv__="""Evaluates `self_i // other_i` for each element of an array instance with the respective element of the array `other`.

    Args:
        other: Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise results. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.FloorDiv

    """,  # noqa: E501
    __ifloordiv__="""Calculates the in-place floor division for each element of an array instance with the respective element of the array `other`.

    Args:
        other: divisor array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: `self`, after performing the in-place floor division. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.FloorDiv

    """,  # noqa: E501
    __rfloordiv__="""Calculates the floor division for each element of the array `other` with the respective element of an array instance.

    Args:
        other: dividend array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise floor division results. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.FloorDiv

    """,  # noqa: E501
    __imod__="""Calculates the in-place remainder for each element of an array instance with the respective element of the array `other`.

    Args:
        other: divisor array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: `self`, after performing the in-place modulo operation. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Remainder

    """,  # noqa: E501
    __mod__=r"""Evaluates `self_i % other_i` for each element of an array instance with the respective element of the array `other`.

    Args:
        other: Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise results. Each element-wise result must have the same sign as the respective element `other_i`. The returned array must have a floating-point data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Remainder

    """,  # noqa: E501
    __rmod__="""Calculates the remainder for each element of the array `other` with the respective element of an array instance.

    Args:
        other: dividend array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise remainders. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Remainder

    """,  # noqa: E501
    __pow__="""Calculates an implementation-dependent approximation of exponentiation by raising each element (the base) of an array instance to the power of `other_i` (the exponent), where `other_i` is the corresponding element of the array `other`.

    Args:
        other: array whose elements correspond to the exponentiation exponent. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise results. The returned array must have a data type determined by Type Promotion Rules.

    """,  # noqa: E501
    __ipow__="""Calculates the in-place power for each element of an array instance with the respective element of the array `other`.

    Args:
        other: exponent array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: `self`, after performing the in-place power operation. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Power

    """,  # noqa: E501
    __rpow__="""Calculates the power for each element of the array `other` raised to the respective element of an array instance.

    Args:
        other: base array. Must be compatible with `self` (see Broadcasting). Should have a numeric data type.

    Returns:
        Self: an array containing the element-wise powers. The returned array must have a data type determined by Type Promotion Rules.

    See Also:
        array_api_typing.Power

    """,  # noqa: E501
)
class Array(
    HasArrayNamespace[NS_co],
    op.CanPosSelf,
    op.CanNegSelf,
    op.CanAddSelf[InputT],
    op.CanIAddSelf[InputT],
    op.CanRAddSelf[InputT],
    op.CanSubSelf[InputT],
    op.CanISubSelf[InputT],
    op.CanRSubSelf[InputT],
    op.CanMulSelf[InputT],
    op.CanIMulSelf[InputT],
    op.CanRMulSelf[InputT],
    op.CanTrueDivSelf[InputT],
    op.CanRTrueDivSelf[InputT],
    op.CanFloorDivSelf[InputT],
    op.CanIFloorDivSelf[InputT],
    op.CanRFloorDivSelf[InputT],
    op.CanModSelf[InputT],
    op.CanIModSelf[InputT],
    op.CanRModSelf[InputT],
    op.CanPowSelf[InputT],
    op.CanIPowSelf[InputT],
    op.CanRPowSelf[InputT],
    Protocol[InputT, NS_co],
):
    """Array API specification for array object attributes and methods."""


BoolArray: TypeAlias = Array[bool, NS_co]
"""Array API specification for boolean array object attributes and methods.

Specifically, this type alias fills the `InputT` type variable with `bool`,
allowing for `bool` objects to be added, subtracted, multiplied, etc. to the
array object.

"""

NumericArray: TypeAlias = Array[float | int, NS_co]
"""Array API specification for numeric array object attributes and methods.

Specifically, this type alias fills the `InputT` type variable with `float |
int`, allowing for `float | int` objects to be added, subtracted, multiplied,
etc. to the array object.

"""
