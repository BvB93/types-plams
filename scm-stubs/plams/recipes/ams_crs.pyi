import sys
from typing import Any, Iterable, Optional, List, Tuple, Union, overload

from scm.plams import Settings, Molecule, AMSResults, CRSResults, JobRunner, JobManager

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

@overload
def run_crs_ams(  # type: ignore[misc]
    settings_ams: Settings[str, Any],
    settings_crs: Settings[str, Any],
    solvents: Union[Molecule, Iterable[Molecule]],
    solutes: Union[None, Molecule, Iterable[Molecule]] = ...,
    return_amsresults: Literal[False] = ...,
    *,
    jobrunner: Optional[JobRunner[Any]] = ...,
    jobmanager: Optional[JobManager] = ...,
    **kwargs: Any,
) -> CRSResults: ...
@overload
def run_crs_ams(
    settings_ams: Settings[str, Any],
    settings_crs: Settings[str, Any],
    solvents: Union[Molecule, Iterable[Molecule]],
    solutes: Union[None, Molecule, Iterable[Molecule]] = ...,
    return_amsresults: Literal[True] = ...,
    *,
    jobrunner: Optional[JobRunner[Any]] = ...,
    jobmanager: Optional[JobManager] = ...,
    **kwargs: Any,
) -> Tuple[CRSResults, List[AMSResults], List[AMSResults]]: ...
