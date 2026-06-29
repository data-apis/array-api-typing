# mypy: disable-error-code="no-redef, explicit-any"

from types import ModuleType
from typing import Any, TypeAlias

import dask.array as da
import numpy as np

import array_api_typing as xpt

# DType aliases
F32: TypeAlias = np.float32
I32: TypeAlias = np.int32

# Define Dask Arrays against which we can test the protocols
# (Dask's Array type is not parametrized by dtype at type level.)
darr: da.Array
darr_i32: da.Array
darr_f32: da.Array
darr_b: da.Array

# =========================================================
# `xpt.HasArrayNamespace`

# Check assignment
_001: xpt.HasArrayNamespace[ModuleType] = darr
_002: xpt.HasArrayNamespace[ModuleType] = darr_i32
_003: xpt.HasArrayNamespace[ModuleType] = darr_f32
_004: xpt.HasArrayNamespace[ModuleType] = darr_b

# Check `__array_namespace__` method
a_ns: xpt.HasArrayNamespace[ModuleType] = darr
ns: ModuleType = a_ns.__array_namespace__()

# =========================================================
# `xpt.HasDType`

# Check DTypeT_co assignment
_005: xpt.HasDType[Any] = darr
_006: xpt.HasDType[np.dtype[I32]] = darr_i32
_007: xpt.HasDType[np.dtype[F32]] = darr_f32
_008: xpt.HasDType[np.dtype[np.bool_]] = darr_b

# =========================================================
# `xpt.Array`

# Check NamespaceT_co assignment
x_ns: xpt.Array[Any, ModuleType] = darr

# Check DTypeT_co assignment
_009: xpt.Array[Any] = darr
_010: xpt.Array[np.dtype[I32]] = darr_i32
_011: xpt.Array[np.dtype[F32]] = darr_f32
_012: xpt.Array[np.dtype[np.bool_]] = darr_b
