import yaml

def load_yaml(file_path):
    with open(file_path) as fd:
        return yaml.safe_load(fd, Loader=yaml.Loader)

