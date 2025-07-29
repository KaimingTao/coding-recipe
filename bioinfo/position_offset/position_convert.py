def aa_pos_to_codon_start(aa_pos):
    aa_ofst = aa_pos - 1
    na_ofst = aa_ofst * 3

    return na_ofst * 3 + 1


def aa_pos_to_codon_range(aa_pos):
    aa_ofst = aa_pos - 1
    na_ofst = aa_ofst * 3
    return range(
        na_ofst + 1,
        na_ofst + 4
    )


def na_pos_to_aa_pos(na_pos):

    na_ofst = na_pos - 1
    aa_ofst = na_ofst // 3

    return aa_ofst + 1


def na_pos_to_codon_start(na_pos):
    pass


def na_pos_to_codon_range(na_pos):
    aa_pos = na_pos_to_aa_pos(na_pos)
    return aa_pos_to_codon_range(aa_pos)


def test():
    