import json
from dacite import from_dict
from colorama import init, Fore
init(autoreset=True)

# Custom imports
from .models.config_data import ConfigData

class ConfigCredentialsReader():
    config_data = None

    def __init__(self):
        self.__parse_config()

    def __parse_config(self, debug: bool=False) -> ConfigData:
        """ Parses config file with credentials to typed model """
        with open('c:/config/config.credentials.json') as json_file:
            config_data_dict = json.load(json_file)

            # Parse python data dict to typed config model ~ https://github.com/konradhalas/dacite
            self.config_data = from_dict(
                data_class=ConfigData, 
                data=config_data_dict
            )

            # Prints to output
            if debug:
                print(Fore.CYAN + "Parsed config_data")
                print(self.config_data)