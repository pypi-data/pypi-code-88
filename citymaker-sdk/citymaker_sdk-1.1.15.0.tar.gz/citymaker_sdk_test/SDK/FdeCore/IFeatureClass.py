#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.FdeCore.IObjectClass import IObjectClass
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IFeatureClass","F":"g"}}
class IFeatureClass(IObjectClass):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def addRenderIndex(self,arg0):  # 先定义函数 
		args = {
				"indexInfo":{"t": "IRenderIndexInfo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addRenderIndex', 0, state)


	def addSpatialIndex(self,arg0):  # 先定义函数 
		args = {
				"indexInfo":{"t": "IIndexInfo","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addSpatialIndex', 0, state)


	def calculateDefaultGridIndex(self,arg0):  # 先定义函数 
		args = {
				"geoFieldName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'calculateDefaultGridIndex', 1, state)


	def calculateDefaultRenderIndex(self,arg0):  # 先定义函数 
		args = {
				"geoFieldName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'calculateDefaultRenderIndex', 1, state)


	def calculateExtent(self,arg0):  # 先定义函数 
		args = {
				"geoFieldName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'calculateExtent', 1, state)


	def deleteRenderIndex(self,arg0):  # 先定义函数 
		args = {
				"geoField":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteRenderIndex', 0, state)


	def deleteSpatialIndex(self,arg0):  # 先定义函数 
		args = {
				"geoField":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteSpatialIndex', 0, state)


	def getFeaturesEnvelope(self,arg0,arg1):  # 先定义函数 
		args = {
				"fidArray":{"t": "<N>","v": arg0},
				"geoField":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getFeaturesEnvelope', 1, state)


	def getRenderIndexInfos(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getRenderIndexInfos', 1, state)


	def getSpatialIndexInfos(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getSpatialIndexInfos', 1, state)


	def purgeGeometry(self,arg0):  # 先定义函数 
		args = {
				"geoFieldName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'purgeGeometry', 0, state)


	def rebuildRenderIndex(self,arg0,arg1):  # 先定义函数 
		args = {
				"geoField":{"t": "S","v": arg0},
				"rebuildType":{"t": "gviRenderIndexRebuildType","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'rebuildRenderIndex', 0, state)


	def rebuildSpatialIndex(self,arg0):  # 先定义函数 
		args = {
				"geoFieldName":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'rebuildSpatialIndex', 0, state)


	def setRenderIndexEnabled(self,arg0,arg1):  # 先定义函数 
		args = {
				"geoField":{"t": "S","v": arg0},
				"enabled":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setRenderIndexEnabled', 0, state)


	def updateExtent(self,arg0):  # 先定义函数 
		args = {
				"geoField":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'updateExtent', 0, state)

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
				super(IFeatureClass, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
