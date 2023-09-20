import os
import sys
from collections.abc import Generator, Sequence
from typing import Any, Generic, TypeVar, overload

import numpy.typing as npt

if sys.version_info >= (3, 8):
    from typing import Literal as L
else:
    from typing_extensions import Literal as L

_T = TypeVar("_T")
_PT = TypeVar("_PT", str, bytes, os.PathLike[str], os.PathLike[bytes])
_ST = TypeVar("_ST", bound=str)

class KFReader(Generic[_PT]):
    endian: L["<", ">"]
    word: L["i", "q"]
    path: _PT
    def __init__(self, path: _PT, blocksize: int = ..., autodetect: bool = ...) -> None: ...
    def read(self, section: str, variable: str) -> Any: ...
    def __iter__(self) -> Generator[tuple[str, str], None, None]: ...

class KFFile:
    autosave: bool
    path: str
    tmpdata: dict[str, dict[str, Any]]
    reader: None | KFReader[str]
    def __init__(self, path: str | os.PathLike[str], autosave: bool = ...) -> None: ...
    @overload
    def read(self, section: str, variable: str, return_as_list: L[False] = ...) -> Any: ...
    @overload
    def read(self, section: str, variable: str, return_as_list: L[True]) -> list[Any]: ...
    def write(
        self, section: str, variable: str, value: bool | int | float | str | Sequence[bool | int | float | str]
    ) -> None: ...
    def save(self) -> None: ...
    def delete_section(self, section: str) -> None: ...
    def sections(self) -> list[str]: ...
    def read_section(self, section: str) -> dict[str, Any]: ...
    def get_skeleton(self) -> dict[str, set[str]]: ...
    def __getitem__(self, name: str | tuple[str, str]) -> Any: ...
    def __setitem__(
        self, name: str | tuple[str, str], value: bool | int | float | str | Sequence[bool | int | float | str]
    ) -> None: ...
    def __iter__(self) -> Generator[tuple[str, str], None, None]: ...
    def __contains__(self, arg: str | tuple[str, str]) -> bool: ...

class KFHistory(Generic[_PT, _ST]):
    kf: KFReader[_PT]
    section: str
    nsteps: int
    shapes: dict[str, tuple[int, ...]]
    blocked: set[str]
    nblocks: int
    def __init__(self, kf: KFReader[_PT], section: _ST) -> None: ...
    def read_all(self, name: str) -> npt.NDArray[Any]: ...
    def iter(self, name: str) -> Generator[Any, None, None]: ...
    @overload
    def iter_optional(self, name: str, default: None = ...) -> Generator[Any | None, None, None]: ...
    @overload
    def iter_optional(self, name: str, default: _T) -> Generator[Any | _T, None, None]: ...
