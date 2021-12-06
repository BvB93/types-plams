import os
from typing import Any, TypeVar, Union, overload

_PT = TypeVar("_PT", bound=Union[str, os.PathLike[str]])

def traj_to_rkf(trajfile: str | os.PathLike[str], rkftrajectoryfile: str | os.PathLike[str]) -> tuple[Any, Any]: ...
@overload
def vasp_output_to_ams(
    vasp_folder: str | os.PathLike[str], wdir: None = ..., overwrite: bool = ..., write_engine_rkf: bool = ...
) -> str: ...
@overload
def vasp_output_to_ams(
    vasp_folder: str | os.PathLike[str], wdir: _PT, overwrite: bool = ..., write_engine_rkf: bool = ...
) -> _PT: ...