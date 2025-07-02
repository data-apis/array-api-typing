from typing import Any, TypeVar

import numpy.typing as npt

import array_api_typing as xpt

_T = TypeVar("_T", bound=npt.NDArray[Any])

def get_namespace(obj: xpt.HasArrayNamespace[_T], /) -> _T: ...

###
# Ensure that `np.ndarray` instances are assignable to `xpt.HasArrayNamespace`.

arr: npt.NDArray[Any]
arr_namespace: xpt.HasArrayNamespace[Any] = arr
