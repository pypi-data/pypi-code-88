#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"BeginCirculatorEdgeAround":{"t":"int","v":0,
"F":"g"},"Degree":{"t":"int","v":0,
"F":"g"},"Location":{"t":"IPolygon","v":None,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ITopoFacet","F":"g"}}
class ITopoFacet:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.BeginCirculatorEdgeAround=args.get("BeginCirculatorEdgeAround")
		self.Degree=args.get("Degree")
		self.Location=args.get("Location")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def circulatorNext(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'CirculatorNext', 1, state)


	def equal(self,arg0):  # 先定义函数 
		args = {
				"x":{"t": "ITopoFacet","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Equal', 1, state)


	def getEdge(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'GetEdge', 1, state)


	def locateEdge(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'LocateEdge', 1, state)


	def locateTopoNode(self,arg0):  # 先定义函数 
		args = {
				"index":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'LocateTopoNode', 1, state)


	def next(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'Next', 1, state)


	def notEqual(self,arg0):  # 先定义函数 
		args = {
				"x":{"t": "ITopoFacet","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'NotEqual', 1, state)

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
				super(ITopoFacet, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
