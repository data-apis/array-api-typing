# mypy: disable-error-code="no-redef"

from types import ModuleType
from typing import Any

import numpy.array_api as np  # type: ignore[import-not-found, unused-ignore]
from numpy import dtype

import array_api_typing as xpt

# Define NDArrays against which we can test the protocols
# Note that `np.array_api` doesn't support boolean arrays.
nparr = np.eye(2)
nparr_i32 = np.asarray([1], dtype=np.int32)
nparr_f32 = np.asarray([1.0], dtype=np.float32)

# =========================================================
# `xpt.HasArrayNamespace`

_: xpt.HasArrayNamespace[ModuleType] = nparr
_: xpt.HasArrayNamespace[ModuleType] = nparr_i32
_: xpt.HasArrayNamespace[ModuleType] = nparr_f32

# Check `__array_namespace__` method
a_ns: xpt.HasArrayNamespace[ModuleType] = nparr
ns: ModuleType = a_ns.__array_namespace__()

# Incorrect values are caught when using `__array_namespace__` and
# backpropagated to the type of `a_ns`
_: xpt.HasArrayNamespace[dict[str, int]] = nparr  # not caught

# =========================================================
# `xpt.HasDType`

# Note that `np.array_api` uses dtype objects, not dtype classes, so we can't
# type annotate specific dtypes like `np.float32` or `np.int32`.

_: xpt.HasDType[dtype[Any]] = nparr
_: xpt.HasDType[dtype[Any]] = nparr_i32
_: xpt.HasDType[dtype[Any]] = nparr_f32

# =========================================================
# `xpt.Array`

# Check NamespaceT_co assignment
a_ns: xpt.Array[Any, ModuleType] = nparr

# Check DTypeT_co assignment
# Note that `np.array_api` uses dtype objects, not dtype classes, so we can't
# type annotate specific dtypes like `np.float32` or `np.int32`.
_: xpt.Array[dtype[Any]] = nparr
x_f32: xpt.Array[dtype[Any]] = nparr_f32
x_i32: xpt.Array[dtype[Any]] = nparr_i32

# Check Attribute `.dtype`
_: dtype[Any] = x_f32.dtype
_: dtype[Any] = x_i32.dtype

# Check Attribute `.device`
_: object = x_f32.device
_: object = x_i32.device

# Check Attribute `.mT`
_: xpt.Array[dtype[Any]] = x_f32.mT
_: xpt.Array[dtype[Any]] = x_i32.mT

# Check Attribute `.ndim`
_: int = x_f32.ndim
_: int = x_i32.ndim

# Check Attribute `.shape`
_: tuple[int | None, ...] = x_f32.shape
_: tuple[int | None, ...] = x_i32.shape

# Check Attribute `.size`
_: int | None = x_f32.size
_: int | None = x_i32.size
