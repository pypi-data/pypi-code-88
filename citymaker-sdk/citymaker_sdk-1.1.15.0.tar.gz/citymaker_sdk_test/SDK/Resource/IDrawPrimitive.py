#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"BakedTexcoordArray":{"t":"IFloatArray","v":"",
"F":"gs"},"ColorArray":{"t":"IUInt32Array","v":"",
"F":"gs"},"ElementCount":{"t":"int","v":0,
"F":"g"},"IndexArray":{"t":"IUInt16Array","v":"",
"F":"gs"},"IsEncrypted":{"t":"bool","v":False,
"F":"g"},"Material":{"t":"IDrawMaterial","v":None,
"F":"gs"},"NormalArray":{"t":"IFloatArray","v":"",
"F":"gs"},"PrimitiveMode":{"t":"gviPrimitiveMode","v":0,
"F":"gs"},"PrimitiveType":{"t":"gviPrimitiveType","v":0,
"F":"gs"},"TexcoordArray":{"t":"IFloatArray","v":"",
"F":"gs"},"VertexArray":{"t":"IFloatArray","v":"",
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDrawPrimitive","F":"g"}}
class IDrawPrimitive:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.BakedTexcoordArray=args.get("BakedTexcoordArray")
		self.ColorArray=args.get("ColorArray")
		self.ElementCount=args.get("ElementCount")
		self.IndexArray=args.get("IndexArray")
		self.IsEncrypted=args.get("IsEncrypted")
		self.Material=args.get("Material")
		self.NormalArray=args.get("NormalArray")
		self.PrimitiveMode=args.get("PrimitiveMode")
		self.PrimitiveType=args.get("PrimitiveType")
		self.TexcoordArray=args.get("TexcoordArray")
		self.VertexArray=args.get("VertexArray")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def encrypt(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'encrypt', 0, state)

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
				super(IDrawPrimitive, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
