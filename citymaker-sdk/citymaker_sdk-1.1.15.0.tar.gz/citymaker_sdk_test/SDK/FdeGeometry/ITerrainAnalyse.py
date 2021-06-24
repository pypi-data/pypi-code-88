#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"onProcessing":{"t":"Dispatch","v":"",
"F":"s"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITerrainAnalyse","F":"g"}}
class ITerrainAnalyse:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

		#CM.AddRenderEventCB(Events)
		#CM.AddRenderEvent(this, Events)

	def initParam(self,args):
		self.onProcessing=args.get("onProcessing")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def calculateCutFill(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"domain":{"t": "IPolygon","v": arg0},
				"tolerance":{"t": "N","v": arg1},
				"referenceHeight":{"t": "N","v": arg2},
				"cutPolygon":{"t": "IMultiPolygon","v": arg3},
				"fillPolygon":{"t": "IMultiPolygon","v": arg4},
				"cutVolume":{"t": "N","v": arg5},
				"fillVolume":{"t": "N","v": arg6}
		}
		state = ""
		CM.AddPrototype(self,args, 'calculateCutFill', 0, state)


	def estimateLandslideVolumeEx(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"modelHill":{"t": "IModel","v": arg0},
				"modelSlope":{"t": "IModel","v": arg1},
				"resolution":{"t": "N","v": arg2},
				"volume":{"t": "N","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'estimateLandslideVolumeEx', 1, state)


	def findWaterSinkBoundary(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"domain":{"t": "IPolygon","v": arg0},
				"tolerance":{"t": "N","v": arg1},
				"waterDepth":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'findWaterSinkBoundary', 1, state)


	def getSurfaceArea(self,arg0,arg1):  # 先定义函数 
		args = {
				"domain":{"t": "IPolygon","v": arg0},
				"tolerance":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getSurfaceArea', 1, state)

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
				super(ITerrainAnalyse, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
