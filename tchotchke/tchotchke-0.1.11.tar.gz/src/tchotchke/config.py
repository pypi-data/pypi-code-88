import os

import yaml

from tchotchke.exceptions import ConfigError


class MetaConfig(type):
    CONFIG_PATH_ENVIRONMENT_VARIABLE = "CONFIG_FILE_PATH"

    def __new__(cls, name, bases, dct):
        config = super().__new__(cls, name, bases, dct)
        config_path = os.getenv(MetaConfig.CONFIG_PATH_ENVIRONMENT_VARIABLE)
        if config_path is None:
            raise ConfigError(f"environment variable: {MetaConfig.CONFIG_PATH_ENVIRONMENT_VARIABLE} not set")
        try:
            with open(config_path, "r") as input_file:
                yaml_config = yaml.safe_load(input_file)
        except FileNotFoundError:
            raise ConfigError(f"failed to locate config file at: {config_path}")
        if yaml_config is None:
            raise ConfigError("failed to parse config yaml")
        for key, value in yaml_config.items():
            setattr(config, key, value)
        return config

    def __getattr__(self, attribute_name):
        raise ConfigError(f"unknown config attribute: {attribute_name}, ensure it exists in yaml config")


class Config(metaclass=MetaConfig):
    pass
