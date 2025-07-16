from typing import Any

import numpy.typing as npt

import array_api_typing as xpt

# Define an NDArray against which we can test the protocols
arr: npt.NDArray[Any]

###
# Ensure that `np.ndarray` instances are assignable to `xpt.HasArrayNamespace`.

arr_namespace: xpt.HasArrayNamespace[Any] = arr

###
# Ensure that `np.ndarray` instances are assignable to `xpt.Array`.

arr_array: xpt.Array[Any, Any] = arr
arr_floatarray: xpt.Array[float, Any] = arr
arr_boolarray: xpt.Array[bool, Any] = arr
