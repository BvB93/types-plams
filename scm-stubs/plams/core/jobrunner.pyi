from typing import Optional, TypeVar, Generic, ClassVar, List, type_check_only, Any
from threading import BoundedSemaphore

from scm.plams import Settings

BST = TypeVar("BST", None, BoundedSemaphore)

@type_check_only
class _MetaRunner(type): ...

class JobRunner(Generic[BST], metaclass=_MetaRunner):
    parallel: bool
    semaphore: Optional[BoundedSemaphore]
    def __init__(self, parallel: bool = ..., maxjobs: int = ...) -> None: ...
    def call(
        self, runscript: str, workdir: str, out: str, err: str, runflags: Settings[str, Any]
    ) -> int: ...

class GridRunner(JobRunner[BST]):
    config: ClassVar[Settings[str, Any]] = ...
    sleepstep: int
    settings: Settings[str, Any]
    def __slurm_get_jobid(self, output: str) -> Optional[str]: ...
    def __slurm_running(self, output: str) -> List[str]: ...
    def __pbs_get_jobid(self, output: str) -> Optional[str]: ...
    def __pbs_running(self, output: str) -> List[str]: ...
    def __init__(
        self,
        grid: str = ...,
        sleepstep: int = ...,
        parallel: bool = ...,
        maxjobs: int = ...,
    ) -> None: ...
    def call(
        self, runscript: str, workdir: str, out: str, err: str, runflags: Settings[str, Any]
    ) -> int: ...
