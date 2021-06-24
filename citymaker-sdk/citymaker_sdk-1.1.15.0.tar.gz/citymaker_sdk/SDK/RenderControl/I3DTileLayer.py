#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
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
		self._renderParams=args.get("renderParams")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

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

	@property
	def renderParams(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"renderParams",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"renderParams",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "renderParams", res)
		return PropsValueData["renderParams"]

	@renderParams.setter
	def renderParams(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "renderParams", val)
		args = {}
		args["renderParams"] = PropsTypeData.get("renderParams")
		args["renderParams"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"renderParams", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"renderParams",JsonData)

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
