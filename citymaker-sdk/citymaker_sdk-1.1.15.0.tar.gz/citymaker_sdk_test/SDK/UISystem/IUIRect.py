#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
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
		self.bottom=args.get("bottom")
		self.height=args.get("height")
		self.left=args.get("left")
		self.right=args.get("right")
		self.top=args.get("top")
		self.width=args.get("width")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

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
				super(IUIRect, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
