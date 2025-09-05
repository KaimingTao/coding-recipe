import json


def load_jsonl(jsonl_file_path):
    result = []
    with open(jsonl_file_path, encoding='utf-8') as jsonl_file:
        for row in jsonl_file.readlines():
            json_obj = json.loads(row)
            result.append(json_obj)

    return result
