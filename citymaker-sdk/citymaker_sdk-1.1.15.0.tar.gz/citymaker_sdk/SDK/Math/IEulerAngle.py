#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"heading":{"t":"double","v":0,
"F":"gs"},"roll":{"t":"double","v":0,
"F":"gs"},"tilt":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IEulerAngle","F":"g"}}
class IEulerAngle:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._heading=args.get("heading")
		self._roll=args.get("roll")
		self._tilt=args.get("tilt")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)


	def set(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"heading":{"t": "N","v": arg0},
				"tilt":{"t": "N","v": arg1},
				"roll":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'set', 0, state)


	def setByEulerAngle(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IEulerAngle","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setByEulerAngle', 0, state)


	def valid(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'valid', 1, state)

	@property
	def heading(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["heading"]

	@heading.setter
	def heading(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "heading", val)
		args = {}
		args["heading"] = PropsTypeData.get("heading")
		args["heading"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"heading", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"heading",JsonData)

	@property
	def roll(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["roll"]

	@roll.setter
	def roll(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "roll", val)
		args = {}
		args["roll"] = PropsTypeData.get("roll")
		args["roll"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"roll", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"roll",JsonData)

	@property
	def tilt(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["tilt"]

	@tilt.setter
	def tilt(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "tilt", val)
		args = {}
		args["tilt"] = PropsTypeData.get("tilt")
		args["tilt"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"tilt", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"tilt",JsonData)

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
