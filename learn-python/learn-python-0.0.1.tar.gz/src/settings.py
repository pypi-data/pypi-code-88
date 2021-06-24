import logging
from src.configuration import config

CONFIG_PATH = ""
LOGGING_LEVEL = config.read("logging", "level") # logging.INFO
LOGGING_FORMAT = config.read("logging", "format")
