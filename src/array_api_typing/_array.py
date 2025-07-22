__all__ = (
    "Array",
    "BoolArray",
    "HasArrayNamespace",
    "NumericArray",
)

from pathlib import Path
from types import ModuleType
from typing import Literal, Never, Protocol, TypeAlias
from typing_extensions import TypeVar

import optype as op

from ._utils import docstring_setter

# Load docstrings from TOML file
try:
    import tomllib
except ImportError:
    import tomli as tomllib  # type: ignore[import-not-found, no-redef]

_docstrings_path = Path(__file__).parent / "_array_docstrings.toml"
with _docstrings_path.open("rb") as f:
    _array_docstrings = tomllib.load(f)["docstrings"]

NS_co = TypeVar("NS_co", covariant=True, default=ModuleType)
T_contra = TypeVar("T_contra", contravariant=True)
R_co = TypeVar("R_co", covariant=True, default=Never)


class HasArrayNamespace(Protocol[NS_co]):
    """Protocol for classes that have an `__array_namespace__` method.

    Example:
    >>> import array_api_typing as xpt
    >>>
    >>> class MyArray:
    ...     def __array_namespace__(self):
    ...         return object()
    >>>
    >>> x = MyArray()
    >>> def has_array_namespace(x: xpt.HasArrayNamespace) -> bool:
    ...     return hasattr(x, "__array_namespace__")
    >>> has_array_namespace(x)
    True

    """

    def __array_namespace__(
        self, /, *, api_version: Literal["2021.12"] | None = None
    ) -> NS_co: ...


@docstring_setter(**_array_docstrings)
class Array(
    HasArrayNamespace[NS_co],
    op.CanPosSelf,
    op.CanNegSelf,
    op.CanAddSame[T_contra, R_co],
    op.CanSubSame[T_contra, R_co],
    op.CanMulSame[T_contra, R_co],
    op.CanTruedivSame[T_contra, R_co],
    op.CanFloordivSame[T_contra, R_co],
    op.CanModSame[T_contra, R_co],
    op.CanPowSame[T_contra, R_co],
    Protocol[T_contra, R_co, NS_co],
):
    """Array API specification for array object attributes and methods."""


BoolArray: TypeAlias = Array[bool, Array[float, Never, NS_co], NS_co]
"""Array API specification for boolean array object attributes and methods.

Specifically, this type alias fills the `T_contra` type variable with
`bool`, allowing for `bool` objects to be added, subtracted, multiplied, etc. to
the array object.

"""

NumericArray: TypeAlias = Array[float | int, NS_co]
"""Array API specification for numeric array object attributes and methods.

Specifically, this type alias fills the `T_contra` type variable with `float
| int`, allowing for `float | int` objects to be added, subtracted, multiplied,
etc. to the array object.

"""
