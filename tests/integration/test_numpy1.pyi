from typing import Any

import numpy.array_api as np

import array_api_typing as xpt

###
# Ensure that `np.ndarray` instances are assignable to `xpt.HasArrayNamespace`.

arr: np.Array
arr_namespace: xpt.HasArrayNamespace[Any] = arr
