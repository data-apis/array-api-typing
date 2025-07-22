from typing import Any, Never, TypeAlias

import numpy as np
import numpy.typing as npt

import array_api_typing as xpt
from array_api_typing._array import BoolArray, NumericArray

F: TypeAlias = np.floating[Any]
F32: TypeAlias = np.float32
I: TypeAlias = np.integer[Any]
I32: TypeAlias = np.int32

# Define NDArrays against which we can test the protocols
nparr: npt.NDArray[Any]
nparr_i32: npt.NDArray[I32] = np.array([1], dtype=I32)
nparr_f32: npt.NDArray[F32] = np.array([1.0], dtype=F32)
nparr_b: npt.NDArray[np.bool_] = np.array([True], dtype=np.bool_)

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
arr_f: xpt.Array[F] = nparr_f32
arr_f32: xpt.Array[F32] = nparr_f32

# Integer Array types
arr_int: xpt.Array[int, xpt.Array[float | int]] = nparr_i32
arr_i: xpt.Array[I, xpt.Array[float | int]] = nparr_i32
arr_i32: xpt.Array[I32, xpt.Array[F32 | I32]] = nparr_i32

# Boolean Array types
arr_bool: xpt.Array[bool, xpt.Array[float | int | bool]] = nparr_b
arr_b: xpt.Array[np.bool_, xpt.Array[F | I | np.bool_]] = nparr_b

# =========================================================
# Check np.ndarray against BoolArray and NumericArray type aliases

boolarray: BoolArray = nparr_b
numericarray: NumericArray = nparr_f32
