import sys
from os import PathLike
from typing import Dict, Any, Set, List, Optional, Union

import numpy as np
from scm.plams import Molecule, Settings, JobRunner, JobManager, KFFile, SingleJob, Results, Job

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

class TimingsDict(TypedDict):
    elapsed: float
    system: float
    cpu: float

class AMSResults(Results):
    rkfs: Dict[str, KFFile]
    def __init__(self, job: AMSJob) -> None: ...
    def collect(self) -> None: ...
    def refresh(self) -> None: ...
    def engine_names(self) -> List[str]: ...
    def rkfpath(self, file: str = ...) -> str: ...
    def readrkf(self, section: str, variable: str, file: str = ...) -> Any: ...
    def read_rkf_section(self, section: str, file: str = ...) -> Dict[str, Any]: ...
    def get_rkf_skeleton(self, file: str = ...) -> Dict[str, Set[str]]: ...
    def get_molecule(self, section: str, file: str = ...) -> Molecule: ...
    def get_input_molecule(self) -> Molecule: ...
    def get_main_molecule(self) -> Molecule: ...
    def get_history_molecule(self, step: int) -> Molecule: ...
    def get_history_variables(self, history_section: str = ...) -> Set[str]: ...
    def get_history_property(self, varname: str, history_section: str = ...) -> List[Any]: ...
    def get_property_at_step(self, step: int, varname: str, history_section: str = ...) -> Any: ...
    def get_engine_results(self, engine: Optional[str] = ...) -> Dict[str, Any]: ...
    def get_engine_properties(self, engine: Optional[str] = ...) -> Dict[str, Any]: ...
    def get_energy(self, unit: str = ..., engine: Optional[str] = ...) -> float: ...
    def get_gradients(self, energy_unit: str = ..., dist_unit: str = ..., engine: Optional[str] = ...) -> np.ndarray: ...
    def get_stresstensor(self, engine: Optional[str] = ...) -> np.ndarray: ...
    def get_hessian(self, engine: Optional[str] = ...) -> np.ndarray: ...
    def get_elastictensor(self, engine: Optional[str] = ...) -> np.ndarray: ...
    def get_frequencies(self, unit: str = ..., engine: Optional[str] = ...) -> np.ndarray: ...
    def get_charges(self, engine: Optional[str] = ...) -> np.ndarray: ...
    def get_dipolemoment(self, engine: Optional[str] = ...) -> np.ndarray: ...
    def get_dipolegradients(self, engine: Optional[str] = ...) -> np.ndarray: ...
    def get_timings(self) -> TimingsDict: ...
    def recreate_molecule(self) -> Optional[Molecule]: ...
    def recreate_settings(self) -> Optional[Settings]: ...
    def ok(self) -> bool: ...
    def get_errormsg(self) -> str: ...
    @property
    def name(self) -> str: ...

class AMSJob(SingleJob):
    def run(
        self,
        jobrunner: Optional[JobRunner] = ...,
        jobmanager: Optional[JobManager] = ...,
        **kwargs: Any,
    ) -> AMSResults: ...
    def get_input(self) -> str: ...
    def get_runscript(self) -> str: ...
    def check(self) -> bool: ...
    def get_errormsg(self) -> str: ...
    def hash_input(self) -> str: ...
    @classmethod
    def from_inputfile(
        cls,
        filename: Union[str, PathLike[str]],
        heredoc_delimit: str = ...,
        *,
        name: str = ...,
        depend: Optional[List[Job]] = ...,
    ) -> AMSJob: ...
    @staticmethod
    def settings_to_mol(s: Settings) -> Dict[str, Molecule]: ...