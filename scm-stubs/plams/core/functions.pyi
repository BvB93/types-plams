import os
import sys
import threading
from collections.abc import Callable, Mapping
from typing import Any, Iterable

from scm.plams import Job, JobManager, Molecule, Settings

if sys.version_info >= (3, 8):
    from typing import Literal as L
else:
    from typing_extensions import Literal as L

config: Settings

def init(
    path: None | str | os.PathLike[str] = ...,
    folder: None | str | os.PathLike[str] = ...,
    config_settings: None | Mapping[str, Any] = ...,
) -> None: ...
def finish(otherJM: None | Iterable[JobManager] = ...) -> None: ...
def load(filename: str | os.PathLike[str]) -> Any: ...
def load_all(path: str | os.PathLike[str], jobmanager: None | JobManager = ...) -> dict[str, Any]: ...
def delete_job(job: Job) -> None: ...
def read_molecules(
    folder: str | os.PathLike[str], formats: L[None, "xyz", "pdb", "mol", "mol2", "rkf"] = ...
) -> dict[str, Molecule]: ...
def read_all_molecules_in_xyz_file(filename: str | bytes | os.PathLike[str] | os.PathLike[bytes]) -> list[Molecule]: ...
def log(message: str, level: int = ...) -> None: ...
def add_to_class(classname: type) -> Callable[[Callable[..., Any]], None]: ...
def add_to_instance(instance: object) -> Callable[[Callable[..., Any]], None]: ...
def parse_heredoc(bash_input: str, heredoc_delimit: str = ...) -> str: ...

_stdlock: threading.Lock
_filelock: threading.Lock
