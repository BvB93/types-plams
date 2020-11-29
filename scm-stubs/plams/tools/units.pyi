import sys
from typing import Dict, overload, Iterable, Union, Any, TypeVar

import numpy as np

if sys.version_info >= (3, 8):
    from typing import Literal, TypedDict
else:
    from typing_extensions import Literal, TypedDict

Constants = Literal['Bohr_radius', 'Avogadro_constant', 'NA', 'speed_of_light', 'c', 'electron_charge', 'e', 'Boltzmann', 'k_B']
Distance = Literal['A', 'Angstrom', 'Bohr', 'a.u.', 'au', 'nm', 'pm', 'm']
Energy = Literal['au', 'a.u.', 'Hartree', 'Ha', 'eV', 'kJ/mol', 'J', 'kcal/mol', 'cm^-1', 'cm-1', 'K']
Angle = Literal['degree', 'deg', 'radian', 'rad', 'grad', 'circle']
Dipole = Literal['au', 'a.u.', 'Cm', 'Debye', 'D']
RecDistance = Literal['1/A', '1/Ang', '1/Angstrom', 'A^-1', 'Ang^-1', 'Angstrom^-1', '1/m', 'm^-1', '1/Bohr', 'Bohr^-1']
Forces = Literal['au/Angstrom', 'au/Ang', 'au/A', 'au/bohr', 'au/au', 'au/a.u.', 'au/m', 'a.u./Angstrom', 'a.u./Ang', 'a.u./A', 'a.u./bohr', 'a.u./au', 'a.u./a.u.', 'a.u./m', 'Hartree/Angstrom', 'Hartree/Ang', 'Hartree/A', 'Hartree/bohr', 'Hartree/au', 'Hartree/a.u.', 'Hartree/m', 'Ha/Angstrom', 'Ha/Ang', 'Ha/A', 'Ha/bohr', 'Ha/au', 'Ha/a.u.', 'Ha/m', 'eV/Angstrom', 'eV/Ang', 'eV/A', 'eV/bohr', 'eV/au', 'eV/a.u.', 'eV/m', 'kJ/mol/Angstrom', 'kJ/mol/Ang', 'kJ/mol/A', 'kJ/mol/bohr', 'kJ/mol/au', 'kJ/mol/a.u.', 'kJ/mol/m', 'J/Angstrom', 'J/Ang', 'J/A', 'J/bohr', 'J/au', 'J/a.u.', 'J/m', 'kcal/mol/Angstrom', 'kcal/mol/Ang', 'kcal/mol/A', 'kcal/mol/bohr', 'kcal/mol/au', 'kcal/mol/a.u.', 'kcal/mol/m', 'cm^-1/Angstrom', 'cm^-1/Ang', 'cm^-1/A', 'cm^-1/bohr', 'cm^-1/au', 'cm^-1/a.u.', 'cm^-1/m', 'cm-1/Angstrom', 'cm-1/Ang', 'cm-1/A', 'cm-1/bohr', 'cm-1/au', 'cm-1/a.u.', 'cm-1/m', 'K/Angstrom', 'K/Ang', 'K/A', 'K/bohr', 'K/au', 'K/a.u.', 'K/m', 'au', 'a.u.']
Hessian = Literal['au/Angstrom^2', 'au/Ang^2', 'au/A^2', 'au/bohr^2', 'au/au^2', 'au/a.u.^2', 'au/m^2', 'a.u./Angstrom^2', 'a.u./Ang^2', 'a.u./A^2', 'a.u./bohr^2', 'a.u./au^2', 'a.u./a.u.^2', 'a.u./m^2', 'Hartree/Angstrom^2', 'Hartree/Ang^2', 'Hartree/A^2', 'Hartree/bohr^2', 'Hartree/au^2', 'Hartree/a.u.^2', 'Hartree/m^2', 'Ha/Angstrom^2', 'Ha/Ang^2', 'Ha/A^2', 'Ha/bohr^2', 'Ha/au^2', 'Ha/a.u.^2', 'Ha/m^2', 'eV/Angstrom^2', 'eV/Ang^2', 'eV/A^2', 'eV/bohr^2', 'eV/au^2', 'eV/a.u.^2', 'eV/m^2', 'kJ/mol/Angstrom^2', 'kJ/mol/Ang^2', 'kJ/mol/A^2', 'kJ/mol/bohr^2', 'kJ/mol/au^2', 'kJ/mol/a.u.^2', 'kJ/mol/m^2', 'J/Angstrom^2', 'J/Ang^2', 'J/A^2', 'J/bohr^2', 'J/au^2', 'J/a.u.^2', 'J/m^2', 'kcal/mol/Angstrom^2', 'kcal/mol/Ang^2', 'kcal/mol/A^2', 'kcal/mol/bohr^2', 'kcal/mol/au^2', 'kcal/mol/a.u.^2', 'kcal/mol/m^2', 'cm^-1/Angstrom^2', 'cm^-1/Ang^2', 'cm^-1/A^2', 'cm^-1/bohr^2', 'cm^-1/au^2', 'cm^-1/a.u.^2', 'cm^-1/m^2', 'cm-1/Angstrom^2', 'cm-1/Ang^2', 'cm-1/A^2', 'cm-1/bohr^2', 'cm-1/au^2', 'cm-1/a.u.^2', 'cm-1/m^2', 'K/Angstrom^2', 'K/Ang^2', 'K/A^2', 'K/bohr^2', 'K/au^2', 'K/a.u.^2', 'K/m^2', 'au', 'a.u.']
Stress = Literal['au/Angstrom^3', 'au/Ang^3', 'au/A^3', 'au/bohr^3', 'au/au^3', 'au/a.u.^3', 'au/m^3', 'a.u./Angstrom^3', 'a.u./Ang^3', 'a.u./A^3', 'a.u./bohr^3', 'a.u./au^3', 'a.u./a.u.^3', 'a.u./m^3', 'Hartree/Angstrom^3', 'Hartree/Ang^3', 'Hartree/A^3', 'Hartree/bohr^3', 'Hartree/au^3', 'Hartree/a.u.^3', 'Hartree/m^3', 'Ha/Angstrom^3', 'Ha/Ang^3', 'Ha/A^3', 'Ha/bohr^3', 'Ha/au^3', 'Ha/a.u.^3', 'Ha/m^3', 'eV/Angstrom^3', 'eV/Ang^3', 'eV/A^3', 'eV/bohr^3', 'eV/au^3', 'eV/a.u.^3', 'eV/m^3', 'kJ/mol/Angstrom^3', 'kJ/mol/Ang^3', 'kJ/mol/A^3', 'kJ/mol/bohr^3', 'kJ/mol/au^3', 'kJ/mol/a.u.^3', 'kJ/mol/m^3', 'J/Angstrom^3', 'J/Ang^3', 'J/A^3', 'J/bohr^3', 'J/au^3', 'J/a.u.^3', 'J/m^3', 'kcal/mol/Angstrom^3', 'kcal/mol/Ang^3', 'kcal/mol/A^3', 'kcal/mol/bohr^3', 'kcal/mol/au^3', 'kcal/mol/a.u.^3', 'kcal/mol/m^3', 'cm^-1/Angstrom^3', 'cm^-1/Ang^3', 'cm^-1/A^3', 'cm^-1/bohr^3', 'cm^-1/au^3', 'cm^-1/a.u.^3', 'cm^-1/m^3', 'cm-1/Angstrom^3', 'cm-1/Ang^3', 'cm-1/A^3', 'cm-1/bohr^3', 'cm-1/au^3', 'cm-1/a.u.^3', 'cm-1/m^3', 'K/Angstrom^3', 'K/Ang^3', 'K/A^3', 'K/bohr^3', 'K/au^3', 'K/a.u.^3', 'K/m^3', 'au', 'a.u.', 'Pa', 'GPa', 'bar', 'atm']

Dicts = TypedDict('Dicts', {
    'distance': Dict[Distance, float],
    'energy': Dict[Energy, float],
    'angle': Dict[Angle, float],
    'dipole': Dict[Dipole, float],
    'reciprocal distance': Dict[RecDistance, float],
    'forces': Dict[Forces, float],
    'hessian': Dict[Hessian, float],
    'stress': Dict[Stress, float],
})

ST = TypeVar("ST", bound=str)
T = TypeVar("T", bound=Union[float, np.generic, None, str, Iterable[Any]])

class Units:
    constants: Dict[Constants, float]
    distance: Dict[Distance, float]
    energy: Dict[Energy, float]
    angle: Dict[Angle, float]
    dipole: Dict[Dipole, float]
    rec_distance: Dict[RecDistance, float]
    forces: Dict[Forces, float]
    hessian: Dict[Hessian, float]
    stress: Dict[Stress, float]
    dicts: Dicts
    @classmethod
    def find_unit(cls, unit: ST) -> Dict[str, ST]: ...
    @classmethod
    def conversion_ratio(cls, inp: str, out: str) -> float: ...
    @classmethod
    def convert(cls, value: T, inp: str, out: str) -> T: ...
