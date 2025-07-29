import csv
from pathlib import Path

def load_csv(file_path, encoding='utf-8-sig'):
    file_path = Path(file_path).resolve()

    table = []

    with open(file_path, encoding=encoding) as fd:
        for record in csv.DictReader(fd, delimiter='\t'):
            table.append(record)

    return table
