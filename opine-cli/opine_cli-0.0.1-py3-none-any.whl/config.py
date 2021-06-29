import json
import os.path

class Config(object):

    def list(self):
        config_utils = ConfigUtils()
        config_raw = config_utils.get()
        if type(config_raw) == dict:
            config_data = json.dumps(config_raw, indent=2, sort_keys=True)
            print(config_data)
        else:
            print(config_raw)
            
                
    def set(self, key, value):
        config_utils = ConfigUtils()
        config_utils.set(key, value)


class ConfigUtils():
    def __init__(self):
        self._config_path = os.path.expanduser("~") + '/opine_cli.cfg'
        self.default_endpoint = "https://api.opine.world"

    def get(self):
        if os.path.isfile(self._config_path) == False:
            return "No config file found. Run the command 'opine init'"
        else:
            file = open(self._config_path,)
            json_data = json.load(file)            
            file.close()
            return json_data
        
    def set(self, key, value):
        config_data = {}
        if not key or not value:
            print("KEY and/or VALUE cannot be empty.")
            print()
            return
        # read configs
        if os.path.isfile(self._config_path) == True:
            file = open(self._config_path,)
            config_data = json.load(file)
            file.close()

        config_data[key] = value
        jsondata = json.dumps(config_data, indent=2, sort_keys=True)
        # write all configs back to file
        file = open(self._config_path, "w")
        file.write(jsondata)
        file.close()
        return jsondata

    def remove(self, key):
        # read configs
        if os.path.isfile(self._config_path) == True:
            file = open(self._config_path,)
            config_data = json.load(file)
            file.close()
        if key in config_data:
            del config_data[key]
            jsondata = json.dumps(config_data, indent=2, sort_keys=True)
            # write all configs back to file
            file = open(self._config_path, "w")
            file.write(jsondata)
            file.close()
            return jsondata

    def set_default_api_endpoint(self):
        self.set("api_endpoint", "https://api.opine.world")
        
