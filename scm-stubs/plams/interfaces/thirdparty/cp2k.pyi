import sys
from os import PathLike
from typing import List, Optional, Union, Tuple, overload, Any

from scm.plams import Results, SingleJob, Molecule, Settings, Job, JobManager, JobRunner

if sys.version_info >= (3, 8):
    from typing import Literal, TypedDict
else:
    from typing_extensions import Literal, TypedDict

class MultigridDict(TypedDict):
    counts: List[int]
    cutoffs: List[float]

class Cp2kResults(Results):
    def recreate_settings(self) -> Settings[str, Any]: ...
    def get_runtime(self) -> float: ...
    def get_energy(self, index: int = ...) -> float: ...
    def get_dispersion(self, index: int = ...) -> float: ...
    @overload
    def get_mulliken_charges(
        self, return_spin: Literal[False] = ..., index: int = ...
    ) -> Union[float, List[float]]: ...
    @overload
    def get_mulliken_charges(
        self, return_spin: Literal[True], index: int = ...
    ) -> Union[Tuple[float, float], Tuple[List[float], List[float]]]: ...
    @overload
    def get_hirshfeld_charges(
        self, return_spin: Literal[False] = ..., index: int = ...
    ) -> Union[float, List[float]]: ...
    @overload
    def get_hirshfeld_charges(
        self, return_spin: Literal[True], index: int = ...
    ) -> Union[Tuple[float, float], Tuple[List[float], List[float]]]: ...
    def get_multigrid_info(self) -> MultigridDict: ...

class Cp2kJob(SingleJob):
    def __init__(
        self,
        copy: Union[None, str, PathLike[str], List[Union[str, PathLike[str]]]] = ...,
        *,
        molecule: Optional[Molecule] = ...,
        name: str = ...,
        settings: Union[None, Settings[str, Any], Job] = ...,
        depend: Optional[List[Job]] = ...,
    ) -> None: ...
    def run(
        self,
        jobrunner: Optional[JobRunner[Any]] = ...,
        jobmanager: Optional[JobManager] = ...,
        **kwargs: Any,
    ) -> Cp2kResults: ...
    def get_input(self) -> str: ...
    def get_runscript(self) -> str: ...
    def check(self) -> bool: ...

def Cp2kSettings2Mol(settings: Settings[str, Any]) -> Optional[Molecule]: ...
