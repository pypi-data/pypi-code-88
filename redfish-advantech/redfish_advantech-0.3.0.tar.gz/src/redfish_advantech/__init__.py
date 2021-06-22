# Copyright Notice:
# Copyright 2016-2021 DMTF. All rights reserved.
# License: BSD 3-Clause License. For full text see link:
# https://github.com/chhuang789

""" Advantech Redfish restful library """

__all__ = ['restful', 'discovery']
__version__ = "0.3.0"

from redfish_advantech.restful.v1api import redfish_advantech
from redfish_advantech.discovery.discovery import discover_ssdp
import logging

def redfish_logger(file_name, log_format, log_level=logging.ERROR):
    formatter = logging.Formatter(log_format)
    fh = logging.FileHandler(file_name)
    fh.setFormatter(formatter)
    logger = logging.getLogger(__name__)
    logger.addHandler(fh)
    logger.setLevel(log_level)
    return logger
