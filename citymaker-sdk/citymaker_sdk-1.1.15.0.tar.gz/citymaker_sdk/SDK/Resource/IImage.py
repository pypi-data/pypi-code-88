#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"frameInterval":{"t":"int","v":1000,
"F":"gs"},"frameNumber":{"t":"int","v":0,
"F":"g"},"hasAlpha":{"t":"bool","v":False,
"F":"g"},"height":{"t":"int","v":0,
"F":"g"},"imageFormat":{"t":"gviImageFormat","v":0,
"F":"g"},"imageType":{"t":"gviImageType","v":0,
"F":"g"},"isEncrypted":{"t":"bool","v":False,
"F":"g"},"width":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IImage","F":"g"}}
class IImage:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._frameInterval=args.get("frameInterval")
		self._frameNumber=args.get("frameNumber")
		self._hasAlpha=args.get("hasAlpha")
		self._height=args.get("height")
		self._imageFormat=args.get("imageFormat")
		self._imageType=args.get("imageType")
		self._isEncrypted=args.get("isEncrypted")
		self._width=args.get("width")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def asBinary(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'asBinary', 1, state)


	def compare(self,arg0):  # 先定义函数 
		args = {
				"otherImage":{"t": "IImage","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'compare', 1, state)


	def convertFormat(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "gviImageFormat","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'convertFormat', 0, state)


	def downSize(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'downSize', 0, state)


	def embedWatermark(self,arg0):  # 先定义函数 
		args = {
				"watermark":{"t": "IImage","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'embedWatermark', 0, state)


	def encrypt(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'encrypt', 0, state)


	def flip(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'flip', 0, state)


	def writeFile(self,arg0):  # 先定义函数 
		args = {
				"imageFile":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'writeFile', 1, state)

	@property
	def frameInterval(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["frameInterval"]

	@frameInterval.setter
	def frameInterval(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "frameInterval", val)
		args = {}
		args["frameInterval"] = PropsTypeData.get("frameInterval")
		args["frameInterval"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"frameInterval", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"frameInterval",JsonData)

	@property
	def frameNumber(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["frameNumber"]

	@property
	def hasAlpha(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["hasAlpha"]

	@property
	def height(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["height"]

	@property
	def imageFormat(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["imageFormat"]

	@property
	def imageType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["imageType"]

	@property
	def isEncrypted(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isEncrypted"]

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
