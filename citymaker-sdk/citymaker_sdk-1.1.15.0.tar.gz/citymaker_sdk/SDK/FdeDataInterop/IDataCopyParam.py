#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"calcTotalCount":{"t":"bool","v":False,
"F":"gs"},"domainCopyPolicy ":{"t":"gviDomainCopyPolicy","v":0,
"F":"gs"},"filter":{"t":"IQueryFilter","v":None,
"F":"gs"},"flushInterval":{"t":"int","v":0,
"F":"gs"},"keepFid":{"t":"bool","v":False,
"F":"gs"},"rebuildRenderIndexPolicy":{"t":"gviRebuildRenderIndexPolicy","v":0,
"F":"gs"},"resourceConflictPolicy":{"t":"gviResourceConflictPolicy","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IDataCopyParam","F":"g"}}
class IDataCopyParam:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

		#CM.AddRenderEventCB(Events)
		#CM.AddRenderEvent(this, Events)

	def initParam(self,args):
		self._calcTotalCount=args.get("calcTotalCount")
		self._domainCopyPolicy =args.get("domainCopyPolicy ")
		self._filter=args.get("filter")
		self._flushInterval=args.get("flushInterval")
		self._keepFid=args.get("keepFid")
		self._rebuildRenderIndexPolicy=args.get("rebuildRenderIndexPolicy")
		self._resourceConflictPolicy=args.get("resourceConflictPolicy")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getFieldMapping(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getFieldMapping', 1, state)


	def setFieldMapping(self,arg0):  # 先定义函数 
		args = {
				"fieldMapping":{"t": "IPropertySet","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setFieldMapping', 0, state)

	@property
	def calcTotalCount(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["calcTotalCount"]

	@calcTotalCount.setter
	def calcTotalCount(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "calcTotalCount", val)
		args = {}
		args["calcTotalCount"] = PropsTypeData.get("calcTotalCount")
		args["calcTotalCount"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"calcTotalCount", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"calcTotalCount",JsonData)

	@property
	def domainCopyPolicy (self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["domainCopyPolicy "]

	@domainCopyPolicy .setter
	def domainCopyPolicy (self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "domainCopyPolicy ", val)
		args = {}
		args["domainCopyPolicy "] = PropsTypeData.get("domainCopyPolicy ")
		args["domainCopyPolicy "]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"domainCopyPolicy ", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"domainCopyPolicy ",JsonData)

	@property
	def filter(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"filter",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"filter",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "filter", res)
		return PropsValueData["filter"]

	@filter.setter
	def filter(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "filter", val)
		args = {}
		args["filter"] = PropsTypeData.get("filter")
		args["filter"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"filter", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"filter",JsonData)

	@property
	def flushInterval(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["flushInterval"]

	@flushInterval.setter
	def flushInterval(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "flushInterval", val)
		args = {}
		args["flushInterval"] = PropsTypeData.get("flushInterval")
		args["flushInterval"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"flushInterval", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"flushInterval",JsonData)

	@property
	def keepFid(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["keepFid"]

	@keepFid.setter
	def keepFid(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "keepFid", val)
		args = {}
		args["keepFid"] = PropsTypeData.get("keepFid")
		args["keepFid"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"keepFid", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"keepFid",JsonData)

	@property
	def rebuildRenderIndexPolicy(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["rebuildRenderIndexPolicy"]

	@rebuildRenderIndexPolicy.setter
	def rebuildRenderIndexPolicy(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "rebuildRenderIndexPolicy", val)
		args = {}
		args["rebuildRenderIndexPolicy"] = PropsTypeData.get("rebuildRenderIndexPolicy")
		args["rebuildRenderIndexPolicy"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"rebuildRenderIndexPolicy", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"rebuildRenderIndexPolicy",JsonData)

	@property
	def resourceConflictPolicy(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["resourceConflictPolicy"]

	@resourceConflictPolicy.setter
	def resourceConflictPolicy(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "resourceConflictPolicy", val)
		args = {}
		args["resourceConflictPolicy"] = PropsTypeData.get("resourceConflictPolicy")
		args["resourceConflictPolicy"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"resourceConflictPolicy", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"resourceConflictPolicy",JsonData)

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
