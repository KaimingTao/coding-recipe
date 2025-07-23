def aa_pos_to_na_pos(aa_pos):
    aa_ofst = aa_pos - 1
    na_ofst = aa_ofst * 3
    return (
        na_ofst * 3 + 1,
        na_ofst * 3 + 2,
        na_ofst * 3 + 3
    )

def na_pos_to_aa_pos(na_pos):

    na_ofst = na_pos - 1
    aa_ofst = na_ofst % 3

    return aa_ofst + 1
