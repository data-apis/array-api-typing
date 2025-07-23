"""Static typing support for the array API standard."""

__all__ = (
    "Array",
    "HasArrayNamespace",
    "HasDType",
    "HasMatrixTranspose",
    "HasNDim",
    "__version__",
    "__version_tuple__",
)

from ._array import (
    Array,
    HasArrayNamespace,
    HasDType,
    HasMatrixTranspose,
    HasNDim,
)
from ._version import version as __version__, version_tuple as __version_tuple__
