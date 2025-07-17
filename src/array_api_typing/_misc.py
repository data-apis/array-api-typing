__all__ = ("DType",)

from typing import Protocol, type_check_only


@type_check_only
class DType(Protocol):
    """Protocol for classes that represent a data type.

    This `typing.Protocol` is `typing.type_check_only` and cannot be used at
    runtime.  This limitation is intentional since the array API structurally
    defines a ``dtype`` object as anything with an ``__eq__`` method that
    compares to another ``dtype`` object. This broad definition means that most
    Python objects will satisfy this protocol and can be erroneously considered
    a ``dtype``.

    """

    def __eq__(self, other: object, /) -> bool:
        """Computes the truth value of ``self == other`` in order to test for data type object equality."""  # noqa: E501
        ...
