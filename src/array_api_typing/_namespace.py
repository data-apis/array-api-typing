from typing import Protocol, TypeVar

from ._array import HasDType

__all__ = (
    "ArrayNamespace",
    # Data Type Functions
    "DoesAsType",
    "HasAsType",
)

DTypeT = TypeVar("DTypeT")
ToDTypeT = TypeVar("ToDTypeT")

# ===================================================================
# Creation Functions
# TODO: arange, asarray, empty, empty_like, eye, from_dlpack, full, full_like,
# linspace, meshgrid, ones, ones_like, tril, triu, zeros, zeros_like

# ===================================================================
# Data Type Functions
# TODO: broadcast_arrays, broadcast_to, can_cast, finfo, iinfo,
# result_type


class DoesAsType(Protocol):
    """Copies an array to a specified data type irrespective of Type Promotion Rules rules.

    Note:
        Casting floating-point ``NaN`` and ``infinity`` values to integral data
        types is not specified and is implementation-dependent.

    Note:
        When casting a boolean input array to a numeric data type, a value of
        `True` must cast to a numeric value equal to ``1``, and a value of
        `False` must cast to a numeric value equal to ``0``.

        When casting a numeric input array to bool, a value of ``0`` must cast
        to `False`, and a non-zero value must cast to `True`.

    Args:
        x: The array to cast.
        dtype: desired data type.
        copy: specifies whether to copy an array when the specified `dtype`
            matches the data type of the input array `x`. If `True`, a newly
            allocated array must always be returned. If `False` and the
            specified `dtype` matches the data type of the input array, the
            input array must be returned; otherwise, a newly allocated must be
            returned. Default: `True`.

    """  # noqa: E501

    def __call__(
        self, x: HasDType[DTypeT], dtype: ToDTypeT, /, *, copy: bool = True
    ) -> HasDType[ToDTypeT]: ...


class HasAsType(Protocol):
    """Protocol for namespaces that have an ``astype`` function."""

    astype: DoesAsType


# ===================================================================
# Element-wise Functions
# TODO: abs, acos, acosh, add, asin, asinh, atan, atan2, atanh, bitwise_and,
# bitwise_invert, bitwise_left_shift, bitwise_or, bitwise_right_shift,
# bitwise_xor, ceil, cos, cosh, divide, equal, exp, exp2, expm1, floor,
# floor_divide, greater, greater_equal, isfinite, isinf, isnan, less,
# less_equal, log, log1p, log2, log10, logical_and, logical_not, logical_or,
# logical_xor, multiply, negative, not_equal, positive, pow, remainder, round,
# sign, sin, sinh, square, sqrt, subtract, tan, tanh, trunc


# ===================================================================
# Linear Algebra Functions
# TODO: matmul, matrix_transpose, tensordot, vecdot

# ===================================================================
# Manipulation Functions
# TODO: concat, expand_dims, flip, permute_dims, reshape, roll, squeeze, stack

# ===================================================================
# Searching Functions
# TODO: argmax, argmin, nonzero, where

# ===================================================================
# Set Functions
# TODO: unique_all, unique_counts, unique_inverse, unique_values

# ===================================================================
# Sorting Functions
# TODO: argsort, sort

# ===================================================================
# Statistical Functions
# TODO: max, mean, min, prod, std, sum, var

# ===================================================================
# Utility Functions
# TODO: all, any

# ===================================================================
# Full Namespace


class ArrayNamespace(
    # Data Type Functions
    HasAsType,
    Protocol,
):
    """Protocol for an Array API-compatible namespace."""
