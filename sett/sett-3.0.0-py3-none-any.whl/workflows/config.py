import os

from ..core.error import UserError
from ..utils.config import create_config as _create_config, get_config_file
from ..utils.log import create_logger

logger = create_logger(__name__)


def create():
    """Creates a new default config file in the users config dir"""
    config_file = get_config_file()
    if os.path.isfile(config_file):
        raise UserError(f"The config file already exists at '{config_file}'")
    _create_config()
    logger.info("Created config file at '%s'", config_file)
