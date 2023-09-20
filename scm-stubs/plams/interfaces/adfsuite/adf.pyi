import sys
from typing import Any

import numpy as np
import numpy.typing as npt
from scm.plams import JobManager, JobRunner, Molecule, SCMJob, SCMResults

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

class _TimingsDict(TypedDict):
    elapsed: float
    system: float
    cpu: float

class _EDADictBase(TypedDict):
    Electrostatic: float
    Kinetic: float
    Coulomb: float
    XC: float

class _EDADict(_EDADictBase, total=False):
    Dispersion: float

class ADFResults(SCMResults):
    job: ADFJob
    def __init__(self, job: ADFJob) -> None: ...
    def get_properties(self) -> dict[str, Any]: ...
    def get_main_molecule(self) -> Molecule: ...
    def get_input_molecule(self) -> Molecule: ...
    def get_energy(self, unit: str = ...) -> float: ...
    def get_dipole_vector(self, unit: str = ...) -> list[float]: ...
    def get_gradients(self, eUnit: str = ..., lUnit: str = ...) -> npt.NDArray[np.float64]: ...
    def get_hessian(self) -> npt.NDArray[np.float64]: ...
    def get_energy_decomposition(self, unit: str = ...) -> _EDADict: ...
    def get_frequencies(self, unit: str = ...) -> npt.NDArray[np.float64]: ...
    def get_timings(self) -> _TimingsDict: ...
    def recreate_molecule(self) -> None | Molecule: ...
    def recreate_settings(self) -> None: ...

class ADFJob(SCMJob):
    results: ADFResults
    def run(self, jobrunner: None | JobRunner[Any] = ..., jobmanager: None | JobManager = ..., **kwargs: Any) -> ADFResults: ...
