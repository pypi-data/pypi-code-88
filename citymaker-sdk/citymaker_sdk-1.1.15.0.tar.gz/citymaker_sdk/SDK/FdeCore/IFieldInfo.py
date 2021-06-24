#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
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
		self._customData=args.get("customData")
		self._domain=args.get("domain")
		self._domainFixed=args.get("domainFixed")
		self._editable=args.get("editable")
		self._fieldType=args.get("fieldType")
		self._geometryDef=args.get("geometryDef")
		self._isSystemField=args.get("isSystemField")
		self._length=args.get("length")
		self._nullable=args.get("nullable")
		self._precision=args.get("precision")
		self._registeredRenderIndex=args.get("registeredRenderIndex")
		self._required=args.get("required")
		self._scale=args.get("scale")
		self._supportRenderField=args.get("supportRenderField")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

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

	@property
	def customData(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"customData",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"customData",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "customData", res)
		return PropsValueData["customData"]

	@customData.setter
	def customData(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "customData", val)
		args = {}
		args["customData"] = PropsTypeData.get("customData")
		args["customData"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"customData", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"customData",JsonData)

	@property
	def domain(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"domain",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"domain",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "domain", res)
		return PropsValueData["domain"]

	@domain.setter
	def domain(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "domain", val)
		args = {}
		args["domain"] = PropsTypeData.get("domain")
		args["domain"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"domain", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"domain",JsonData)

	@property
	def domainFixed(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["domainFixed"]

	@property
	def editable(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["editable"]

	@editable.setter
	def editable(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "editable", val)
		args = {}
		args["editable"] = PropsTypeData.get("editable")
		args["editable"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"editable", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"editable",JsonData)

	@property
	def fieldType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["fieldType"]

	@fieldType.setter
	def fieldType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "fieldType", val)
		args = {}
		args["fieldType"] = PropsTypeData.get("fieldType")
		args["fieldType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"fieldType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"fieldType",JsonData)

	@property
	def geometryDef(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"geometryDef",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"geometryDef",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "geometryDef", res)
		return PropsValueData["geometryDef"]

	@geometryDef.setter
	def geometryDef(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "geometryDef", val)
		args = {}
		args["geometryDef"] = PropsTypeData.get("geometryDef")
		args["geometryDef"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"geometryDef", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"geometryDef",JsonData)

	@property
	def isSystemField(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["isSystemField"]

	@property
	def length(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["length"]

	@length.setter
	def length(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "length", val)
		args = {}
		args["length"] = PropsTypeData.get("length")
		args["length"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"length", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"length",JsonData)

	@property
	def nullable(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["nullable"]

	@nullable.setter
	def nullable(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "nullable", val)
		args = {}
		args["nullable"] = PropsTypeData.get("nullable")
		args["nullable"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"nullable", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"nullable",JsonData)

	@property
	def precision(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["precision"]

	@precision.setter
	def precision(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "precision", val)
		args = {}
		args["precision"] = PropsTypeData.get("precision")
		args["precision"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"precision", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"precision",JsonData)

	@property
	def registeredRenderIndex(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["registeredRenderIndex"]

	@registeredRenderIndex.setter
	def registeredRenderIndex(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "registeredRenderIndex", val)
		args = {}
		args["registeredRenderIndex"] = PropsTypeData.get("registeredRenderIndex")
		args["registeredRenderIndex"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"registeredRenderIndex", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"registeredRenderIndex",JsonData)

	@property
	def required(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["required"]

	@required.setter
	def required(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "required", val)
		args = {}
		args["required"] = PropsTypeData.get("required")
		args["required"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"required", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"required",JsonData)

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
	def supportRenderField(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["supportRenderField"]

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
