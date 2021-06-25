import json
from functools import reduce
import operator

def getFromDict(dataDict, mapList):
    return reduce(operator.getitem, mapList, dataDict)

def setInDict(fileName,mapList, value,indent):
    if indent == 0:
        indent = None
    mapList = mapList.split('.')
    dataDict = json.load(open(fileName,'r'))
    getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value
    writePath = open(fileName,'w')
    json.dump(dataDict,writePath,indent=indent)

def delInDict(fileName,mapList,indent):
    if indent == 0:
        indent = None
    mapList = mapList.split('.')
    dataDict = json.load(open(fileName,'r'))
    del getFromDict(dataDict, mapList[:-1])[mapList[-1]]
    writePath = open(fileName,'w')
    if mapList == "All":
        writePath.write("{}")
    json.dump(dataDict,writePath,indent=indent)

def appendInDict(fileName,mapList, value,indent):
    if indent == 0:
        indent = None
    mapList = mapList.split('.')
    dataDict = json.load(open(fileName,'r'))
    if type(reduce(operator.getitem, mapList, dataDict)) is list:
        getFromDict(dataDict, mapList[:-1])[mapList[-1]].append(value)
    else:
        getFromDict(dataDict, mapList[:-1])[mapList[-1]] = value
    writePath = open(fileName,'w')
    json.dump(dataDict,writePath,indent=indent)

def getDict(fileName):
    return json.load(open(fileName,'r'))

