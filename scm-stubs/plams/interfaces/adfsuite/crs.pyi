import sys
from typing import Optional, Union, Sequence, Any, Dict, Set, overload

import pandas as pd
import numpy as np
from matplotlib.pyplot import Figure
from scm.plams import SCMJob, SCMResults, JobRunner, JobManager

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

class CRSResults(SCMResults):
    @property
    def section(self) -> str: ...
    def get_energy(
        self, energy_type: str = ..., compound_idx: int = ..., unit: str = ...
    ) -> float: ...
    def get_activity_coefficient(self, compound_idx: int = ...) -> float: ...
    @overload
    def get_sigma_profile(
        self, subsection: str = ..., unit: str = ..., as_df: Literal[False] = False
    ) -> Dict[str, np.ndarray]: ...
    @overload
    def get_sigma_profile(self, subsection: str = ..., unit: str = ..., as_df: Literal[True] = False) -> pd.DataFrame: ...  # type: ignore[assignment]
    @overload
    def get_sigma_potential(
        self, subsection: str = ..., unit: str = ..., as_df: Literal[False] = False
    ) -> Dict[str, np.ndarray]: ...
    @overload
    def get_sigma_potential(self, subsection: str = ..., unit: str = ..., as_df: Literal[True] = False) -> pd.DataFrame: ...  # type: ignore[assignment]
    def get_prop_names(self, section: Optional[str] = ...) -> Set[str]: ...
    def get_results(self, section: Optional[str] = ...) -> Dict[str, Any]: ...
    def plot(
        self,
        *arrays: np.ndarray,
        x_axis: Union[None, str, Sequence[Any], np.ndarray] = ...,
        plot_fig: bool = ...,
        x_label: Optional[str] = ...,
        y_label: Optional[str] = ...,
    ) -> Figure: ...

class CRSJob(SCMJob):
    results: CRSResults
    def run(
        self,
        jobrunner: Optional[JobRunner[Any]] = ...,
        jobmanager: Optional[JobManager] = ...,
        **kwargs: Any,
    ) -> CRSResults: ...
    @staticmethod
    def cos_to_coskf(filename: str) -> str: ...
