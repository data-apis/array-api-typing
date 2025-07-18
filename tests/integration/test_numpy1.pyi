from typing import Any, Never

# requires numpy < 2
import numpy.array_api as np

import array_api_typing as xpt

# Define an NDArray against which we can test the protocols
arr = np.eye(2)

###
# Ensure that `np.ndarray` instances are assignable to `xpt.HasArrayNamespace`.

arr_namespace: xpt.HasArrayNamespace[Any] = arr

###
# Ensure that `np.ndarray` instances are assignable to `xpt.Array`.

arr_array: xpt.Array[Never, Any] = arr
arr_floatarray: xpt.Array[float, Any] = arr
arr_boolarray: xpt.Array[bool, Any] = arr
