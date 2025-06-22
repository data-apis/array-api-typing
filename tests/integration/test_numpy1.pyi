# Test array_api_typing with numpy < 2.0
#
# NOTES:
# - `np.array_api` uses dtype objects instead of dtype classes, preventing the
#   use of `np.float32` and `np.int32` as type aliases in type annotations.
# - `bool` doesn't seem to be a valid dtype in `np.array_api`. The valid dtypes
#   are signedinteger of 8, 16, 32, and 64 bits, unsignedinteger of 8, 16, 32,
#   and 64 bits, and floating of 32 and 64 bits and None.

from typing import Any, Never

import numpy.array_api as np  # type: ignore[import-not-found, unused-ignore]

import array_api_typing as xpt
from array_api_typing._array import NumericArray

# Define an NDArray against which we can test the protocols
nparr = np.eye(2)
nparr_i32 = np.asarray([1], dtype=np.int32)
nparr_f32 = np.asarray([1.0], dtype=np.float32)

# =========================================================
# Ensure that `np.ndarray` instances are assignable to `xpt.HasArrayNamespace`

arr_ns: xpt.HasArrayNamespace[Any] = nparr
arr_ns_i32: xpt.HasArrayNamespace[Any] = nparr_i32
arr_ns_f32: xpt.HasArrayNamespace[Any] = nparr_f32

# =========================================================
# Ensure that `np.ndarray` instances are assignable to `xpt.Array`.

# Generic Array type
arr_array: xpt.Array[Never] = nparr

# Float Array types
arr_float: xpt.Array[float] = nparr_f32

# Integer Array types
arr_int: xpt.Array[int, xpt.Array[float | int]] = nparr_i32
arr_i: xpt.Array[int | float, xpt.Array[float | int]] = nparr_i32

# =========================================================
# Check np.ndarray against BoolArray and NumericArray type aliases

numericarray: NumericArray = nparr_f32
