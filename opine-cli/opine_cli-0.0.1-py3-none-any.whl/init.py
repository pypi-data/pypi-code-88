
import json
from opinecli.config import ConfigUtils
from opinecli import auth 

class Init(object):
    def __init__(self):
        pass
    
    def start(self, endpoint="https://api.opine.world"):
        ConfigUtils().set("api_endpoint", endpoint)
        auth.SignIn().login()


    
