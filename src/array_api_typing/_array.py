__all__ = (
    "Array",
    "HasArrayNamespace",
    "HasDType",
    "HasDevice",
    "HasMatrixTranspose",
    "HasNDim",
    "HasShape",
    "HasSize",
    "HasTranspose",
)

from types import ModuleType
from typing import Literal, Protocol, Self
from typing_extensions import TypeVar

NamespaceT_co = TypeVar("NamespaceT_co", covariant=True, default=ModuleType)
DTypeT_co = TypeVar("DTypeT_co", covariant=True)
DeviceT_co = TypeVar("DeviceT_co", covariant=True, default=object)


class HasArrayNamespace(Protocol[NamespaceT_co]):
    """Protocol for classes that have an `__array_namespace__` method.

    This `Protocol` is intended for use in static typing to ensure that an
    object has an `__array_namespace__` method that returns a namespace for
    array operations. This `Protocol` should not be used at runtime for type
    checking or as a base class.

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
    ) -> NamespaceT_co:
        """Returns an object that has all the array API functions on it.

        Args:
            api_version: string representing the version of the array API
                specification to be returned, in 'YYYY.MM' form, for example,
                '2020.10'. If it is `None`, it should return the namespace
                corresponding to latest version of the array API specification.
                If the given version is invalid or not implemented for the given
                module, an error should be raised. Default: `None`.

        Returns:
            NamespaceT_co: An object representing the array API namespace. It
                should have every top-level function defined in the
                specification as an attribute. It may contain other public names
                as well, but it is recommended to only include those names that
                are part of the specification.

        """
        ...


class HasDType(Protocol[DTypeT_co]):
    """Protocol for array classes that have a data type attribute."""

    @property
    def dtype(self, /) -> DTypeT_co:
        """Data type of the array elements."""
        ...


class HasDevice(Protocol[DeviceT_co]):
    """Protocol for array classes that have a device attribute."""

    @property
    def device(self) -> DeviceT_co:
        """Hardware device the array data resides on."""
        ...


class HasMatrixTranspose(Protocol):
    """Protocol for array classes that have a matrix transpose attribute."""

    @property
    def mT(self) -> Self:  # noqa: N802
        """Transpose of a matrix (or a stack of matrices).

        If an array instance has fewer than two dimensions, an error should be
        raised.

        Returns:
            Self: array whose last two dimensions (axes) are permuted in reverse
                order relative to original array (i.e., for an array instance
                having shape `(..., M, N)`, the returned array must have shape
                `(..., N, M))`.  The returned array must have the same data type
                as the original array.

        """
        ...


class HasNDim(Protocol):
    """Protocol for array classes that have a number of dimensions attribute."""

    @property
    def ndim(self) -> int:
        """Number of array dimensions (axes).

        Returns:
            int: number of array dimensions (axes).

        """
        ...


class HasShape(Protocol):
    """Protocol for array classes that have a shape attribute."""

    @property
    def shape(self) -> tuple[int | None, ...]:
        """Shape of the array.

        Returns:
            tuple[int | None, ...]: array dimensions. An array dimension must be None
                if and only if a dimension is unknown.

        Notes:
            For array libraries having graph-based computational models, array
            dimensions may be unknown due to data-dependent operations (e.g.,
            boolean indexing; `A[:, B > 0]`) and thus cannot be statically
            resolved without knowing array contents.

        """
        ...


class HasSize(Protocol):
    """Protocol for array classes that have a size attribute."""

    @property
    def size(self) -> int | None:
        """Number of elements in an array.

        Returns:
            int | None: number of elements in an array. The returned value must
                be `None` if and only if one or more array dimensions are
                unknown.

        Notes:
            This must equal the product of the array's dimensions.

        """
        ...


class HasTranspose(Protocol):
    """Protocol for array classes that support the transpose operation."""

    @property
    def T(self) -> Self:  # noqa: N802
        """Transpose of the array.

        The array instance must be two-dimensional. If the array instance is not
        two-dimensional, an error should be raised.

        Returns:
            Self: two-dimensional array whose first and last dimensions (axes)
                are permuted in reverse order relative to original array. The
                returned array must have the same data type as the original
                array.

        Notes:
            Limiting the transpose to two-dimensional arrays (matrices) deviates
            from the NumPy et al practice of reversing all axes for arrays
            having more than two-dimensions. This is intentional, as reversing
            all axes was found to be problematic (e.g., conflicting with the
            mathematical definition of a transpose which is limited to matrices;
            not operating on batches of matrices; et cetera). In order to
            reverse all axes, one is recommended to use the functional
            `PermuteDims` interface found in this specification.

        """
        ...


class Array(
    # ------ Attributes -------
    HasDType[DTypeT_co],
    # ------- Methods ---------
    HasArrayNamespace[NamespaceT_co],
    # -------------------------
    Protocol[DTypeT_co, NamespaceT_co],
):
    """Array API specification for array object attributes and methods.

    The type is: ``Array[+DTypeT, +NamespaceT = ModuleType] = Array[DTypeT,
    NamespaceT]`` where:

    - `DTypeT` is the data type of the array elements.
    - `NamespaceT` is the type of the array namespace. It defaults to
      `ModuleType`, which is the most common form of array namespace (e.g.,
      `numpy`, `cupy`, etc.). However, it can be any type, e.g. a
      `types.SimpleNamespace`, to allow for wrapper libraries to
      semi-dynamically define their own array namespaces based on the wrapped
      array type.

    This type is intended for use in static typing to ensure that an object has
    the attributes and methods defined in the array API specification. It should
    not be used at runtime for type checking or as a base class.

    """
