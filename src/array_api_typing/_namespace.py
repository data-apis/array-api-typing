from typing import Protocol

__all__ = ("ArrayNamespace",)

# ===================================================================
# Creation Functions
# TODO: arange, asarray, empty, empty_like, eye, from_dlpack, full, full_like,
# linspace, meshgrid, ones, ones_like, tril, triu, zeros, zeros_like

# ===================================================================
# Data Type Functions
# TODO: astype, broadcast_arrays, broadcast_to, can_cast, finfo, iinfo,
# result_type

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


class ArrayNamespace(Protocol):
    """Protocol for an Array API-compatible namespace."""
