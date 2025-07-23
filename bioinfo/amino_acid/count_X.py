# Range is using python/number/num_range

def count_x(aa_seq):
    x_ranges = []
    this_range = None
    for ofst, a in enumerate(aa_seq):
        if a != 'X':
            if this_range:
                x_ranges.append(this_range)
            this_range = None
            continue

        if not this_range:
            this_range = Range(ofst + 1, ofst + 1)
            continue

        if this_range:
            this_range.stop = ofst + 1

    if this_range:
        x_ranges.append(this_range)

    return x_ranges
