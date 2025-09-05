import json

def dump_json(file_path, obj):
    with open(file_path, 'w') as fd:
        json.dump(obj, fd, indent=4, ensure_ascii=False)
