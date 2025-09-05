import sys
import csv
from pathlib import Path

def load_csv(file_path, encoding='utf-8-sig'):
    file_path = Path(file_path).resolve()

    table = []

    with open(file_path, encoding=encoding) as fd:
        for record in csv.DictReader(fd, delimiter=','):
            table.append(record)

    return table


def csv2markdown(file_path, columns):
    file_path = Path(file_path).resolve()

    md_text = []
    for row in load_csv(file_path):
        for column in columns:
            md_text.append(
                f"{column}: f{row[column]}"
            )
        md_text.append('-' * 4)

    md_path = file_path.parent / f"{file_path.stem}.md"

    with open(md_path, 'w') as fd:
        for text in md_text:
            fd.write(text)
            fd.write('\n')


if __name__ == '__main__':
    csv2markdown(sys.argv[1], sys.argv[2:])
