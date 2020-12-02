import sys

from types import TracebackType
from typing import (
    overload,
    TypeVar,
    Mapping,
    Dict,
    Generic,
    Type,
    Any,
    Iterable,
    Sequence,
    Tuple,
    Callable,
    Optional,
)

if sys.version_info >= (3, 8):
    from typing import Protocol
else:
    from typing_extensions import Protocol

KT = TypeVar("KT")
VT = TypeVar("VT")
KT_contra = TypeVar("KT_contra", contravariant=True)
T_co = TypeVar("T_co", covariant=True)
MT = TypeVar("MT", bound=SupportsMissing[Any, Any])
ST = TypeVar("ST", bound=Settings[Any, Any])

class SupportsMissing(Protocol[KT_contra, T_co]):
    def __missing__(self, __key: KT_contra) -> T_co: ...

class Settings(Dict[KT, VT]):
    def copy(self: ST) -> ST: ...
    def soft_update(self: ST, other: Mapping[KT, VT]) -> ST: ...
    def update(self, other: Mapping[KT, VT]) -> None: ...  # type: ignore[override]
    def merge(self: ST, other: Mapping[KT, VT]) -> ST: ...
    def find_case(self, key: KT) -> KT: ...
    def as_dict(self) -> Dict[KT, VT]: ...
    @classmethod
    def suppress_missing(cls: Type[MT]) -> SuppressMissing[MT]: ...
    def get_nested(
        self, key_tuple: Iterable[Any], suppress_missing: bool = False
    ) -> Any: ...
    def set_nested(
        self, key_tuple: Sequence[Any], value: Any, suppress_missing: bool = False
    ) -> None: ...
    def flatten(self, flatten_list: bool = ...) -> Settings[Tuple[Any, ...], Any]: ...
    def unflatten(self, unflatten_list: bool = ...) -> Settings[Any, Any]: ...
    @classmethod  # type: ignore[override]
    @overload
    def fromkeys(cls, __iterable: Iterable[KT]) -> Settings[KT, Any]: ...
    @classmethod
    @overload
    def fromkeys(cls, __iterable: Iterable[KT], __value: VT) -> Settings[KT, VT]: ...
    @overload
    def __missing__(self: Settings[KT, Settings[Any, Any]], name: KT) -> VT: ...
    @overload
    def __missing__(self, name: KT) -> Settings[Any, Any]: ...
    def __getattr__(self, name: KT) -> VT: ...  # type: ignore[misc]
    def __setattr__(self, name: KT, value: VT) -> None: ...  # type: ignore[misc,override]
    def __str__(self) -> str: ...
    def __repr__(self) -> str: ...
    def __add__(self: ST, other: Mapping[KT, VT]) -> ST: ...
    def __iadd__(self: ST, other: Mapping[KT, VT]) -> ST: ...
    def __copy__(self: ST) -> ST: ...

class SuppressMissing(Generic[MT]):
    obj: MT
    @property
    def missing(
        self: SuppressMissing[SupportsMissing[KT_contra, T_co]]
    ) -> Callable[[MT, KT_contra], T_co]: ...
    @missing.setter
    def missing(
        self: SuppressMissing[SupportsMissing[KT_contra, T_co]],
        value: Callable[[MT, KT_contra], T_co],
    ) -> None: ...
    def __init__(self, obj: Type[MT]) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException],
        traceback: Optional[TracebackType],
    ) -> None: ...
