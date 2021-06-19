import os

import yaml

from src.exceptions import ConfigError


class Config:
    CONFIG_PATH_ENVIRONMENT_VARIABLE = "CONFIG_FILE_PATH"
    __instance = None

    def __init__(self):
        config_path = os.getenv(Config.CONFIG_PATH_ENVIRONMENT_VARIABLE)
        if config_path is None:
            raise ConfigError(f"environment variable: {Config.CONFIG_PATH_ENVIRONMENT_VARIABLE} not set")
        try:
            with open(config_path, "r") as input_file:
                self.__yaml_config = yaml.safe_load(input_file)
        except FileNotFoundError:
            raise ConfigError(f"failed to locate config file at: {config_path}")
        if self.__yaml_config is None:
            raise ConfigError("failed to parse config yaml")
        pass

    @staticmethod
    def initialize_instance():
        Config.__instance = Config()

    @staticmethod
    def get():
        return Config.__instance

    def __getattr__(self, attribute_name):
        attribute_value = self.__yaml_config.get(attribute_name, None)
        if attribute_value is not None:
            return attribute_value
        else:
            raise ConfigError(f"unknown attribute: {attribute_name}, ensure key exists in config yaml")


Config.initialize_instance()
