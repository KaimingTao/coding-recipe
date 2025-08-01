import sqlite3


def get_conn(db_file_path):
    # TODO: file not found

    conn = sqlite3.connect(db_file_path)
    conn.row_factory = sqlite3.Row

    return conn
