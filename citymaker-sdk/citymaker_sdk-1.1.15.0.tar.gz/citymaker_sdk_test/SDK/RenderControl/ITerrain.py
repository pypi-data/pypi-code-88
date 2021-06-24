#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.RenderControl.IRObject import IRObject
Props={"demAvailable":{"t":"bool","v":True,
"F":"gs"},"enableAtmosphere":{"t":"bool","v":False,
"F":"gs"},"enableOceanEffect":{"t":"bool","v":True,
"F":"gs"},"isPlanarTerrain":{"t":"bool","v":True,
"F":"g"},"isRegistered":{"t":"bool","v":False,
"F":"g"},"oceanWindDirection":{"t":"double","v":0,
"F":"gs"},"oceanWindSpeed":{"t":"double","v":0,
"F":"gs"},"opacity":{"t":"double","v":1,
"F":"gs"},"supportAtmosphere":{"t":"bool","v":False,
"F":"g"},"visibleMask":{"t":"gviViewportMask","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITerrain","F":"g"}}
#Events = {connectInfo:{fn:null}crsWKT:{fn:null}}
class ITerrain(IRObject):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.demAvailable=args.get("demAvailable")
		self.enableAtmosphere=args.get("enableAtmosphere")
		self.enableOceanEffect=args.get("enableOceanEffect")
		self.isPlanarTerrain=args.get("isPlanarTerrain")
		self.isRegistered=args.get("isRegistered")
		self.oceanWindDirection=args.get("oceanWindDirection")
		self.oceanWindSpeed=args.get("oceanWindSpeed")
		self.opacity=args.get("opacity")
		self.supportAtmosphere=args.get("supportAtmosphere")
		self.visibleMask=args.get("visibleMask")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def findBestPath(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7):  # 先定义函数 
		args = {
				"startX":{"t": "N","v": arg0},
				"startY":{"t": "N","v": arg1},
				"endX":{"t": "N","v": arg2},
				"endY":{"t": "N","v": arg3},
				"sampleNumber":{"t": "N","v": arg4},
				"searchAreaFactor":{"t": "N","v": arg5},
				"maxClimbSlope":{"t": "N","v": arg6},
				"maxDescentSlope":{"t": "N","v": arg7}
		}
		state = ""
		return CM.AddPrototype(self,args, 'findBestPath', 1, state)


	def flyTo(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "gviTerrainActionCode","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'flyTo', 0, state)


	def getElevation(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"x":{"t": "N","v": arg0},
				"y":{"t": "N","v": arg1},
				"getAltitudeType":{"t": "gviGetElevationType","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getElevation', 1, state)


	def getInvisibleRegion(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getInvisibleRegion', 1, state)


	def getOceanRegion(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getOceanRegion', 1, state)


	def getSlope(self,arg0,arg1):  # 先定义函数 
		args = {
				"x":{"t": "N","v": arg0},
				"y":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSlope', 1, state)


	def registerTerrain(self,arg0,arg1):  # 先定义函数 
		args = {
				"layerInfo":{"t": "S","v": arg0},
				"pass":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'registerTerrain', 1, state)


	def setInvisibleRegion(self,arg0):  # 先定义函数 
		args = {
				"region":{"t": "IMultiPolygon","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setInvisibleRegion', 0, state)


	def setOceanRegion(self,arg0):  # 先定义函数 
		args = {
				"region":{"t": "IMultiPolygon","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setOceanRegion', 0, state)


	def unregisterTerrain(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'unregisterTerrain', 0, state)

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
				super(ITerrain, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
