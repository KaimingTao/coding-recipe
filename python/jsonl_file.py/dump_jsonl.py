import json


def dump_jsonl(jsonl_file_path, table):
    with open(jsonl_file_path, 'w', encoding='utf-8') as jsonl_file:
        for row in table:
            json_line = json.dumps(row, ensure_ascii=False)
            jsonl_file.write(json_line + '\n')


