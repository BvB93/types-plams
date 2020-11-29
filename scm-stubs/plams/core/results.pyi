from threading import Event
from typing import type_check_only, overload, List, Optional, Any, Callable, TypeVar

from scm.plams import Job, Molecule, Settings

T = TypeVar("T")
@type_check_only
class _MetaResults(type): ...

class Results(metaclass=_MetaResults):
    job: Job
    files: List[str]
    finished: Event
    done: Event
    def __init__(self, job: Job) -> None: ...
    def refresh(self) -> None: ...
    def collect(self) -> None: ...
    def wait(self) -> None: ...
    def grep_file(
        self, filename: str, pattern: str = ..., options: str = ...
    ) -> List[str]: ...
    def grep_output(self, pattern: str = ..., options: str = ...) -> List[str]: ...
    def awk_file(
        self,
        filename: str,
        script: str = ...,
        progfile: Optional[str] = ...,
        **kwargs: Any
    ) -> List[str]: ...
    def awk_output(
        self, script: str = ..., progfile: Optional[str] = ..., **kwargs: Any
    ) -> List[str]: ...
    def rename(self, old: str, new: str) -> None: ...
    @overload
    def get_file_chunk(
        self,
        filename: str,
        begin: Optional[str] = ...,
        end: Optional[str] = ...,
        match: int = ...,
        inc_begin: bool = ...,
        inc_end: bool = ...,
        process: None = ...,
    ) -> List[str]: ...
    @overload
    def get_file_chunk(
        self,
        filename: str,
        begin: Optional[str] = ...,
        end: Optional[str] = ...,
        match: int = ...,
        inc_begin: bool = ...,
        inc_end: bool = ...,
        process: Callable[[str], T] = ...,
    ) -> List[T]: ...
    @overload
    def get_output_chunk(
        self,
        begin: Optional[str] = ...,
        end: Optional[str] = ...,
        match: int = ...,
        inc_begin: bool = ...,
        inc_end: bool = ...,
        process: None = ...,
    ) -> List[str]: ...
    @overload
    def get_output_chunk(
        self,
        begin: Optional[str] = ...,
        end: Optional[str] = ...,
        match: int = ...,
        inc_begin: bool = ...,
        inc_end: bool = ...,
        process: Callable[[str], T] = ...,
    ) -> List[T]: ...
    def recreate_molecule(self) -> Optional[Molecule]: ...
    def recreate_settings(self) -> Optional[Settings[str, Any]]: ...
    def __getitem__(self, name: str) -> str: ...
