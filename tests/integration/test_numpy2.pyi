from typing import Any

import numpy.typing as npt

import array_api_typing as xpt

###
# Ensure that `np.ndarray` instances are assignable to `xpt.HasArrayNamespace`.

arr: npt.NDArray[Any]
arr_namespace: xpt.HasArrayNamespace[Any] = arr
