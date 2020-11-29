import sys
from os import PathLike
from typing import (
    Dict,
    Union,
    List,
    Tuple,
    Generator,
    Set,
    Any,
    Optional,
    overload,
    Generic,
    TypeVar,
)

import numpy as np

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

PT = TypeVar("PT", str, bytes, PathLike[str], PathLike[bytes])
ST = TypeVar("ST", bound=str)
Scalar = Union[bool, int, float, str]

class KFReader(Generic[PT]):
    endian: Literal["<", ">"]
    word: Literal["i", "q"]
    path: PT
    def __init__(
        self, path: PT, blocksize: int = ..., autodetect: bool = ...
    ) -> None: ...
    def read(self, section: str, variable: str) -> Any: ...
    def __iter__(self) -> Generator[Tuple[str, str], None, None]: ...

class KFFile:
    autosave: bool
    path: str
    tmpdat: Dict[str, Dict[str, Any]]
    reader: Optional[KFReader[str]]
    def __init__(
        self, path: Union[str, PathLike[str]], autosave: bool = ...
    ) -> None: ...
    @overload
    def read(
        self, section: str, variable: str, return_as_list: Literal[False] = ...
    ) -> Any: ...
    @overload
    def read(
        self, section: str, variable: str, return_as_list: Literal[True]
    ) -> List[Any]: ...
    def write(
        self, section: str, variable: str, value: Union[Scalar, List[Scalar]]
    ) -> None: ...
    def save(self) -> None: ...
    def delete_section(self, section: str) -> None: ...
    def sections(self) -> List[str]: ...
    def read_section(self, section: str) -> Dict[str, Any]: ...
    def get_skeleton(self) -> Dict[str, Set[str]]: ...
    def __getitem__(self, name: Union[str, Tuple[str, str]]) -> Any: ...
    def __setitem__(
        self, name: Union[str, Tuple[str, str]], value: Union[Scalar, List[Scalar]]
    ) -> None: ...
    def __iter__(self) -> Generator[Tuple[str, str], None, None]: ...
    def __contains__(self, arg: Union[str, Tuple[str, str]]) -> bool: ...

class KFHistory(Generic[PT, ST]):
    kf: KFReader[PT]
    section: str
    nsteps: int
    shapes: Dict[str, Tuple[int, ...]]
    blocked: Set[str]
    nblocks: int
    def __init__(self, kf: KFReader[PT], section: ST) -> None: ...
    def read_all(self, name: str) -> np.ndarray: ...
    def iter(self, name: str) -> Generator[Any, None, None]: ...
    def iter_optional(self, name: str, default: Optional[Any] = ...) -> Any: ...
