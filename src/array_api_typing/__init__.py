"""Static typing support for the array API standard."""

__all__ = (
    "Array",
    "ArrayNamespace",
    "DType",
    "Device",
    "HasArrayNamespace",
    "__version__",
    "__version_tuple__",
    "signature_types",
)

from . import signature_types
from ._array import Array
from ._misc_objects import Device, DType
from ._namespace import ArrayNamespace, HasArrayNamespace
from ._version import version as __version__, version_tuple as __version_tuple__
