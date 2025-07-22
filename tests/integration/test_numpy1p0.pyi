# mypy: disable-error-code="no-redef"

from types import ModuleType
from typing import TypeAlias

import numpy.array_api as np  # type: ignore[import-not-found, unused-ignore]

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
