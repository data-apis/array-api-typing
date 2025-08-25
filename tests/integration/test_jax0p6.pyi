# mypy: disable-error-code="no-redef, explicit-any"

from types import ModuleType
from typing import Any, TypeAlias

import jax.numpy as jnp
from jax import Array

import array_api_typing as xpt

# DType aliases
F32: TypeAlias = jnp.float32
I32: TypeAlias = jnp.int32

# Define JAX Arrays against which we can test the protocols (JAX's Array type is
# not parametrized by dtype at type level.)
arr: Array
arr_i32: Array
arr_f32: Array
arr_b: Array

# =========================================================
# `xpt.HasArrayNamespace`

# Check assignment
_001: xpt.HasArrayNamespace[ModuleType] = arr
_002: xpt.HasArrayNamespace[ModuleType] = arr_i32
_003: xpt.HasArrayNamespace[ModuleType] = arr_f32
_004: xpt.HasArrayNamespace[ModuleType] = arr_b

# Check `__array_namespace__` method
a_ns: xpt.HasArrayNamespace[ModuleType] = arr
ns: ModuleType = a_ns.__array_namespace__()

# =========================================================
# `xpt.HasDType`

# Check DTypeT_co assignment
_005: xpt.HasDType[Any] = arr
_006: xpt.HasDType[jnp.dtype[I32]] = arr_i32
_007: xpt.HasDType[jnp.dtype[F32]] = arr_f32
_008: xpt.HasDType[jnp.dtype[jnp.bool_]] = arr_b

# =========================================================
# `xpt.Array`

# Check NamespaceT_co assignment
x_ns: xpt.Array[Any, ModuleType] = arr

# Check DTypeT_co assignment
_009: xpt.Array[Any] = arr
_010: xpt.Array[jnp.dtype[I32]] = arr_i32
_011: xpt.Array[jnp.dtype[F32]] = arr_f32
_012: xpt.Array[jnp.dtype[jnp.bool_]] = arr_b
