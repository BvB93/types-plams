from scm.plams import Molecule
from ase import Atoms

def toASE(molecule: Molecule) -> Atoms: ...
def fromASE(molecule: Atoms) -> Molecule: ...
