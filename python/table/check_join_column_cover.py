

def check_join_column_cover(table1, col1, table2, col2):
    value1 = [
        row[col1]
        for row in table1
    ]

    value1 = set(value1)

    value2 = [
        row[col2]
        for row in table2
    ]

    value2 = set(value2)

    return value1 - value2, value2 - value1
