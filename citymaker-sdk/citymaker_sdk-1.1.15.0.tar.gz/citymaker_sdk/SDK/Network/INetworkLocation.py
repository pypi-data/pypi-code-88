#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
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
		self._networkPosition=args.get("networkPosition")
		self._position=args.get("position")
		self._type=args.get("type")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

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

	@property
	def networkPosition(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"networkPosition",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"networkPosition",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "networkPosition", res)
		return PropsValueData["networkPosition"]

	@property
	def position(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"position",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"position",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "position", res)
		return PropsValueData["position"]

	@position.setter
	def position(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "position", val)
		args = {}
		args["position"] = PropsTypeData.get("position")
		args["position"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"position", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"position",JsonData)

	@property
	def type(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["type"]

	@property
	def propertyType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["propertyType"]

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
