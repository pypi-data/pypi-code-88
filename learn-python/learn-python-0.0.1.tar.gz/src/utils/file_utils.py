import os


def get_path():
    config_path = os.environ.get("APP_CONFIG")
    return config_path if config_path else os.path.expanduser("~/.app/config_file")
