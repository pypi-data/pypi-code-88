#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"animationTime":{"t":"double","v":0,
"F":"gs"},"closeButtonEnabled":{"t":"bool","v":True,
"F":"gs"},"hastitle":{"t":"bool","v":False,
"F":"gs"},"hideOnClick":{"t":"bool","v":True,
"F":"gs"},"isPopupWindow":{"t":"byte","v":1,
"F":"gs"},"minButtonVisible":{"t":"bool","v":True,
"F":"gs"},"offsetX":{"t":"int","v":0,
"F":"gs"},"offsetY":{"t":"int","v":0,
"F":"gs"},"position":{"t":"gviHTMLWindowPosition","v":0,
"F":"gs"},"resizable":{"t":"bool","v":True,
"F":"gs"},"rgnTransparentColor":{"t":"uint","v":0,
"F":"gs"},"round":{"t":"int","v":-1,
"F":"gs"},"showWindow":{"t":"byte","v":0,
"F":"gs"},"sizeX":{"t":"int","v":0,
"F":"gs"},"sizeY":{"t":"int","v":0,
"F":"gs"},"topmost":{"t":"bool","v":False,
"F":"gs"},"transparence":{"t":"byte","v":255,
"F":"gs"},"winId":{"t":"int","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IWindowParam","F":"g"}}
#Events = {animation:{fn:null}filePath:{fn:null}resetOnHide:{fn:null}rgnTemplateFile:{fn:null}}
class IWindowParam:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.animationTime=args.get("animationTime")
		self.closeButtonEnabled=args.get("closeButtonEnabled")
		self.hastitle=args.get("hastitle")
		self.hideOnClick=args.get("hideOnClick")
		self.isPopupWindow=args.get("isPopupWindow")
		self.minButtonVisible=args.get("minButtonVisible")
		self.offsetX=args.get("offsetX")
		self.offsetY=args.get("offsetY")
		self.position=args.get("position")
		self.resizable=args.get("resizable")
		self.rgnTransparentColor=args.get("rgnTransparentColor")
		self.round=args.get("round")
		self.showWindow=args.get("showWindow")
		self.sizeX=args.get("sizeX")
		self.sizeY=args.get("sizeY")
		self.topmost=args.get("topmost")
		self.transparence=args.get("transparence")
		self.winId=args.get("winId")
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
				super(IWindowParam, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
