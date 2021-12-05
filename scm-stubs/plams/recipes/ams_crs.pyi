import sys
from collections.abc import Iterable
from typing import Any, overload

from scm.plams import AMSResults, CRSResults, JobManager, JobRunner, Molecule, Settings

if sys.version_info >= (3, 8):
    from typing import Literal as L
else:
    from typing_extensions import Literal as L

@overload
def run_crs_ams(
    settings_ams: Settings[str, Any],
    settings_crs: Settings[str, Any],
    solvents: Molecule | Iterable[Molecule],
    solutes: None | Molecule | Iterable[Molecule] = ...,
    *,
    return_amsresults: L[False] = ...,
    jobrunner: None | JobRunner[Any] = ...,
    jobmanager: None | JobManager = ...,
    **kwargs: Any,
) -> CRSResults: ...
@overload
def run_crs_ams(
    settings_ams: Settings[str, Any],
    settings_crs: Settings[str, Any],
    solvents: Molecule | Iterable[Molecule],
    solutes: None | Molecule | Iterable[Molecule] = ...,
    *,
    return_amsresults: L[True],
    jobrunner: None | JobRunner[Any] = ...,
    jobmanager: None | JobManager = ...,
    **kwargs: Any,
) -> tuple[CRSResults, list[AMSResults], list[AMSResults]]: ...
