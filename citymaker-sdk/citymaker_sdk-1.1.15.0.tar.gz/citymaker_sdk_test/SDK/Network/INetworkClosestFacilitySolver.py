#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.Network.INetworkSolver import INetworkSolver
Props={"eventLocationCount":{"t":"int","v":0,
"F":"g"},"facilityLocationCount":{"t":"int","v":0,
"F":"g"},"routeCount":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetworkClosestFacilitySolver","F":"g"}}
class INetworkClosestFacilitySolver(INetworkSolver):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.eventLocationCount=args.get("eventLocationCount")
		self.facilityLocationCount=args.get("facilityLocationCount")
		self.routeCount=args.get("routeCount")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def addEventLocation(self,arg0):  # 先定义函数 
		args = {
				"nel":{"t": "INetworkEventLocation","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addEventLocation', 0, state)


	def addFacilityLocation(self,arg0):  # 先定义函数 
		args = {
				"nl":{"t": "INetworkLocation","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addFacilityLocation', 0, state)


	def clearEventLocations(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearEventLocations', 0, state)


	def clearFacilityLocations(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearFacilityLocations', 0, state)


	def getEventLocation(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getEventLocation', 1, state)


	def getFacilityLocation(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getFacilityLocation', 1, state)


	def getRoute(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getRoute', 1, state)


	def loadFacilityLocationFromFeatureClass(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"fc":{"t": "IFeatureClass","v": arg0},
				"queryFilter":{"t": "IQueryFilter","v": arg1},
				"geoColumnName":{"t": "S","v": arg2},
				"facilityNameColumn":{"t": "S","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'loadFacilityLocationFromFeatureClass', 0, state)

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
				super(INetworkClosestFacilitySolver, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
