try:
    import yaml
except ImportError
    import ruamel.yaml
    yaml = ruamel.yaml.YAML()
