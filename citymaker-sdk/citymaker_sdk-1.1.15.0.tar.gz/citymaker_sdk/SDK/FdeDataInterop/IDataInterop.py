#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"connectionType":{"t":"gviDataConnectionType","v":0,
"F":"g"},"layersInfo":{"t":"ILayerInfoCollection","v":None,
"F":"g"},"properties":{"t":"IPropertySet","v":0,
"F":"g"},"stepValue":{"t":"int","v":False,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDataInterop","F":"g"}}
#Events = {connectionString:{fn:null}}
class IDataInterop:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

		#CM.AddRenderEventCB(Events)
		#CM.AddRenderEvent(this, Events)

	def initParam(self,args):
		self._connectionType=args.get("connectionType")
		self._layersInfo=args.get("layersInfo")
		self._properties=args.get("properties")
		self._stepValue=args.get("stepValue")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def exportLayer(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"oC":{"t": "IObjectClass","v": arg0},
				"filter":{"t": "IQueryFilter","v": arg1},
				"geoName":{"t": "S","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'exportLayer', 1, state)


	def exportLayers(self,arg0,arg1):  # 先定义函数 
		args = {
				"fDS":{"t": "IFeatureDataSet","v": arg0},
				"classNames":{"t": "<S>","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'exportLayers', 1, state)


	def getCount(self,arg0):  # 先定义函数 
		args = {
				"filter":{"t": "IQueryFilter","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getCount', 1, state)


	def importLayer(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"oC":{"t": "IObjectClass","v": arg0},
				"geoName":{"t": "S","v": arg1},
				"fields":{"t": "IPropertySet","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'importLayer', 1, state)


	def importLayers(self,arg0,arg1):  # 先定义函数 
		args = {
				"fDS":{"t": "IFeatureDataSet","v": arg0},
				"layers":{"t": "IPropertySet","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'importLayers', 1, state)


	def search(self,arg0,arg1):  # 先定义函数 
		args = {
				"filter":{"t": "IQueryFilter","v": arg0},
				"reuseRow":{"t": "B","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'search', 1, state)

	@property
	def connectionType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["connectionType"]

	@property
	def layersInfo(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"layersInfo",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"layersInfo",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "layersInfo", res)
		return PropsValueData["layersInfo"]

	@property
	def properties(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"properties",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"properties",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "properties", res)
		return PropsValueData["properties"]

	@property
	def stepValue(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["stepValue"]

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
