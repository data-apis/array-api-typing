"""Static typing support for the array API standard."""

__all__ = [
    "Array",
    "DType",
    "Device",
    "HasArrayNamespace",
    "Namespace",
    "__version__",
    "__version_tuple__",
]

from ._array import Array
from ._device import Device
from ._dtype import DType
from ._namespace import HasArrayNamespace, Namespace
from ._version import version as __version__, version_tuple as __version_tuple__
