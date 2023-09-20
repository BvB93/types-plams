import sys
from collections.abc import Sequence
from typing import Any, overload

import matplotlib.pyplot as plt
import numpy as np
import numpy.typing as npt
import pandas as pd
from scm.plams import JobManager, JobRunner, SCMJob, SCMResults

if sys.version_info >= (3, 8):
    from typing import Literal as L
else:
    from typing_extensions import Literal as L

class CRSResults(SCMResults):
    job: CRSJob
    def __init__(self, job: CRSJob) -> None: ...
    @property
    def section(self) -> str: ...
    def get_energy(self, energy_type: str = ..., compound_idx: int = ..., unit: str = ...) -> float: ...
    def get_activity_coefficient(self, compound_idx: int = ...) -> float: ...
    @overload
    def get_sigma_profile(
        self, subsection: str = ..., unit: str = ..., *, as_df: L[False] = ...
    ) -> dict[str, npt.NDArray[np.float64]]: ...
    @overload
    def get_sigma_profile(self, subsection: str = ..., unit: str = ..., *, as_df: L[True]) -> pd.DataFrame: ...
    @overload
    def get_sigma_potential(
        self, subsection: str = ..., unit: str = ..., *, as_df: L[False] = ...
    ) -> dict[str, npt.NDArray[np.float64]]: ...
    @overload
    def get_sigma_potential(self, subsection: str = ..., unit: str = ..., *, as_df: L[True]) -> pd.DataFrame: ...
    def get_prop_names(self, section: None | str = ...) -> set[str]: ...
    def get_results(self, section: None | str = ...) -> dict[str, Any]: ...
    def plot(
        self,
        *arrays: npt.NDArray[np.float64],
        x_axis: None | str | Sequence[Any] | npt.NDArray[np.float64] = ...,
        plot_fig: bool = ...,
        x_label: None | str = ...,
        y_label: None | str = ...,
    ) -> plt.Figure: ...

class CRSJob(SCMJob):
    results: CRSResults
    def run(self, jobrunner: None | JobRunner[Any] = ..., jobmanager: None | JobManager = ..., **kwargs: Any) -> CRSResults: ...
    @staticmethod
    def cos_to_coskf(filename: str) -> str: ...
