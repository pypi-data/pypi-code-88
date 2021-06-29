import requests
import json
import getpass
from opinecli.config import ConfigUtils

class SignIn(object):
       
    def login(self):
        _config_utils = ConfigUtils()
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        config_data = _config_utils.get()
        params = {"email": username, "password": password}
        headers = {"content-type": "application/json"}
        result = requests.post(f'{config_data["api_endpoint"]}/login', json=params, headers=headers)
        if result.status_code == 200:
            print("\nLogin successful")
            _config_utils.set("user", result.json()['results'])
            # print(result.json()['results'])
        else:
            print("\nLogin failed!")

        

    def revoke(self):
        _config_utils = ConfigUtils()
        _config_utils.remove("user")
        print("Credentials and auth tokens revoked!")


    
