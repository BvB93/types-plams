import os
import sys
from collections.abc import Sequence
from typing import Any, Dict, TypeVar, overload

import numpy as np
from scm.plams import AMSJob, Molecule

if sys.version_info >= (3, 8):
    from typing import Literal as L
else:
    from typing_extensions import Literal as L

_DT = TypeVar("_DT", bound=Dict[Any, Any])

@overload
def get_stoichiometry(job_or_molecule_or_path: AMSJob | Molecule | str, as_dict: L[False] = ...) -> str: ...
@overload
def get_stoichiometry(job_or_molecule_or_path: AMSJob | Molecule | str, as_dict: L[True]) -> dict[str, int]: ...
@overload
def get_stoichiometry(job_or_molecule_or_path: _DT, as_dict: bool = ...) -> _DT: ...
def balance_equation(
    reactants: Sequence[AMSJob | Molecule | str | dict[str, int]],
    products: Sequence[AMSJob | Molecule | str | dict[str, int]],
    normalization: str = ...,
    normalization_value: float = ...,
) -> tuple[list[np.float_], list[np.float_]]: ...
def reaction_energy(
    reactants: AMSJob | str | os.PathLike[str],
    products: AMSJob | str | os.PathLike[str],
    normalization: str = ...,
    unit: str = ...,
) -> tuple[list[np.float_], list[np.float_], np.float_]: ...
