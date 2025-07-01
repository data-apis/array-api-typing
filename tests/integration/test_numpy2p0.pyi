# mypy: disable-error-code="no-redef"

from types import ModuleType
from typing import Any, TypeAlias, assert_type

import numpy as np
import numpy.typing as npt

import array_api_typing as xpt

# DType aliases
F32: TypeAlias = np.float32
I32: TypeAlias = np.int32
B: TypeAlias = np.bool_

# Define NDArrays against which we can test the protocols
nparr: npt.NDArray[Any]
nparr_i32: npt.NDArray[I32]
nparr_f32: npt.NDArray[F32]
nparr_b: npt.NDArray[B]

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
# `xpt.HasDType`

# Check DTypeT_co assignment
_: xpt.HasDType[Any] = nparr
_: xpt.HasDType[np.dtype[I32]] = nparr_i32
_: xpt.HasDType[np.dtype[F32]] = nparr_f32
_: xpt.HasDType[np.dtype[B]] = nparr_b

# =========================================================
# `xpt.Array`

# Check NamespaceT_co assignment
a_ns: xpt.Array[Any, ModuleType] = nparr

# Check DTypeT_co assignment
_: xpt.Array[Any] = nparr
x_f32: xpt.Array[np.dtype[F32]] = nparr_f32
x_i32: xpt.Array[np.dtype[I32]] = nparr_i32
x_b: xpt.Array[np.dtype[B]] = nparr_b

# Check Attribute `.dtype`
assert_type(x_f32.dtype, np.dtype[F32])
assert_type(x_i32.dtype, np.dtype[I32])
assert_type(x_b.dtype, np.dtype[B])

# Check Attribute `.device`
assert_type(x_f32.device, object)
assert_type(x_i32.device, object)
assert_type(x_b.device, object)

# Check Attribute `.mT`
assert_type(x_f32.mT, xpt.Array[np.dtype[F32]])
assert_type(x_i32.mT, xpt.Array[np.dtype[I32]])
assert_type(x_b.mT, xpt.Array[np.dtype[B]])

# Check Attribute `.ndim`
assert_type(x_f32.ndim, int)
assert_type(x_i32.ndim, int)
assert_type(x_b.ndim, int)

# Check Attribute `.shape`
assert_type(x_f32.shape, tuple[int | None, ...])
assert_type(x_i32.shape, tuple[int | None, ...])
assert_type(x_b.shape, tuple[int | None, ...])

# Check Attribute `.size`
assert_type(x_f32.size, int | None)
assert_type(x_i32.size, int | None)
assert_type(x_b.size, int | None)
