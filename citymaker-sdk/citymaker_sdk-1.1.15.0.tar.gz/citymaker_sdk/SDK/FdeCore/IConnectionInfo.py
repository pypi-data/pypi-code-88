#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"connectionType":{"t":"gviConnectionType","v":0,
"F":"gs"},"port":{"t":"uint","v":0,
"F":"gs"},"timeout":{"t":"int","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IConnectionInfo","F":"g"}}
#Events = {database:{fn:null}instance:{fn:null}password:{fn:null}providerName:{fn:null}server:{fn:null}userName:{fn:null}version:{fn:null}}
class IConnectionInfo:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._connectionType=args.get("connectionType")
		self._port=args.get("port")
		self._timeout=args.get("timeout")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def fromConnectionString(self,arg0):  # 先定义函数 
		args = {
				"connectionString":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'fromConnectionString', 1, state)


	def getProperty(self,arg0):  # 先定义函数 
		args = {
				"name":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getProperty', 1, state)


	def setProperty(self,arg0,arg1):  # 先定义函数 
		args = {
				"key":{"t": "S","v": arg0},
				"val":{"t": "O","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setProperty', 0, state)


	def toConnectionString(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'toConnectionString', 1, state)

	@property
	def connectionType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["connectionType"]

	@connectionType.setter
	def connectionType(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "connectionType", val)
		args = {}
		args["connectionType"] = PropsTypeData.get("connectionType")
		args["connectionType"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"connectionType", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"connectionType",JsonData)

	@property
	def port(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["port"]

	@port.setter
	def port(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "port", val)
		args = {}
		args["port"] = PropsTypeData.get("port")
		args["port"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"port", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"port",JsonData)

	@property
	def timeout(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["timeout"]

	@timeout.setter
	def timeout(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "timeout", val)
		args = {}
		args["timeout"] = PropsTypeData.get("timeout")
		args["timeout"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"timeout", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"timeout",JsonData)

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
