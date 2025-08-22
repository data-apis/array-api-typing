"""Static typing support for the array API standard."""

__all__ = (  # noqa: RUF022
    # ==================
    # Array
    "Array",
    "HasArrayNamespace",
    "HasDType",
    "HasMatrixTranspose",
    "HasNDim",
    "HasShape",
    "HasSize",
    "HasTranspose",
    # ==================
    # Namespace
    "ArrayNamespace",
    "DoesAsType",
    "HasAsType",
    # ==================
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
from ._namespace import ArrayNamespace, DoesAsType, HasAsType
from ._version import version as __version__, version_tuple as __version_tuple__
