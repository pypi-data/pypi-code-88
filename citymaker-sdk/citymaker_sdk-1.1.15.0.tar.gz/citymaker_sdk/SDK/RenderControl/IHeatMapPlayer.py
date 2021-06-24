#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"alpha":{"t":"double","v":0,
"F":"gs"},"autoRepeat":{"t":"bool","v":False,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IHeatMapPlayer","F":"g"}}
class IHeatMapPlayer:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._alpha=args.get("alpha")
		self._autoRepeat=args.get("autoRepeat")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def continue_(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'continue', 0, state)


	def getColor(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getColor', 1, state)


	def pause(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'pause', 0, state)


	def setColor(self,arg0,arg1):  # 先定义函数 
		args = {
				"colors":{"t": "<S>","v": arg0},
				"colorCount":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setColor', 1, state)


	def setTime(self,arg0):  # 先定义函数 
		args = {
				"curTime":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setTime', 1, state)


	def startPlay(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"startTime":{"t": "S","v": arg0},
				"endTime":{"t": "S","v": arg1},
				"duration":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'startPlay', 1, state)


	def stop(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'stop', 0, state)

	@property
	def alpha(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["alpha"]

	@alpha.setter
	def alpha(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "alpha", val)
		args = {}
		args["alpha"] = PropsTypeData.get("alpha")
		args["alpha"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"alpha", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"alpha",JsonData)

	@property
	def autoRepeat(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["autoRepeat"]

	@autoRepeat.setter
	def autoRepeat(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "autoRepeat", val)
		args = {}
		args["autoRepeat"] = PropsTypeData.get("autoRepeat")
		args["autoRepeat"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"autoRepeat", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"autoRepeat",JsonData)

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
