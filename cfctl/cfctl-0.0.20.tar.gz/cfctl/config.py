import os
import inspect
from pathlib import Path


from abakusbuilder import settings
from abakusbuilder.exceptions import * 

class Configuration(object):
    """
    A global configuration that can be loaded and used to read
    global settings.
    
    The configuration is loaded from abakusbuilder.settings 
    and are processed. 

    Runtime configurations are also setup here. 
    """
  
    __instance = None
    
    @staticmethod
    def getInstance():
        
        if Configuration.__instance == None:
            Configuration()
        return Configuration.__instance
    
    def __init__(self, host=None, username=None, password=None):
    
        if Configuration.__instance != None:
            raise Exception("This class is a singleton But we created a new one")
        else:
            Configuration.__instance = self
            self._host = host
            
  
if __name__ == "__main__":
    
    #c = Configuration.getInstance()
    #print(c.workspaces)


