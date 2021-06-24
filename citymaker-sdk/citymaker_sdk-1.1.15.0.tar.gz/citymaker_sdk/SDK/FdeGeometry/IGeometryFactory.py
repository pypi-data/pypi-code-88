#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IGeometryFactory","F":"g"}}
class IGeometryFactory:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def createFromBinary(self,arg0):  # 先定义函数 
		args = {
				"binaryBuffer":{"t": "IBinaryBuffer","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createFromBinary', 1, state)


	def createFromWKT(self,arg0):  # 先定义函数 
		args = {
				"wKT":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createFromWKT', 1, state)


	def createGeometry(self,arg0,arg1):  # 先定义函数 
		args = {
				"geometryType":{"t": "gviGeometryType","v": arg0},
				"vertexAttribute":{"t": "gviVertexAttribute","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createGeometry', 1, state)


	def geometryCreate(self,arg0):  # 先定义函数 
		args = {
				"createType":{"t": "gviGeometryType","v": arg0}
		}
		state = "new"
		CM.AddPrototype(self,args, 'geometryCreate', 0, state)


	def createPoint(self,arg0):  # 先定义函数 
		args = {
				"vertexAttribute":{"t": "gviVertexAttribute","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createPoint', 1, state)

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
