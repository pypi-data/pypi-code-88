#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"barrierCount":{"t":"int","v":0,
"F":"g"},"isBuildRouteLine":{"t":"bool","v":False,
"F":"gs"},"isUseHierarchy":{"t":"bool","v":False,
"F":"gs"},"locationCount":{"t":"int","v":0,
"F":"g"},"locationSearchTolerance":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetworkSolver","F":"g"}}
#Events = {hierarchyAttributeName:{fn:null}impedanceAttributeName:{fn:null}}
class INetworkSolver:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.barrierCount=args.get("barrierCount")
		self.isBuildRouteLine=args.get("isBuildRouteLine")
		self.isUseHierarchy=args.get("isUseHierarchy")
		self.locationCount=args.get("locationCount")
		self.locationSearchTolerance=args.get("locationSearchTolerance")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def addBarrier(self,arg0):  # 先定义函数 
		args = {
				"nb":{"t": "INetworkBarrier","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addBarrier', 0, state)


	def addLocation(self,arg0):  # 先定义函数 
		args = {
				"networkLocation":{"t": "INetworkLocation","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addLocation', 0, state)


	def clearBarriers(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearBarriers', 0, state)


	def clearLocations(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearLocations', 0, state)


	def getBarrier(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getBarrier', 1, state)


	def getLocation(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getLocation', 1, state)


	def getRestrictionAttributeNames(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getRestrictionAttributeNames', 1, state)


	def loadNetworkData(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'loadNetworkData', 0, state)


	def setRestrictionAttributeName(self,arg0):  # 先定义函数 
		args = {
				"attributeName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setRestrictionAttributeName', 0, state)


	def solve(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'solve', 1, state)

	def __getattr__(self,name):
		if name in Props:
			attrVal=Props[name]
			if name =="_HashCode":
				return CM.dict_get(attrVal, "v", None)
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("g") > -1:
				if CP.ClassFN.get(t) is not None and "PickResult" not in Props["propertyType"]["v"] and name != "propertyType":
					PropsTypeData = CM.getPropsTypeData(self._HashCode)
					PropsValueData = CM.getPropsValueData(self._HashCode)
					jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),name,None)
					res=socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,jsonData)
					CM.addPropsValue(PropsValueData["_HashCode"], name, res)
					return PropsValueData[name]
				else:
					PropsValueData = CM.getPropsValueData(self._HashCode)
					if name == "fullScreen":
						res=CM.isFull()
					CM.addPropsValue(PropsValueData.get("_HashCode"), name, res)
					return PropsValueData[name]

	def __setattr__(self,name,value):
		if name in Props:
			attrVal=Props[name]
			F = CM.dict_get(attrVal, "F", None)
			t = CM.dict_get(attrVal, "t", None)
			if F.find("s") > -1:
				if name =="_HashCode":
					CM.dict_set(attrVal, "F", value)
					return
				PropsTypeData = CM.getPropsTypeData(self._HashCode)
				PropsValueData = CM.getPropsValueData(self._HashCode)
				CM.addPropsValue(PropsValueData.get("_HashCode"), name, value)
				if name == "fullScreen":
					res=CM.isFull()
					return
				args = {}
				args[name] = PropsTypeData.get(name)
				args[name]["v"] = value
				JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),name, args)
				socketApi.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},name,JsonData)
				super(INetworkSolver, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
