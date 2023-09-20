from threading import Event
from typing import Any, Callable, TypeVar, overload

from scm.plams import Job, Molecule, Settings

_T = TypeVar("_T")

class _MetaResults(type): ...

class Results(metaclass=_MetaResults):
    job: Job
    files: list[str]
    finished: Event
    done: Event
    def __init__(self, job: Job) -> None: ...
    def refresh(self) -> None: ...
    def collect(self) -> None: ...
    def wait(self) -> None: ...
    def grep_file(self, filename: str, pattern: str = ..., options: str = ...) -> list[str]: ...
    def grep_output(self, pattern: str = ..., options: str = ...) -> list[str]: ...
    def awk_file(self, filename: str, script: str = ..., progfile: None | str = ..., **kwargs: Any) -> list[str]: ...
    def awk_output(self, script: str = ..., progfile: None | str = ..., **kwargs: Any) -> list[str]: ...
    def rename(self, old: str, new: str) -> None: ...
    @overload
    def get_file_chunk(
        self,
        filename: str,
        begin: None | str = ...,
        end: None | str = ...,
        match: int = ...,
        inc_begin: bool = ...,
        inc_end: bool = ...,
        process: None = ...,
    ) -> list[str]: ...
    @overload
    def get_file_chunk(
        self,
        filename: str,
        begin: None | str = ...,
        end: None | str = ...,
        match: int = ...,
        inc_begin: bool = ...,
        inc_end: bool = ...,
        process: Callable[[str], _T] = ...,
    ) -> list[_T]: ...
    @overload
    def get_output_chunk(
        self,
        begin: None | str = ...,
        end: None | str = ...,
        match: int = ...,
        inc_begin: bool = ...,
        inc_end: bool = ...,
        process: None = ...,
    ) -> list[str]: ...
    @overload
    def get_output_chunk(
        self,
        begin: None | str = ...,
        end: None | str = ...,
        match: int = ...,
        inc_begin: bool = ...,
        inc_end: bool = ...,
        process: Callable[[str], _T] = ...,
    ) -> list[_T]: ...
    def recreate_molecule(self) -> None | Molecule: ...
    def recreate_settings(self) -> None | Settings: ...
    def __getitem__(self, name: str) -> str: ...
