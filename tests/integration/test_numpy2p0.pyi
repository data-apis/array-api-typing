# mypy: disable-error-code="no-redef"

from types import ModuleType
from typing import Any, TypeAlias

import numpy as np
import numpy.typing as npt

import array_api_typing as xpt

# DType aliases
F32: TypeAlias = np.float32
I32: TypeAlias = np.int32

# Define NDArrays against which we can test the protocols
nparr: npt.NDArray[Any]
nparr_i32: npt.NDArray[I32]
nparr_f32: npt.NDArray[F32]
nparr_b: npt.NDArray[np.bool_]

# =========================================================
# `xpt.HasArrayNamespace`

# Check assignment
_: xpt.HasArrayNamespace[ModuleType] = nparr
_: xpt.HasArrayNamespace[ModuleType] = nparr_i32
_: xpt.HasArrayNamespace[ModuleType] = nparr_f32
_: xpt.HasArrayNamespace[ModuleType] = nparr_b

# Check `__array_namespace__` method
a_ns: xpt.HasArrayNamespace[ModuleType] = nparr
ns: ModuleType = a_ns.__array_namespace__()

# Incorrect values are caught when using `__array_namespace__` and
# backpropagated to the type of `a_ns`
_: xpt.HasArrayNamespace[dict[str, int]] = nparr  # not caught

# =========================================================
# `xpt.Array`

# Check NamespaceT_co assignment
a_ns: xpt.Array[ModuleType] = nparr
