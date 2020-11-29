import sys
from os import PathLike
from typing import Optional, List, Any, Union, Container, Type

from scm.plams import Molecule, SingleJob, Job, Settings

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

def global_minimum(
    mol: Molecule,
    n_scans: int = ...,
    no_h: bool = ...,
    no_ring: bool = ...,
    bond_orders: Container[float] = ...,
    job_type: Union[Literal[False], Type[SingleJob]] = ...,
    path: Union[None, str, PathLike[str]] = ...,
    *,
    name: str = ...,
    settings: Union[None, Settings[str, Any], Job] = ...,
    depend: Optional[List[Job]] = ...,
) -> Molecule: ...
