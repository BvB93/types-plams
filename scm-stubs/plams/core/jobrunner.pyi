import sys
import threading
from typing import Any, ClassVar, Generic, TypeVar, overload

from scm.plams import Settings

if sys.version_info >= (3, 8):
    from typing import Literal as L
else:
    from typing_extensions import Literal as L

_BST = TypeVar("_BST", None, threading.BoundedSemaphore)

class _MetaRunner(type): ...

class JobRunner(Generic[_BST], metaclass=_MetaRunner):
    parallel: bool
    semaphore: None | threading.BoundedSemaphore
    @overload
    def __new__(cls, parallel: bool = ..., maxjobs: L[0] = ...) -> JobRunner[None]: ...  # type: ignore[misc]
    @overload
    def __new__(cls, parallel: bool = ..., maxjobs: int = ...) -> JobRunner[threading.BoundedSemaphore]: ...
    def call(self, runscript: str, workdir: str, out: str, err: str, runflags: Settings[str, Any]) -> int: ...

class GridRunner(JobRunner[_BST]):
    config: ClassVar[Settings[str, Any]] = ...
    sleepstep: int
    settings: Settings[str, Settings[str, Any]]
    def __slurm_get_jobid(self, output: str) -> None | str: ...
    def __slurm_running(self, output: str) -> list[str]: ...
    def __pbs_get_jobid(self, output: str) -> None | str: ...
    def __pbs_running(self, output: str) -> list[str]: ...
    @overload
    def __new__(  # type: ignore[misc]
        cls,
        grid: Settings[str, Any] | L["auto", "pbs", "slurm"] = ...,
        sleepstep: int = ...,
        parallel: bool = ...,
        maxjobs: L[0] = ...,
    ) -> GridRunner[None]: ...
    @overload
    def __new__(
        cls,
        grid: Settings[str, Any] | L["auto", "pbs", "slurm"] = ...,
        sleepstep: int = ...,
        parallel: bool = ...,
        maxjobs: int = ...,
    ) -> GridRunner[threading.BoundedSemaphore]: ...
    def call(self, runscript: str, workdir: str, out: str, err: str, runflags: Settings[str, Any]) -> int: ...
