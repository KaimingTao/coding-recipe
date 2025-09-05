from pathlib import Path
from load_csv import load_csv
from tables2excel import tables2excel


def csv2excel(excel_file_path, csv_file_list):
    table_list = [
        {
            'name': Path(csv_file).resolve().stem,
            'table': load_csv(csv_file)
        }
        for csv_file in csv_file_list
    ]

    tables2excel(excel_file_path, table_list)
