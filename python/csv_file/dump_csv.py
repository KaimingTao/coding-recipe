from pathlib import Path
import csv


def dump_csv(
        file_path, table, headers=[],
        use_all_headers=False):
    file_path = Path(file_path).resolve()

    file_path.parent.mkdir(exist_ok=True, parents=True)

    headers = resolve_headers(table, headers, use_all_headers)

    table = keep_table_columns(table, headers)

    with open(file_path, 'w', encoding='utf-8-sig') as fd:
        writer = csv.DictWriter(fd, fieldnames=headers)
        writer.writeheader()
        writer.writerows(table)


def resolve_headers(table, headers, use_all_headers=False):
    table_headers = get_headers_from_table(table)

    if not headers:
        headers = table_headers
    else:
        remain_headers = [
            i
            for i in table_headers
            if i not in headers
        ]
        if use_all_headers:
            headers = headers + remain_headers

    return headers


def get_headers_from_table(table):

    table_headers = []

    for rec in table:
        for key in rec.keys():
            if key not in table_headers:
                table_headers.append(key)

    return table_headers


def keep_table_columns(table, headers):

    return [
            {
                k: v
                for k, v in i.items()
                if k in headers
            }
            for i in table
    ]


