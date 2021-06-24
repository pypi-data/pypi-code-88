#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"bottom":{"t":"IUIDim","v":None,
"F":"g"},"height":{"t":"IUIDim","v":None,
"F":"gs"},"left":{"t":"IUIDim","v":None,
"F":"g"},"right":{"t":"IUIDim","v":None,
"F":"g"},"top":{"t":"IUIDim","v":None,
"F":"g"},"width":{"t":"IUIDim","v":None,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IUIRect","F":"g"}}
class IUIRect:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._bottom=args.get("bottom")
		self._height=args.get("height")
		self._left=args.get("left")
		self._right=args.get("right")
		self._top=args.get("top")
		self._width=args.get("width")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getPosition(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getPosition', 1, state)


	def getSize(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getSize', 1, state)


	def init(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"left":{"t": "IUIDim","v": arg0},
				"top":{"t": "IUIDim","v": arg1},
				"right":{"t": "IUIDim","v": arg2},
				"bottom":{"t": "IUIDim","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'init', 0, state)


	def setPosition(self,arg0,arg1):  # 先定义函数 
		args = {
				"left":{"t": "IUIDim","v": arg0},
				"top":{"t": "IUIDim","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setPosition', 0, state)


	def setSize(self,arg0,arg1):  # 先定义函数 
		args = {
				"width":{"t": "IUIDim","v": arg0},
				"height":{"t": "IUIDim","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setSize', 0, state)

	@property
	def bottom(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"bottom",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"bottom",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "bottom", res)
		return PropsValueData["bottom"]

	@property
	def height(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"height",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"height",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "height", res)
		return PropsValueData["height"]

	@height.setter
	def height(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "height", val)
		args = {}
		args["height"] = PropsTypeData.get("height")
		args["height"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"height", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"height",JsonData)

	@property
	def left(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"left",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"left",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "left", res)
		return PropsValueData["left"]

	@property
	def right(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"right",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"right",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "right", res)
		return PropsValueData["right"]

	@property
	def top(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"top",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"top",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "top", res)
		return PropsValueData["top"]

	@property
	def width(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"width",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"width",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "width", res)
		return PropsValueData["width"]

	@width.setter
	def width(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "width", val)
		args = {}
		args["width"] = PropsTypeData.get("width")
		args["width"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"width", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"width",JsonData)

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
