#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"envelope":{"t":"IEnvelope","v":None,
"F":"g"},"groupCount":{"t":"int","v":0,
"F":"g"},"isEmpty":{"t":"bool","v":False,
"F":"g"},"isEncrypted":{"t":"bool","v":False,
"F":"g"},"modelType":{"t":"gviModelType","v":1,
"F":"g"},"radius":{"t":"double","v":0,
"F":"g"},"singleton":{"t":"bool","v":True,
"F":"gs"},"switchSize":{"t":"int","v":0,
"F":"gs"},"totalTriangleCount":{"t":"Number","v":False,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IModel","F":"g"}}
class IModel:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._envelope=args.get("envelope")
		self._groupCount=args.get("groupCount")
		self._isEmpty=args.get("isEmpty")
		self._isEncrypted=args.get("isEncrypted")
		self._modelType=args.get("modelType")
		self._radius=args.get("radius")
		self._singleton=args.get("singleton")
		self._switchSize=args.get("switchSize")
		self._totalTriangleCount=args.get("totalTriangleCount")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addGroup(self,arg0):  # 先定义函数 
		args = {
				"drawGroup":{"t": "IDrawGroup","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'addGroup', 1, state)


	def asBinary(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asBinary', 1, state)


	def checkAndRebuild(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'checkAndRebuild', 0, state)


	def checkUp(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'checkUp', 1, state)


	def checkUpFast(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'checkUpFast', 1, state)


	def clear(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'clear', 0, state)


	def cloneAndTransform(self,arg0):  # 先定义函数 
		args = {
				"m":{"t": "IMatrix","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'cloneAndTransform', 1, state)


	def encrypt(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'encrypt', 0, state)


	def getGroup(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getGroup', 1, state)


	def getImageNames(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getImageNames', 1, state)


	def insertGroup(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"drawGroup":{"t": "IDrawGroup","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'insertGroup', 1, state)


	def multiplyMatrix(self,arg0):  # 先定义函数 
		args = {
				"m":{"t": "IMatrix","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'multiplyMatrix', 0, state)


	def removeGroup(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"count":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'removeGroup', 1, state)


	def setGroup(self,arg0,arg1):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0},
				"drawGroup":{"t": "IDrawGroup","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setGroup', 1, state)


	def valid(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'valid', 1, state)


	def writeFile(self,arg0,arg1):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"images":{"t": "IPropertySet","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'writeFile', 0, state)


	def writeFileWithMatrix(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"m":{"t": "IMatrix","v": arg1},
				"images":{"t": "IPropertySet","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'writeFileWithMatrix', 0, state)

	@property
	def envelope(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"envelope",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"envelope",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "envelope", res)
		return PropsValueData["envelope"]

	@property
	def groupCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["groupCount"]

	@property
	def isEmpty(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isEmpty"]

	@property
	def isEncrypted(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isEncrypted"]

	@property
	def modelType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["modelType"]

	@property
	def radius(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["radius"]

	@property
	def singleton(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["singleton"]

	@singleton.setter
	def singleton(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "singleton", val)
		args = {}
		args["singleton"] = PropsTypeData.get("singleton")
		args["singleton"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"singleton", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"singleton",JsonData)

	@property
	def switchSize(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["switchSize"]

	@switchSize.setter
	def switchSize(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "switchSize", val)
		args = {}
		args["switchSize"] = PropsTypeData.get("switchSize")
		args["switchSize"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"switchSize", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"switchSize",JsonData)

	@property
	def totalTriangleCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["totalTriangleCount"]

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
