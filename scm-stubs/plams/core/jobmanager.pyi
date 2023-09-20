import os
from typing import Any

from scm.plams import Job, Settings

class JobManager:
    settings: Settings
    jobs: list[Any]
    names: dict[str, int]
    hashes: dict[str, Any]
    path: str
    foldername: str
    workdir: str
    logfile: str
    input: str
    def __init__(
        self, settings: Settings, path: None | str | os.PathLike[str] = ..., folder: None | str | os.PathLike[str] = ...
    ) -> None: ...
    def load_job(self, filename: str | os.PathLike[str]) -> Any: ...
    def remove_job(self, job: Job) -> None: ...
