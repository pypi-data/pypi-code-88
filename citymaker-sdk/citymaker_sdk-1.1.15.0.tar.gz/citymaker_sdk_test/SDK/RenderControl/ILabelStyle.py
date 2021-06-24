#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"backgroundColor":{"t":"Color","v":"",
"F":"gs"},"bold":{"t":"bool","v":False,
"F":"gs"},"fontSize":{"t":"int","v":12,
"F":"gs"},"iconColor":{"t":"Color","v":"",
"F":"gs"},"italic":{"t":"bool","v":False,
"F":"gs"},"limitScreenSize":{"t":"bool","v":True,
"F":"gs"},"lineColor":{"t":"Color","v":"",
"F":"gs"},"lineLength":{"t":"double","v":0.0,
"F":"gs"},"lineToGround":{"t":"gviLineToGroundType","v":0,
"F":"gs"},"lockMode":{"t":"gviLockMode","v":0,
"F":"gs"},"maxImageSize":{"t":"int","v":-1,
"F":"gs"},"maxViewingHeight":{"t":"double","v":1000,
"F":"gs"},"minViewingHeight":{"t":"double","v":0,
"F":"gs"},"multilineJustification":{"t":"gviMultilineJustification","v":1,
"F":"gs"},"pivotAlignment":{"t":"gviPivotAlignment","v":1,
"F":"gs"},"scale":{"t":"double","v":1.0,
"F":"gs"},"showTextBehavior":{"t":"gviShowTextOptions","v":0,
"F":"gs"},"textColor":{"t":"Color","v":"",
"F":"gs"},"textOnImage":{"t":"bool","v":False,
"F":"gs"},"underline":{"t":"bool","v":False,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ILabelStyle","F":"g"}}
#Events = {fontName:{fn:null}frameFileName:{fn:null}textAlignment:{fn:null}}
class ILabelStyle:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.backgroundColor=args.get("backgroundColor")
		self.bold=args.get("bold")
		self.fontSize=args.get("fontSize")
		self.iconColor=args.get("iconColor")
		self.italic=args.get("italic")
		self.limitScreenSize=args.get("limitScreenSize")
		self.lineColor=args.get("lineColor")
		self.lineLength=args.get("lineLength")
		self.lineToGround=args.get("lineToGround")
		self.lockMode=args.get("lockMode")
		self.maxImageSize=args.get("maxImageSize")
		self.maxViewingHeight=args.get("maxViewingHeight")
		self.minViewingHeight=args.get("minViewingHeight")
		self.multilineJustification=args.get("multilineJustification")
		self.pivotAlignment=args.get("pivotAlignment")
		self.scale=args.get("scale")
		self.showTextBehavior=args.get("showTextBehavior")
		self.textColor=args.get("textColor")
		self.textOnImage=args.get("textOnImage")
		self.underline=args.get("underline")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")
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
				super(ILabelStyle, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
