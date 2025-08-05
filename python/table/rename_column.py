
def rename_column(table, col_name, new_col_name):
    [
        row.update({new_col_name: row[col_name] or ''})
        for row in table
    ]

    for row in table:
        del row[col_name]

    return table
