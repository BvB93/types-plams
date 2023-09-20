import os
import sys
from collections.abc import Container, Generator, Iterable
from typing import IO, Any, TypeVar, overload

from rdkit import Chem
from scm.plams import Atom, Molecule

if sys.version_info >= (3, 8):
    from typing import Literal as L
else:
    from typing_extensions import Literal as L

_FT = TypeVar("_FT", str, Chem.Mol, Molecule)

def from_rdmol(rdkit_mol: Chem.Mol | Molecule, confid: int = ..., properties: bool = ...) -> Molecule: ...
def to_rdmol(
    plams_mol: Chem.Mol | Molecule, sanitize: bool = ..., properties: bool = ..., assignChirality: bool = ...
) -> Chem.Mol: ...
@overload
def from_smiles(  # type: ignore[misc]
    smiles: str, nconfs: L[1] = ..., name: None | str = ..., forcefield: L[None, "uff", "mmff"] = ..., rms: float = ...
) -> Molecule: ...
@overload
def from_smiles(
    smiles: str, nconfs: int, name: None | str = ..., forcefield: L[None, "uff", "mmff"] = ..., rms: float = ...
) -> list[Molecule]: ...
@overload
def from_smarts(  # type: ignore[misc]
    smarts: str, nconfs: L[1] = ..., name: None | str = ..., forcefield: L[None, "uff", "mmff"] = ..., rms: float = ...
) -> Molecule: ...
@overload
def from_smarts(
    smarts: str, nconfs: int, name: None | str = ..., forcefield: L[None, "uff", "mmff"] = ..., rms: float = ...
) -> list[Molecule]: ...
@overload
def get_conformations(  # type: ignore[misc]
    mol: Chem.Mol | Molecule,
    nconfs: L[1] = ...,
    name: None | str = ...,
    forcefield: L[None, "uff", "mmff"] = ...,
    rms: float = ...,
    enforceChirality: bool = ...,
) -> Molecule: ...
@overload
def get_conformations(
    mol: Chem.Mol | Molecule,
    nconfs: int,
    name: None | str = ...,
    forcefield: L[None, "uff", "mmff"] = ...,
    rms: float = ...,
    enforceChirality: bool = ...,
) -> list[Molecule]: ...
@overload
def from_sequence(  # type: ignore[misc]
    sequence: str, nconfs: L[1] = ..., name: None | str = ..., forcefield: L[None, "uff", "mmff"] = ..., rms: float = ...
) -> Molecule: ...
@overload
def from_sequence(
    sequence: str, nconfs: int, name: None | str = ..., forcefield: L[None, "uff", "mmff"] = ..., rms: float = ...
) -> list[Molecule]: ...
def calc_rmsd(mol1: Chem.Mol | Molecule, mol2: Chem.Mol | Molecule) -> float: ...
def modify_atom(mol: Chem.Mol | Molecule, idx: int, element: str) -> Molecule: ...
def apply_template(mol: Chem.Mol | Molecule, template: str) -> Molecule: ...
@overload
def apply_reaction_smarts(
    mol: Chem.Mol | Molecule,
    reaction_smarts: str,
    complete: bool = ...,
    forcefield: L[None, "uff", "mmff"] = ...,
    *,
    return_rdmol: L[False] = ...,
) -> Molecule: ...
@overload
def apply_reaction_smarts(
    mol: Chem.Mol | Molecule,
    reaction_smarts: str,
    complete: bool = ...,
    forcefield: L[None, "uff", "mmff"] = ...,
    *,
    return_rdmol: L[True],
) -> Chem.Mol: ...
def gen_coords_rdmol(rdmol: Chem.Mol) -> list[int]: ...
@overload
def readpdb(
    pdb_file: str | os.PathLike[str] | IO[str],
    removeHs: bool = ...,
    proximityBonding: bool = ...,
    *,
    return_rdmol: L[False] = ...,
) -> Molecule: ...
@overload
def readpdb(
    pdb_file: str | os.PathLike[str] | IO[str], removeHs: bool = ..., proximityBonding: bool = ..., *, return_rdmol: L[True]
) -> Chem.Mol: ...
def writepdb(mol: Chem.Mol | Molecule, pdb_file: str | os.PathLike[str] | IO[str]) -> None: ...
@overload
def add_Hs(mol: Chem.Mol | Molecule, forcefield: L[None, "uff", "mmff"] = ..., *, return_rdmol: L[False] = ...) -> Molecule: ...
@overload
def add_Hs(mol: Chem.Mol | Molecule, forcefield: L[None, "uff", "mmff"] = ..., *, return_rdmol: L[True]) -> Chem.Mol: ...
@overload
def partition_protein(
    mol: Chem.Mol | Molecule,
    residue_bonds: None | Container[tuple[int, int]] = ...,
    split_heteroatoms: bool = ...,
    *,
    return_rdmol: L[False] = ...,
) -> tuple[list[Chem.Mol], list[Chem.Mol]]: ...
@overload
def partition_protein(
    mol: Chem.Mol | Molecule,
    residue_bonds: None | Container[tuple[int, int]] = ...,
    split_heteroatoms: bool = ...,
    *,
    return_rdmol: L[True],
) -> tuple[list[Molecule], list[Molecule]]: ...
def get_backbone_atoms(mol: Chem.Mol | Molecule) -> list[int]: ...
def get_substructure(mol: Chem.Mol | Molecule, func_list: Iterable[_FT]) -> dict[_FT, list[tuple[Atom, ...]]]: ...
def yield_coords(rdmol: Chem.Mol, id: int = ...) -> Generator[tuple[float, float, float], None, None]: ...
