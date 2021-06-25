"""ExiDB is a package that maybe help you at your database basically it NOSQL
based on JSON it have Query that can find you the thing that you need by search by it name"""

from .tool import *
from jsonpath import JSONPath

class ExiDB:
    def __init__(self,filepath,indent=0) -> None:
        self.filepath = filepath
        self.indent = indent

    def insert(self,mapList:str,value) -> None:
        "That will insert the value inside the JSON file"
        setInDict(self.filepath,mapList,value,self.indent)

    def edit(self,mapList:str,value) -> None:
        "That will edit the value inside the JSON file"
        setInDict(self.filepath,mapList,value,self.indent)
    
    def append(self,mapList,value) -> None:
        appendInDict(self.filepath,mapList,value,self.indent)

    def delete(self,mapList:str) -> None:
        "That will delete the value inside the JSON file"
        delInDict(self.filepath,mapList,self.indent)

    def purge(self) -> None:
        "That will purge all the JSON file"
        delInDict(self.filepath,"All",self.indent)

    def get(self,mapList:str):
        "That will return DATA"
        return getFromDict(self.filepath,mapList)

class QueryDB:
    def __init__(self,filepath):
        self.filepath = filepath

    def search(self,mapList):
        myDict = getDict("test.json")
        print(JSONPath(f"$..{mapList}").parse(myDict))
