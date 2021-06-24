#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.RenderControl.IRenderable import IRenderable
Props={"renderParams":{"t":"IPropertySet","v":None,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"I3DTileLayer","F":"g"}}
#Events = {connectionInfo:{fn:null}password:{fn:null}}
class I3DTileLayer(IRenderable):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.renderParams=args.get("renderParams")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def setTileLayerRenderParams(self,arg0,arg1):  # 先定义函数 
		args = {
				"value":{"t": "S","v": arg0},
				"type":{"t": "gviSetTileLayerRenderParams","v": arg1}
		}
		state = "new"
		CM.AddPrototype(self,args, 'setTileLayerRenderParams', 0, state)


	def getTileLayerRenderParams(self,arg0):  # 先定义函数 
		args = {
				"type":{"t": "gviSetTileLayerRenderParams","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'GetTileLayerRenderParams', 1, state)


	def addPolygonHole(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"fdeValue":{"t": "IPolygon","v": arg0},
				"isModifyZ":{"t": "B","v": arg1},
				"featherRadius":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addPolygonHole', 1, state)


	def clearAllPolygonHole(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clearAllPolygonHole', 0, state)


	def getHoles(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getHoles', 1, state)


	def getModifiers(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getModifiers', 1, state)


	def getPolygonHoleFeatherRadius(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getPolygonHoleFeatherRadius', 1, state)


	def getPolygonHoleGeometry(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getPolygonHoleGeometry', 1, state)


	def getPolygonHoleModifyZStatus(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getPolygonHoleModifyZStatus', 1, state)


	def getPolygonHoleNumber(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getPolygonHoleNumber', 1, state)


	def getPolygonHoleParam(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getPolygonHoleParam', 1, state)


	def getWKT(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getWKT', 1, state)


	def polylineIntersect(self,arg0):  # 先定义函数 
		args = {
				"polyline":{"t": "IPolyline","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'polylineIntersect', 1, state)


	def removePolygonHole(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'removePolygonHole', 1, state)


	def setHoles(self,arg0):  # 先定义函数 
		args = {
				"region":{"t": "IMultiPolygon","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setHoles', 0, state)


	def setModifiers(self,arg0):  # 先定义函数 
		args = {
				"region":{"t": "IMultiPolygon","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setModifiers', 0, state)


	def setPolygonHoleFeatherRadius(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"featherRadius":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setPolygonHoleFeatherRadius', 1, state)


	def setPolygonHoleGeometry(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"fdeValue":{"t": "IPolygon","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setPolygonHoleGeometry', 1, state)


	def setPolygonHoleModifyZStatus(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"isModifyZ":{"t": "B","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setPolygonHoleModifyZStatus', 1, state)


	def setPolygonHoleParam(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"fdeValue":{"t": "IPolygon","v": arg1},
				"isModifyZ":{"t": "B","v": arg2},
				"featherRadius":{"t": "N","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setPolygonHoleParam', 1, state)

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
				super(I3DTileLayer, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
