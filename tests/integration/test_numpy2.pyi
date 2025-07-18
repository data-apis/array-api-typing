from typing import Any, Never

import numpy as np
import numpy.typing as npt

import array_api_typing as xpt

# Define NDArrays against which we can test the protocols
nparr: npt.NDArray[Any]
nparr_i32: npt.NDArray[np.int32] = np.array([1], dtype=np.int32)
nparr_f32: npt.NDArray[np.float32] = np.array([1.0], dtype=np.float32)

###
# Ensure that `np.ndarray` instances are assignable to `xpt.HasArrayNamespace`.

arr_ns: xpt.HasArrayNamespace[Any] = nparr
arr_ns_i32: xpt.HasArrayNamespace[Any] = nparr_i32
arr_ns_f32: xpt.HasArrayNamespace[Any] = nparr_f32

###
# Ensure that `np.ndarray` instances are assignable to `xpt.Array`.

arr_array: xpt.Array[Never, Any] = nparr
arr_floatarray: xpt.Array[float, Any] = nparr
arr_boolarray: xpt.Array[bool, Any] = nparr

# Test correct type assignments with actual array instances
arr_i32: xpt.Array[np.int32, Any] = nparr_i32  # type: ignore[assignment]  # FIXME
arr_f32: xpt.Array[np.float32, Any] = nparr_f32
