#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"border":{"t":"bool","v":False,
"F":"g"},"location":{"t":"ILine","v":None,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITopoDirectedEdge","F":"g"}}
class ITopoDirectedEdge:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._border=args.get("border")
		self._location=args.get("location")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def equal(self,arg0):  # 先定义函数 
		args = {
				"x":{"t": "ITopoDirectedEdge","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'equal', 1, state)


	def getFacet(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getFacet', 1, state)


	def getTopoNode(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getTopoNode', 1, state)


	def next(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'next', 1, state)


	def notEqual(self,arg0):  # 先定义函数 
		args = {
				"x":{"t": "ITopoDirectedEdge","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'notEqual', 1, state)


	def opposite(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'opposite', 1, state)


	def prev(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'prev', 1, state)

	@property
	def border(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["border"]

	@property
	def location(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"location",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"location",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "location", res)
		return PropsValueData["location"]

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
