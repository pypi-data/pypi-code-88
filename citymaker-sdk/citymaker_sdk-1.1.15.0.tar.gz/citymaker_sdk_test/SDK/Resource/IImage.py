#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"FrameInterval":{"t":"int","v":1000,
"F":"gs"},"FrameNumber":{"t":"int","v":0,
"F":"g"},"HasAlpha":{"t":"bool","v":False,
"F":"g"},"Height":{"t":"int","v":0,
"F":"g"},"ImageFormat":{"t":"gviImageFormat","v":0,
"F":"g"},"ImageType":{"t":"gviImageType","v":0,
"F":"g"},"IsEncrypted":{"t":"bool","v":False,
"F":"g"},"width":{"t":"int","v":0,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IImage","F":"g"}}
class IImage:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.FrameInterval=args.get("FrameInterval")
		self.FrameNumber=args.get("FrameNumber")
		self.HasAlpha=args.get("HasAlpha")
		self.Height=args.get("Height")
		self.ImageFormat=args.get("ImageFormat")
		self.ImageType=args.get("ImageType")
		self.IsEncrypted=args.get("IsEncrypted")
		self.width=args.get("width")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def asBinary(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'AsBinary', 1, state)


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
		return CM.AddPrototype(self,args, 'WriteFile', 1, state)

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
				super(IImage, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
