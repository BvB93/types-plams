import os
from collections.abc import Collection
from typing import Any, TypeVar

import numpy.typing as npt
from scm.plams import Job, KFFile, Molecule, Results, Settings, SingleJob

_CT = TypeVar("_CT", bound=Collection[Any])
_JT = TypeVar("_JT", bound=SCMJob)

class SCMResults(Results):
    job: SCMJob
    _kf: KFFile
    def __init__(self, job: SCMJob) -> None: ...
    def collect(self) -> None: ...
    def refresh(self) -> None: ...
    def readkf(self, section: str, variable: str) -> Any: ...
    def newkf(self, filename: str | os.PathLike[str]) -> KFFile: ...
    def get_properties(self) -> dict[str, Any]: ...
    def get_molecule(self, section: str, variable: str, unit: str = ..., internal: bool = ..., n: int = ...) -> Molecule: ...
    def to_input_order(self, data: _CT) -> _CT: ...
    def readarray(self, section: str, subsection: str, **kwargs: Any) -> npt.NDArray[Any]: ...

class SCMJob(SingleJob):
    results: SCMResults
    def get_input(self) -> str: ...
    def get_runscript(self) -> str: ...
    def check(self) -> bool: ...
    def hash_input(self) -> str: ...
    @classmethod
    def from_inputfile(
        cls: type[_JT],
        filename: str | os.PathLike[str],
        heredoc_delimit: str = ...,
        *,
        name: str = ...,
        depend: None | list[Job] = ...,
    ) -> _JT: ...
    @staticmethod
    def settings_to_mol(s: Settings) -> None: ...
