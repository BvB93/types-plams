import sys
from typing import Optional, TypeVar, Generic, ClassVar, List, type_check_only, Any, overload, Union
from threading import BoundedSemaphore

from scm.plams import Settings

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

BST = TypeVar("BST", None, BoundedSemaphore)
@type_check_only
class _MetaRunner(type): ...

class JobRunner(Generic[BST], metaclass=_MetaRunner):
    parallel: bool
    semaphore: Optional[BoundedSemaphore]
    @overload
    def __new__(  # type: ignore[misc]
        cls, parallel: bool = ..., maxjobs: Literal[0] = ...
    ) -> JobRunner[None]: ...
    @overload
    def __new__(
        cls, parallel: bool = ..., maxjobs: int = ...
    ) -> JobRunner[BoundedSemaphore]: ...
    def call(
        self,
        runscript: str,
        workdir: str,
        out: str,
        err: str,
        runflags: Settings[str, Any],
    ) -> int: ...

class GridRunner(JobRunner[BST]):
    config: ClassVar[Settings[str, Any]] = ...
    sleepstep: int
    settings: Settings[str, Settings[str, Any]]
    def __slurm_get_jobid(self, output: str) -> Optional[str]: ...
    def __slurm_running(self, output: str) -> List[str]: ...
    def __pbs_get_jobid(self, output: str) -> Optional[str]: ...
    def __pbs_running(self, output: str) -> List[str]: ...
    @overload
    def __new__(  # type: ignore[misc]
        cls,
        grid: Union[Settings[str, Any], Literal["auto", "pbs", "slurm"]] = ...,
        sleepstep: int = ...,
        parallel: bool = ...,
        maxjobs: Literal[0] = ...
    ) -> GridRunner[None]: ...
    @overload
    def __new__(
        cls,
        grid: Union[Settings[str, Any], Literal["auto", "pbs", "slurm"]] = ...,
        sleepstep: int = ...,
        parallel: bool = ...,
        maxjobs: int = ...
    ) -> GridRunner[BoundedSemaphore]: ...
    def call(
        self,
        runscript: str,
        workdir: str,
        out: str,
        err: str,
        runflags: Settings[str, Any],
    ) -> int: ...
