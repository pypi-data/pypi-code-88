from dataclasses import dataclass

# Custom imports
from .config_sql import ConfigSql

@dataclass
class ConfigData:
    """ Python data model which matches 'config.credentials.json' -> semi static-typed properties. """
    slack_token: str
    bluecrest_10_10_10_30_connection: ConfigSql
    easypost_services_connection: ConfigSql