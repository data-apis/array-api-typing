"""Static typing support for array API arrays."""

from typing import Protocol

from ._namespace import HasArrayNamespace


class Array(HasArrayNamespace, Protocol):
    """An Array API array of homogenously-typed numbers."""

    # TODO(https://github.com/data-apis/array-api-typing/issues/23): Populate this
    # protocol with methods defined by the Array API specification.
