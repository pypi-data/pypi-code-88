#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"conflict":{"t":"IConflict","v":None,
"F":"g"},"onReplicationStatusChanged":{"t":"Dispatch","v":"",
"F":"s"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IReplication","F":"g"}}
class IReplication:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

		#CM.AddRenderEventCB(Events)
		#CM.AddRenderEvent(this, Events)

	def initParam(self,args):
		self.conflict=args.get("conflict")
		self.onReplicationStatusChanged=args.get("onReplicationStatusChanged")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def mergeFrom(self,arg0,arg1):  # 先定义函数 
		args = {
				"source":{"t": "IFeatureDataSet","v": arg0},
				"truncate":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'mergeFrom', 0, state)


	def mergeTo(self,arg0,arg1):  # 先定义函数 
		args = {
				"destination":{"t": "IFeatureDataSet","v": arg0},
				"truncate":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'mergeTo', 0, state)


	def setStepValue(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "N","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setStepValue', 0, state)

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
				super(IReplication, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
