def row2dict(rows):
    result = []
    for row in rows:
        rec = {}
        for key in row.keys():
            rec[key] = row[key]
        result.append(rec)

    return result
