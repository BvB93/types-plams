import sys
from typing import Dict, Any, List, Optional

import numpy as np
from scm.plams import SCMResults, SCMJob, Molecule, JobRunner, JobManager

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

class TimingsDict(TypedDict):
    elapsed: float
    system: float
    cpu: float

class _EDADict(TypedDict):
    Electrostatic: float
    Kinetic: float
    Coulomb: float
    XC: float

class EDADict(_EDADict, total=False):
    Dispersion: float

class ADFResults(SCMResults):
    def get_properties(self) -> Dict[str, Any]: ...
    def get_main_molecule(self) -> Molecule: ...
    def get_input_molecule(self) -> Molecule: ...
    def get_energy(self, unit: str = ...) -> float: ...
    def get_dipole_vector(self, unit: str = ...) -> List[float]: ...
    def get_gradients(self, eUnit: str = ..., lUnit: str = ...) -> np.ndarray: ...
    def get_hessian(self) -> np.ndarray: ...
    def get_energy_decomposition(self, unit: str = ...) -> EDADict: ...
    def get_frequencies(self, unit: str = ...) -> np.ndarray: ...
    def get_timings(self) -> TimingsDict: ...
    def recreate_molecule(self) -> Optional[Molecule]: ...
    def recreate_settings(self) -> None: ...

class ADFJob(SCMJob):
    results: ADFResults
    def run(
        self,
        jobrunner: Optional[JobRunner[Any]] = ...,
        jobmanager: Optional[JobManager] = ...,
        **kwargs: Any,
    ) -> ADFResults: ...
