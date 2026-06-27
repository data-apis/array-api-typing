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
_001: xpt.HasArrayNamespace[ModuleType] = nparr
_002: xpt.HasArrayNamespace[ModuleType] = nparr_i32
_003: xpt.HasArrayNamespace[ModuleType] = nparr_f32
_004: xpt.HasArrayNamespace[ModuleType] = nparr_b

# Check `__array_namespace__` method
a_ns: xpt.HasArrayNamespace[ModuleType] = nparr
ns: ModuleType = a_ns.__array_namespace__()

# =========================================================
# `xpt.HasDType`

# Check DTypeT_co assignment
_005: xpt.HasDType[Any] = nparr
_006: xpt.HasDType[np.dtype[I32]] = nparr_i32
_007: xpt.HasDType[np.dtype[F32]] = nparr_f32
_008: xpt.HasDType[np.dtype[np.bool_]] = nparr_b

# =========================================================
# `xpt.Array`

# Check NamespaceT_co assignment
x_ns: xpt.Array[Any, ModuleType] = nparr

# Check DTypeT_co assignment
_009: xpt.Array[Any] = nparr
_010: xpt.Array[np.dtype[I32]] = nparr_i32
_011: xpt.Array[np.dtype[F32]] = nparr_f32
_012: xpt.Array[np.dtype[np.bool_]] = nparr_b
