from typing import Union, Any, List, Dict
from os import PathLike

from scm.plams import Settings, Job

class JobManager:
    settings: Settings[str, Any]
    jobs: List[Any]
    names: Dict[str, int]
    hashes: Dict[str, Any]
    path: str
    foldername: str
    workdir: str
    logfile: str
    input: str
    def __init__(
        self,
        settings: Settings[str, Any],
        path: Union[None, str, PathLike[str]] = ...,
        folder: Union[None, str, PathLike[str]] = ...,
    ) -> None: ...
    def load_job(self, filename: Union[str, PathLike[str]]) -> Any: ...
    def remove_job(self, job: Job) -> None: ...
