import logging
import os
from typing import Dict, Union, Optional

try:
    import ConfigParser as cp
except ImportError:
    import configparser as cp

log = logging.getLogger(__name__)
logging.basicConfig(filename='myapp.log', level=logging.INFO)

current_path = os.path.abspath(os.path.dirname(__file__))
filename = os.path.join(current_path, "../conf/app.cfg")

# Init ConfigParser and load --> externalize path 
config = cp.ConfigParser()
config.read(filename)


def database_config():
    url = config.get('database', 'db_url')
    username = config.get('database', 'username')
    password = config.get('database', 'password')

    log.debug("URL {}, Username {},password {}".format(url, username, "********"))

    return url, username, password


def get_section(section: str) -> Optional[Dict[str, Union[str, int, float, bool]]]:
    pass


def get_kerberos() -> None:
    pass


class ConfigParser:
    pass


"""
Implement the ConfigParser to adapt our need
"""


class MyConfig(ConfigParser):

    def read(self, filenames, encoding=None):
        super().read(filenames=filenames, encoding=encoding)
