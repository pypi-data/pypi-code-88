#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"networkPosition":{"t":"IPoint","v":None,
"F":"g"},"position":{"t":"IPoint","v":None,
"F":"gs"},"type":{"t":"gviNetworkLocationType","v":1,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"INetworkLocation","F":"g"}}
#Events = {name:{fn:null}}
class INetworkLocation:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.networkPosition=args.get("networkPosition")
		self.position=args.get("position")
		self.type=args.get("type")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)


	def getCost(self,arg0):  # 先定义函数 
		args = {
				"impedance":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getCost', 1, state)


	def getEarlistArriveCost(self,arg0):  # 先定义函数 
		args = {
				"impedance":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getEarlistArriveCost', 1, state)


	def getLatestArriveCost(self,arg0):  # 先定义函数 
		args = {
				"impedance":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getLatestArriveCost', 1, state)


	def setCost(self,arg0,arg1):  # 先定义函数 
		args = {
				"impedance":{"t": "S","v": arg0},
				"newVal":{"t": "O","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setCost', 0, state)


	def setEarlistArriveCost(self,arg0,arg1):  # 先定义函数 
		args = {
				"impedance":{"t": "S","v": arg0},
				"newVal":{"t": "O","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setEarlistArriveCost', 0, state)


	def setLatestArriveCost(self,arg0,arg1):  # 先定义函数 
		args = {
				"impedance":{"t": "S","v": arg0},
				"newVal":{"t": "O","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setLatestArriveCost', 0, state)

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
				super(INetworkLocation, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
