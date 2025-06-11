"""Static typing support for the array API standard."""

from typing import Protocol, final


@final
class Array(HasArrayNamespace, Protocol):
    pass
