from typing import Any

# requires numpy < 2
import numpy.array_api as np

import array_api_typing as xpt

###
# Ensure that `np.ndarray` instances are assignable to `xpt.HasArrayNamespace`.

arr = np.eye(2)
arr_namespace: xpt.HasArrayNamespace[Any] = arr
