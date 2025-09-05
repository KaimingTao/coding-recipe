import yaml

def dump_yaml(file_path, yaml_obj):
    with file_path.open('w', encoding='utf-8') as fd:
        yaml.dump(yaml_obj, fd, allow_unicode=True, default_flow_style=False)
