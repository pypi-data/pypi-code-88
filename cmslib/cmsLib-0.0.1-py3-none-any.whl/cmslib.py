
import yaml
import os

class HelloClass():

    def say_hello(self):
        return "hello world"


class Yaml_Server_Access:

    def CheckWhichPathExists(self, pathDict = None):
        ''' Identifies which path exists fot the YAML config file '''
        pathDict = pathDict or {
            "path1": r"C:\Users\ryderp\Documents\projects\vendorportalconnection\config.yaml",
            "path2": r"C:\Users\winshuttle3\Documents\WinShuttleAutomation\PythonCodes\config.yaml",
        }

        for path in pathDict:
            if os.path.exists(pathDict[path]):
                return pathDict[path]

        print("no Path Found")  
        return "no Path Found"

    def GetConfigFromYaml(self, listVal):
        '''
        Yaml convertor method
        Collects data from the config.yaml file. 
        '''
        if not isinstance(listVal, list): 
            raise ValueError("listVal is not a list")
        
        path = self.CheckWhichPathExists()

        with open(path, 'r') as stream:
            try:
                YamlInfo = yaml.safe_load(stream)
                dict1 =  {i:YamlInfo[i] for i in listVal}
                return dict1
            except yaml.YAMLError as exc:
                print(exc)

    def ChoosePath(self, process, name):
        '''
        Checks the path in the config and checks whether it exists or now
        process = name of processs project eg winshuttleAutomation
        name = name of path 
        '''
        paths = self.GetConfigFromYaml([process])[process]["paths"][name]
        return self.CheckWhichPathExists(pathDict =paths)



    def SelectConfigByName(self, configWord = None, IsApath = False ):
        path = self.CheckWhichPathExists()
        if path == r"C:\Users\winshuttle3\Documents\WinShuttleAutomation\PythonCodes\config.yaml":
            if IsApath: 
                values = self.GetConfigFromYaml(["WinshuttleAutomation"])["WinshuttleAutomation"]["paths"][configWord]["dev"]
            else:
                values = self.GetConfigFromYaml(["WinshuttleAutomation"])["WinshuttleAutomation"][configWord]["dev"]
            return values
        else:
            if IsApath: 
                values = self.GetConfigFromYaml(["WinshuttleAutomation"])["WinshuttleAutomation"]["paths"][configWord]["prod"]
            else:
                values = self.GetConfigFromYaml(["WinshuttleAutomation"])["WinshuttleAutomation"][configWord]["prod"]
            return values

    def IfInProd(self):
        ''' 
            Check if we are in a dev or prod  environment
        '''
        path = self.CheckWhichPathExists()
        if path == r"C:\Users\winshuttle3\Documents\WinShuttleAutomation\PythonCodes\config.yaml":
            # we are in a dev environment so dont run winshuttle
            return False
        return True
        
        





