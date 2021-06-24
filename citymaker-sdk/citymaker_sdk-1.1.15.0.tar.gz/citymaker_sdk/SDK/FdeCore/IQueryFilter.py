#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"filterType":{"t":"gviFilterType","v":1,
"F":"g"},"idsFilter":{"t":"int []","v":"",
"F":"gs"},"resultBeginIndex":{"t":"int","v":-1,
"F":"gs"},"resultLimit":{"t":"int","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IQueryFilter","F":"g"}}
#Events = {postfixClause:{fn:null}prefixClause:{fn:null}subFields:{fn:null}tables:{fn:null}whereClause:{fn:null}}
class IQueryFilter:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._filterType=args.get("filterType")
		self._idsFilter=args.get("idsFilter")
		self._resultBeginIndex=args.get("resultBeginIndex")
		self._resultLimit=args.get("resultLimit")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def addSubField(self,arg0):  # 先定义函数 
		args = {
				"subField":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'addSubField', 0, state)

	@property
	def filterType(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["filterType"]

	@property
	def idsFilter(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["idsFilter"]

	@idsFilter.setter
	def idsFilter(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "idsFilter", val)
		args = {}
		args["idsFilter"] = PropsTypeData.get("idsFilter")
		args["idsFilter"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"idsFilter", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"idsFilter",JsonData)

	@property
	def resultBeginIndex(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["resultBeginIndex"]

	@resultBeginIndex.setter
	def resultBeginIndex(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "resultBeginIndex", val)
		args = {}
		args["resultBeginIndex"] = PropsTypeData.get("resultBeginIndex")
		args["resultBeginIndex"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"resultBeginIndex", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"resultBeginIndex",JsonData)

	@property
	def resultLimit(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		return PropsValueData["resultLimit"]

	@resultLimit.setter
	def resultLimit(self,val):
		PropsTypeData =  glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		CM.addPropsValue(PropsValueData.get("_HashCode"), "resultLimit", val)
		args = {}
		args["resultLimit"] = PropsTypeData.get("resultLimit")
		args["resultLimit"]["v"] = val
		JsonData = CM.setJsonData("set_",PropsValueData.get("_HashCode"),"resultLimit", args)
		wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"resultLimit",JsonData)

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
