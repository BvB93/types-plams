from typing import List

from scm.plams.core.basejob import (
    Job as Job,
    SingleJob as SingleJob,
    MultiJob as MultiJob,
)
from scm.plams.core.errors import (
    PlamsError as PlamsError,
    FileError as FileError,
    ResultsError as ResultsError,
    JobError as JobError,
    PTError as PTError,
    UnitsError as UnitsError,
    MoleculeError as MoleculeError,
)
from scm.plams.core.functions import (
    init as init,
    finish as finish,
    log as log,
    load as load,
    load_all as load_all,
    delete_job as delete_job,
    add_to_class as add_to_class,
    add_to_instance as add_to_instance,
    config as config,
    read_molecules as read_molecules,
)
from scm.plams.core.jobmanager import JobManager as JobManager
from scm.plams.core.jobrunner import (
    JobRunner as JobRunner,
    GridRunner as GridRunner,
)
from scm.plams.core.results import Results as Results
from scm.plams.core.settings import Settings as Settings

from scm.plams.mol.atom import Atom as Atom
from scm.plams.mol.bond import Bond as Bond
from scm.plams.mol.molecule import Molecule as Molecule
from scm.plams.mol.pdbtools import (
    PDBRecord as PDBRecord,
    PDBHandler as PDBHandler,
)

from scm.plams.interfaces.adfsuite.ams import (
    AMSJob as AMSJob,
    AMSResults as AMSResults,
)
from scm.plams.interfaces.molecule.ase import (
    fromASE as fromASE,
    toASE as toASE,
)
from scm.plams.interfaces.molecule.rdkit import (
    add_Hs as add_Hs,
    apply_reaction_smarts as apply_reaction_smarts,
    apply_template as apply_template,
    gen_coords_rdmol as gen_coords_rdmol,
    get_backbone_atoms as get_backbone_atoms,
    modify_atom as modify_atom,
    to_rdmol as to_rdmol,
    from_rdmol as from_rdmol,
    from_sequence as from_sequence,
    from_smiles as from_smiles,
    from_smarts as from_smarts,
    partition_protein as partition_protein,
    readpdb as readpdb,
    writepdb as writepdb,
    get_substructure as get_substructure,
    get_conformations as get_conformations,
    yield_coords as yield_coords,
)

from scm.plams.tools.units import Units
from scm.plams.tools.periodictable import (
    PeriodicTable as PeriodicTable,
    PT as PT,
)
from scm.plams.tools.kftools import (
    KFReader as KFReader,
    KFFile as KFFile,
    KFHistory as KFHistory,
)

__all__: List[str]
__version__: str
