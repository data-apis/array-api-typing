"""Static typing support for the array API standard."""

from typing import Protocol, final


@final
class DType(Protocol):
    pass
