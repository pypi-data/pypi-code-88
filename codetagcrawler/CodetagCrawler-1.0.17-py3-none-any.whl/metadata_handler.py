import yaml


def get_metadata(config_path):
    with open(config_path, 'r') as f:
        return yaml.load(f, Loader=yaml.FullLoader)

