"""Static typing support for the array API standard."""

__all__ = [
    "Array",
    "ArrayNamespace",
    "DType",
    "Device",
    "HasArrayNamespace",
    "__version__",
    "__version_tuple__",
]

from ._array import Array
from ._device import Device
from ._dtype import DType
from ._namespace import ArrayNamespace, HasArrayNamespace
from ._version import version as __version__, version_tuple as __version_tuple__
