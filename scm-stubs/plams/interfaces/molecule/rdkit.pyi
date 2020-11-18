import sys
from os import PathLike
from typing import (
    Union,
    Optional,
    Any,
    IO,
    TypeVar,
    Tuple,
    Generator,
    Dict,
    List,
    overload,
    Container,
    Iterable,
)

from rdkit.Chem import Mol
from scm.plams import Molecule, Atom

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

FT = TypeVar("FT", str, Mol, Molecule)

def from_rdmol(
    rdkit_mol: Union[Mol, Molecule], confid: int = ..., properties: bool = ...
) -> Molecule: ...
def to_rdmol(
    plams_mol: Union[Mol, Molecule],
    sanitize: bool = ...,
    properties: bool = ...,
    assignChirality: bool = ...,
) -> Mol: ...
@overload
def from_smiles(  # type: ignore[misc]
    smiles: str,
    nconfs: Literal[1] = ...,
    name: Optional[str] = ...,
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    rms: float = ...,
) -> Molecule: ...
@overload
def from_smiles(
    smiles: str,
    nconfs: int,
    name: Optional[str] = ...,
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    rms: float = ...,
) -> List[Molecule]: ...
@overload
def from_smarts(  # type: ignore[misc]
    smarts: str,
    nconfs: Literal[1] = ...,
    name: Optional[str] = ...,
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    rms: float = ...,
) -> Molecule: ...
@overload
def from_smarts(
    smarts: str,
    nconfs: int,
    name: Optional[str] = ...,
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    rms: float = ...,
) -> List[Molecule]: ...
@overload
def get_conformations(  # type: ignore[misc]
    mol: Union[Mol, Molecule],
    nconfs: Literal[1] = ...,
    name: Optional[str] = ...,
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    rms: float = ...,
    enforceChirality: bool = False,
) -> Molecule: ...
@overload
def get_conformations(
    mol: Union[Mol, Molecule],
    nconfs: int,
    name: Optional[str] = ...,
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    rms: float = ...,
    enforceChirality: bool = False,
) -> List[Molecule]: ...
@overload
def from_sequence(  # type: ignore[misc]
    sequence: str,
    nconfs: Literal[1] = ...,
    name: Optional[str] = ...,
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    rms: float = ...,
) -> Molecule: ...
@overload
def from_sequence(
    sequence: str,
    nconfs: int,
    name: Optional[str] = ...,
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    rms: float = ...,
) -> List[Molecule]: ...
def calc_rmsd(mol1: Union[Mol, Molecule], mol2: Union[Mol, Molecule]) -> float: ...
def modify_atom(mol: Union[Mol, Molecule], idx: int, element: str) -> Molecule: ...
def apply_template(mol: Union[Mol, Molecule], template: str) -> Molecule: ...
@overload
def apply_reaction_smarts(
    mol: Union[Mol, Molecule],
    reaction_smarts: str,
    complete: bool = ...,
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    return_rdmol: Literal[False] = ...,
) -> Molecule: ...
@overload
def apply_reaction_smarts(
    mol: Union[Mol, Molecule],
    reaction_smarts: str,
    complete: bool = ...,
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    return_rdmol: Literal[True] = ...,
) -> Mol: ...
def gen_coords_rdmol(rdmol: Mol) -> List[int]: ...
@overload
def readpdb(
    pdb_file: Union[str, PathLike[str], IO[str]],
    removeHs: bool = ...,
    proximityBonding: bool = ...,
    return_rdmol: Literal[False] = ...,
) -> Molecule: ...
@overload
def readpdb(
    pdb_file: Union[str, PathLike[str], IO[str]],
    removeHs: bool = ...,
    proximityBonding: bool = ...,
    return_rdmol: Literal[True] = ...,
) -> Mol: ...
def writepdb(
    mol: Union[Mol, Molecule], pdb_file: Union[str, PathLike[str], IO[str]]
) -> None: ...
@overload
def add_Hs(
    mol: Union[Mol, Molecule],
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    return_rdmol: Literal[False] = ...,
) -> Molecule: ...
@overload
def add_Hs(
    mol: Union[Mol, Molecule],
    forcefield: Optional[Literal["uff", "mff"]] = ...,
    return_rdmol: Literal[True] = ...,
) -> Mol: ...
@overload
def partition_protein(
    mol: Union[Mol, Molecule],
    residue_bonds: Optional[Container[Tuple[int, int]]] = ...,
    split_heteroatoms: bool = ...,
    return_rdmol: Literal[False] = ...,
) -> Tuple[List[Mol], List[Mol]]: ...
@overload
def partition_protein(
    mol: Union[Mol, Molecule],
    residue_bonds: Optional[Container[Tuple[int, int]]] = ...,
    split_heteroatoms: bool = ...,
    return_rdmol: Literal[True] = ...,
) -> Tuple[List[Molecule], List[Molecule]]: ...
def get_backbone_atoms(mol: Union[Mol, Molecule]) -> List[int]: ...
def get_substructure(
    mol: Union[Mol, Molecule], func_list: Iterable[FT]
) -> Dict[FT, List[Tuple[Atom, ...]]]: ...
def yield_coords(
    rdmol: Mol, id: int = ...
) -> Generator[Tuple[float, float, float], None, None]: ...
