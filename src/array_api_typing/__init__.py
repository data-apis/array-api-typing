"""Static typing support for the array API standard."""

__all__ = (
    "Array",
    "HasArrayNamespace",
    "HasDType",
    "HasMatrixTranspose",
    "HasNDim",
    "HasShape",
    "HasSize",
    "HasTranspose",
    "__version__",
    "__version_tuple__",
)

from ._array import (
    Array,
    HasArrayNamespace,
    HasDType,
    HasMatrixTranspose,
    HasNDim,
    HasShape,
    HasSize,
    HasTranspose,
)
from ._version import version as __version__, version_tuple as __version_tuple__
