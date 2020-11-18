from typing import Dict, overload, Iterable, Union, Any

import numpy as np

T = TypeVar("T", bound=Union[float, np.generic, None, str])

class Units:
    constants: Dict[str, float]
    distance: Dict[str, float]
    rec_distance: Dict[str, float]
    energy: Dict[str, float]
    angle: Dict[str, float]
    dipole: Dict[str, float]
    forces: Dict[str, float]
    hessian: Dict[str, float]
    stress: Dict[str, float]
    dicts: Dict[str, Dict[str, float]]
    @classmethod
    def find_unit(cls, unit: str) -> Dict[str, str]: ...
    @classmethod
    def conversion_ratio(cls, inp: str, out: str) -> float: ...
    @overload
    @classmethod
    def convert(cls, value: T, inp: str, out: str) -> T: ...
    @overload
    @classmethod
    def convert(cls, value: Iterable[Any], inp: str, out: str) -> np.ndarray: ...
