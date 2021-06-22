import json
import os


class config_file_parser:
    def __init__(self,config_file_path):
        self._config_file_path = config_file_path
        self._json_entity = {}

    def check_json_is_right(self):
        if "release_mode" not in self._json_entity:
            print("error:release_mode field is miss.")
            return 1

        if "project_id" not in self._json_entity:
            print("error:project_id field is miss.")
            return 1

        if "firmware_version" not in self._json_entity:
            print("error:firmware_version field is miss.")
            return 1

        if "before_bin_file_path" not in self._json_entity:
            print("error:before_bin_file_path field is miss.")
            return 1

        if "project_path" not in self._json_entity:
            print("error:project_path field is miss.")
            return 1

        if "change_log" not in self._json_entity:
            print("error:change_log field is miss.")
            return 1

        return 0



    def parser(self):
        with open(self._config_file_path,"r") as f:
            self._json_entity = json.loads(f.read(1000000))
        
        if self.check_json_is_right() == 1:
            return 1

        return 0

    
    def get_json_data(self,key):
        return self._json_entity[key]


    def reset_release_mode(self):
        self._json_entity["release_mode"] = "False"
    

    def save_json_entity_to_file(self):
        self.reset_release_mode()
        with open(self._config_file_path,"w") as f:
            f.write(json.dumps(self._json_entity,indent = 4))
    


