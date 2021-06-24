#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"center":{"t":"IVector3","v":None,
"F":"g"},"depth":{"t":"double","v":0,
"F":"g"},"height":{"t":"double","v":0,
"F":"g"},"maxX":{"t":"double","v":0,
"F":"gs"},"maxY":{"t":"double","v":0,
"F":"gs"},"maxZ":{"t":"double","v":0,
"F":"gs"},"minX":{"t":"double","v":0,
"F":"gs"},"minY":{"t":"double","v":0,
"F":"gs"},"minZ":{"t":"double","v":0,
"F":"gs"},"width":{"t":"double","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IEnvelope","F":"g"}}
class IEnvelope:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._center=args.get("center")
		self._depth=args.get("depth")
		self._height=args.get("height")
		self._maxX=args.get("maxX")
		self._maxY=args.get("maxY")
		self._maxZ=args.get("maxZ")
		self._minX=args.get("minX")
		self._minY=args.get("minY")
		self._minZ=args.get("minZ")
		self._width=args.get("width")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)


	def contain(self,arg0):  # 先定义函数 
		args = {
				"val":{"t": "IVector3","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'contain', 1, state)


	def expandByEnvelope(self,arg0):  # 先定义函数 
		args = {
				"val":{"t": "IEnvelope","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'expandByEnvelope', 0, state)


	def expandByVector(self,arg0):  # 先定义函数 
		args = {
				"val":{"t": "IVector3","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'expandByVector', 0, state)


	def intersect(self,arg0):  # 先定义函数 
		args = {
				"envelope":{"t": "IEnvelope","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'intersect', 1, state)


	def isIntersect(self,arg0):  # 先定义函数 
		args = {
				"envelope":{"t": "IEnvelope","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'isIntersect', 1, state)


	def set(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"minX":{"t": "N","v": arg0},
				"maxX":{"t": "N","v": arg1},
				"minY":{"t": "N","v": arg2},
				"maxY":{"t": "N","v": arg3},
				"minZ":{"t": "N","v": arg4},
				"maxZ":{"t": "N","v": arg5}
		}
		state = ""
		CM.AddPrototype(self,args, 'set', 0, state)


	def setByEnvelope(self,arg0):  # 先定义函数 
		args = {
				"val":{"t": "IEnvelope","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setByEnvelope', 0, state)


	def valid(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'valid', 1, state)

	@property
	def center(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"center",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"center",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "center", res)
		return PropsValueData["center"]

	@property
	def depth(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["depth"]

	@property
	def height(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["height"]

	@property
	def maxX(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxX"]

	@maxX.setter
	def maxX(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxX", val)
		args = {}
		args["maxX"] = PropsTypeData.get("maxX")
		args["maxX"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxX", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxX",JsonData)

	@property
	def maxY(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxY"]

	@maxY.setter
	def maxY(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxY", val)
		args = {}
		args["maxY"] = PropsTypeData.get("maxY")
		args["maxY"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxY", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxY",JsonData)

	@property
	def maxZ(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["maxZ"]

	@maxZ.setter
	def maxZ(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "maxZ", val)
		args = {}
		args["maxZ"] = PropsTypeData.get("maxZ")
		args["maxZ"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"maxZ", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"maxZ",JsonData)

	@property
	def minX(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minX"]

	@minX.setter
	def minX(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minX", val)
		args = {}
		args["minX"] = PropsTypeData.get("minX")
		args["minX"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minX", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minX",JsonData)

	@property
	def minY(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minY"]

	@minY.setter
	def minY(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minY", val)
		args = {}
		args["minY"] = PropsTypeData.get("minY")
		args["minY"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minY", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minY",JsonData)

	@property
	def minZ(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["minZ"]

	@minZ.setter
	def minZ(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "minZ", val)
		args = {}
		args["minZ"] = PropsTypeData.get("minZ")
		args["minZ"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"minZ", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"minZ",JsonData)

	@property
	def width(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["width"]

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
