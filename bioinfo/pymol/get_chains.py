from pathlib import Path
from Bio import PDB

def get_chains(pdb_code: str, pdb_filename: Path):

    pdb_filename = pdb_filename.resolve()

    structure = PDB.PDBParser().get_structure(
        pdb_code,
        pdb_filename
    )
    print(list(structure.get_chains()))
