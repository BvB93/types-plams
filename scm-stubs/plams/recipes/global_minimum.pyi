import os
import sys
from collections.abc import Container
from typing import Any

from scm.plams import Job, Molecule, Settings, SingleJob

if sys.version_info >= (3, 8):
    from typing import Literal as L
else:
    from typing_extensions import Literal as L

def global_minimum(
    mol: Molecule,
    n_scans: int = ...,
    no_h: bool = ...,
    no_ring: bool = ...,
    bond_orders: Container[float] = ...,
    job_type: L[False] | type[SingleJob] = ...,
    path: None | str | os.PathLike[str] = ...,
    *,
    name: str = ...,
    settings: None | Settings | Job = ...,
    depend: None | list[Job] = ...,
) -> Molecule: ...
