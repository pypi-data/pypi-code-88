#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"bakedTexcoordArray":{"t":"IFloatArray","v":"",
"F":"gs"},"colorArray":{"t":"IUInt32Array","v":"",
"F":"gs"},"elementCount":{"t":"int","v":0,
"F":"g"},"indexArray":{"t":"IUInt16Array","v":"",
"F":"gs"},"isEncrypted":{"t":"bool","v":False,
"F":"g"},"material":{"t":"IDrawMaterial","v":None,
"F":"gs"},"normalArray":{"t":"IFloatArray","v":"",
"F":"gs"},"primitiveMode":{"t":"gviPrimitiveMode","v":0,
"F":"gs"},"primitiveType":{"t":"gviPrimitiveType","v":0,
"F":"gs"},"texcoordArray":{"t":"IFloatArray","v":"",
"F":"gs"},"vertexArray":{"t":"IFloatArray","v":"",
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDrawPrimitive","F":"g"}}
class IDrawPrimitive:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._bakedTexcoordArray=args.get("bakedTexcoordArray")
		self._colorArray=args.get("colorArray")
		self._elementCount=args.get("elementCount")
		self._indexArray=args.get("indexArray")
		self._isEncrypted=args.get("isEncrypted")
		self._material=args.get("material")
		self._normalArray=args.get("normalArray")
		self._primitiveMode=args.get("primitiveMode")
		self._primitiveType=args.get("primitiveType")
		self._texcoordArray=args.get("texcoordArray")
		self._vertexArray=args.get("vertexArray")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def encrypt(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'encrypt', 0, state)

	@property
	def bakedTexcoordArray(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"bakedTexcoordArray",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"bakedTexcoordArray",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "bakedTexcoordArray", res)
		return PropsValueData["bakedTexcoordArray"]

	@bakedTexcoordArray.setter
	def bakedTexcoordArray(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "bakedTexcoordArray", val)
		args = {}
		args["bakedTexcoordArray"] = PropsTypeData.get("bakedTexcoordArray")
		args["bakedTexcoordArray"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"bakedTexcoordArray", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"bakedTexcoordArray",JsonData)

	@property
	def colorArray(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"colorArray",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"colorArray",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "colorArray", res)
		return PropsValueData["colorArray"]

	@colorArray.setter
	def colorArray(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "colorArray", val)
		args = {}
		args["colorArray"] = PropsTypeData.get("colorArray")
		args["colorArray"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"colorArray", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"colorArray",JsonData)

	@property
	def elementCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["elementCount"]

	@property
	def indexArray(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"indexArray",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"indexArray",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "indexArray", res)
		return PropsValueData["indexArray"]

	@indexArray.setter
	def indexArray(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "indexArray", val)
		args = {}
		args["indexArray"] = PropsTypeData.get("indexArray")
		args["indexArray"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"indexArray", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"indexArray",JsonData)

	@property
	def isEncrypted(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isEncrypted"]

	@property
	def material(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"material",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"material",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "material", res)
		return PropsValueData["material"]

	@material.setter
	def material(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "material", val)
		args = {}
		args["material"] = PropsTypeData.get("material")
		args["material"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"material", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"material",JsonData)

	@property
	def normalArray(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"normalArray",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"normalArray",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "normalArray", res)
		return PropsValueData["normalArray"]

	@normalArray.setter
	def normalArray(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "normalArray", val)
		args = {}
		args["normalArray"] = PropsTypeData.get("normalArray")
		args["normalArray"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"normalArray", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"normalArray",JsonData)

	@property
	def primitiveMode(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["primitiveMode"]

	@primitiveMode.setter
	def primitiveMode(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "primitiveMode", val)
		args = {}
		args["primitiveMode"] = PropsTypeData.get("primitiveMode")
		args["primitiveMode"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"primitiveMode", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"primitiveMode",JsonData)

	@property
	def primitiveType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["primitiveType"]

	@primitiveType.setter
	def primitiveType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "primitiveType", val)
		args = {}
		args["primitiveType"] = PropsTypeData.get("primitiveType")
		args["primitiveType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"primitiveType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"primitiveType",JsonData)

	@property
	def texcoordArray(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"texcoordArray",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"texcoordArray",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "texcoordArray", res)
		return PropsValueData["texcoordArray"]

	@texcoordArray.setter
	def texcoordArray(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "texcoordArray", val)
		args = {}
		args["texcoordArray"] = PropsTypeData.get("texcoordArray")
		args["texcoordArray"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"texcoordArray", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"texcoordArray",JsonData)

	@property
	def vertexArray(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"vertexArray",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"vertexArray",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "vertexArray", res)
		return PropsValueData["vertexArray"]

	@vertexArray.setter
	def vertexArray(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "vertexArray", val)
		args = {}
		args["vertexArray"] = PropsTypeData.get("vertexArray")
		args["vertexArray"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"vertexArray", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"vertexArray",JsonData)

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
