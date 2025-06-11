"""Static typing support for the array API standard."""

from __future__ import annotations

from typing import Any, Protocol, TypeAlias, TypeVar

_T_co = TypeVar("_T_co", covariant=True)


class NestedSequence(Protocol[_T_co]):
    def __getitem__(self, key: int, /) -> _T_co | NestedSequence[_T_co]: ...
    def __len__(self, /) -> int: ...


SupportsBufferProtocol: TypeAlias = Any
