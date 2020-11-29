from os import PathLike
from typing import (
    List,
    Union,
    Optional,
    Any,
    Collection,
    TypeVar,
    Generic,
    Generator,
    Iterator,
)
from abc import ABCMeta, abstractmethod

from scm.plams import Results, Settings, JobRunner, JobManager, Molecule

JT = TypeVar("JT", bound=Job)

class Job(metaclass=ABCMeta):
    results: Results
    status: str
    name: str
    jobmanager: None
    parent: None
    settings: Settings[str, Any]
    default_settings: List[Settings[str, Any]]
    depend: List[Job]
    def __init__(
        self,
        name: str = ...,
        settings: Union[None, Settings[str, Any], Job] = ...,
        depend: Optional[List[Job]] = ...,
    ) -> None: ...
    def run(
        self,
        jobrunner: Optional[JobRunner[Any]] = ...,
        jobmanager: Optional[JobManager] = ...,
        **kwargs: Any,
    ) -> Results: ...
    def pickle(self, filename: Union[None, str, PathLike[str]] = ...) -> None: ...
    def ok(self, strict: bool = ...) -> bool: ...
    @abstractmethod
    def check(self) -> bool: ...
    @abstractmethod
    def hash(self) -> Optional[str]: ...
    def prerun(self) -> None: ...
    def postrun(self) -> None: ...

class SingleJob(Job, metaclass=ABCMeta):
    molecule: Optional[Molecule]
    def __init__(
        self,
        molecule: Optional[Molecule] = ...,
        *,
        name: str = ...,
        settings: Union[None, Settings[str, Any], Job] = ...,
        depend: Optional[List[Job]] = ...,
    ) -> None: ...
    @abstractmethod
    def get_input(self) -> Any: ...
    @abstractmethod
    def get_runscript(self) -> Any: ...
    def hash_input(self) -> str: ...
    def hash_runscript(self) -> str: ...
    def hash(self) -> str: ...
    def check(self) -> bool: ...
    def full_runscript(self) -> str: ...
    @classmethod
    def load_external(
        cls,
        path: Union[str, PathLike[str]],
        settings: Optional[Settings[str, Any]] = ...,
        molecule: Optional[Molecule] = ...,
        finalize: bool = ...,
    ) -> Job: ...

class MultiJob(Job, Generic[JT]):
    children: Collection[JT]
    childrunner: Optional[JobRunner[Any]]
    def __init__(
        self,
        children: Optional[Collection[JT]] = ...,
        childrunner: Optional[JobRunner[Any]] = ...,
        *,
        name: str = ...,
        settings: Union[None, Settings[str, Any], Job] = ...,
        depend: Optional[List[Job]] = ...,
    ) -> None: ...
    def new_children(self) -> None: ...
    def hash(self) -> None: ...
    def check(self) -> bool: ...
    def other_jobs(self) -> Generator[JT, None, None]: ...
    def remove_child(self, job: JT) -> None: ...
    def __iter__(self) -> Iterator[JT]: ...
