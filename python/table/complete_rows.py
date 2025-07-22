def complete_rows(table):
    headers = get_headers_from_table(table)

    for row in table:
        for h in headers:
            if h not in row:
                row[h] = ''

    return table


def get_headers_from_table(table):

    table_headers = []

    for rec in table:
        for key in rec.keys():
            if key not in table_headers:
                table_headers.append(key)

    return table_headers
