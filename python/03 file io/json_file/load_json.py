import json


def load_json(json_path):
    with open(json_path) as fd:
        return json.load(fd)

