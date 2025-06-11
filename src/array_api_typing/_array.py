"""Static typing support for the array API standard."""

from typing import Protocol

from ._namespace import HasArrayNamespace


class Array(HasArrayNamespace, Protocol):
    pass
