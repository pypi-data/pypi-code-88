#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"offset":{"t":"float","v":0,
"F":"gs"},"scale":{"t":"float","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IUIDim","F":"g"}}
class IUIDim:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._offset=args.get("offset")
		self._scale=args.get("scale")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def init(self,arg0,arg1):  # 先定义函数 
		args = {
				"scale":{"t": "N","v": arg0},
				"offset":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'init', 0, state)

	@property
	def offset(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["offset"]

	@offset.setter
	def offset(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "offset", val)
		args = {}
		args["offset"] = PropsTypeData.get("offset")
		args["offset"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"offset", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"offset",JsonData)

	@property
	def scale(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["scale"]

	@scale.setter
	def scale(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "scale", val)
		args = {}
		args["scale"] = PropsTypeData.get("scale")
		args["scale"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"scale", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"scale",JsonData)

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
