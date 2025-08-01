import sqlite3


def run_query(db_file_path, sql_query):

    conn = sqlite3.connect(str(db_file_path))
    # Make sure the results are with table headers
    conn.row_factory = sqlite3.Row

    cursor = conn.cursor()
    cursor.execute(sql_query)

    table = []
    for row in cursor.fetchall():
        rec = {}
        for key in row.keys():
            rec[key] = row[key]
        table.append(rec)
    return table
