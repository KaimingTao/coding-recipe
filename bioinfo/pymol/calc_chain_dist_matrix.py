import Bio.PDB
import numpy



def calc_chain_dist_matrix(chain_one, chain_two):
    """Returns a matrix of C-alpha distances between two chains"""
    answer = numpy.zeros((len(chain_one), len(chain_two)), numpy.float)
    for row, residue_one in enumerate(chain_one) :
        for col, residue_two in enumerate(chain_two) :
            answer[row, col] = calc_residue_dist(residue_one, residue_two)
    return answer



def calc_residue_dist(residue_one, residue_two) :
    """Returns the C-alpha distance between two residues"""
    # print(list(residue_one.get_atom()))
    try:
        diff_vector  = residue_one["CA"].coord - residue_two["CA"].coord
    except (AttributeError, KeyError):
        return numpy.Inf
    return numpy.sqrt(numpy.sum(diff_vector * diff_vector))


def test():
    structure = Bio.PDB.PDBParser().get_structure(pdb_code, pdb_filename)
    model = structure[0]
    dist_matrix = calc_chain_dist_matrix(model["E"], model["A"])
    contact_map = dist_matrix < 5.0
    print(contact_map)
    print("Minimum distance", numpy.min(dist_matrix))
    print("Maximum distance", numpy.max(dist_matrix))
