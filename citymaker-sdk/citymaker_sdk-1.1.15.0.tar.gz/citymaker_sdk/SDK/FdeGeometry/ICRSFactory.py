#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"ICRSFactory","F":"g"}}
class ICRSFactory:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def createCGCS2000(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createCGCS2000', 1, state)


	def createCRS(self,arg0):  # 先定义函数 
		args = {
				"crsType":{"t": "gviCoordinateReferenceSystemType","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createCRS', 1, state)


	def createFromWKID(self,arg0):  # 先定义函数 
		args = {
				"wKID":{"t": "N","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createFromWKID', 1, state)


	def createFromWKT(self,arg0):  # 先定义函数 
		args = {
				"wKT":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createFromWKT', 1, state)


	def createWGS84(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'createWGS84', 1, state)

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
