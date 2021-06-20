"""
Logging utility

Example:
    LOGGER = logger.get_logger('example')
"""
import logging
from typing import Any


def get_logger(class_name: str) -> Any:
    """
    Creates logger object for package modules

    Args:
        class_name (str): name of class/file

    Return:
        logger (obj): Logger object instance
    """
    logger = logging.getLogger(class_name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)

    return logger
