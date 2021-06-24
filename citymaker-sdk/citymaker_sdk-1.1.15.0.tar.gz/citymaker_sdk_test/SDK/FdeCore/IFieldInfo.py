#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"customData":{"t":"IPropertySet","v":None,
"F":"gs"},"domain":{"t":"IDomain","v":None,
"F":"gs"},"domainFixed":{"t":"bool","v":False,
"F":"g"},"editable":{"t":"bool","v":False,
"F":"gs"},"fieldType":{"t":"gviFieldType","v":0,
"F":"gs"},"geometryDef":{"t":"IGeometryDef","v":None,
"F":"gs"},"isSystemField":{"t":"bool","v":False,
"F":"g"},"length":{"t":"int","v":0,
"F":"gs"},"nullable":{"t":"bool","v":False,
"F":"gs"},"precision":{"t":"int","v":0,
"F":"gs"},"registeredRenderIndex":{"t":"bool","v":False,
"F":"gs"},"required":{"t":"bool","v":False,
"F":"gs"},"scale":{"t":"int","v":0,
"F":"gs"},"supportRenderField":{"t":"bool","v":False,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IFieldInfo","F":"g"}}
#Events = {alias:{fn:null}defaultValue:{fn:null}name:{fn:null}}
class IFieldInfo:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.customData=args.get("customData")
		self.domain=args.get("domain")
		self.domainFixed=args.get("domainFixed")
		self.editable=args.get("editable")
		self.fieldType=args.get("fieldType")
		self.geometryDef=args.get("geometryDef")
		self.isSystemField=args.get("isSystemField")
		self.length=args.get("length")
		self.nullable=args.get("nullable")
		self.precision=args.get("precision")
		self.registeredRenderIndex=args.get("registeredRenderIndex")
		self.required=args.get("required")
		self.scale=args.get("scale")
		self.supportRenderField=args.get("supportRenderField")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'clone', 1, state)


	def equal(self,arg0):  # 先定义函数 
		args = {
				"other":{"t": "IFieldInfo","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'equal', 1, state)

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
				super(IFieldInfo, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
