#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IParametricModelling","F":"g"}}
class IParametricModelling:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def multiPolylineToPipeLine(self,arg0,arg1):  # 先定义函数 
		args = {
				"multiPolyline":{"t": "IMultiPolyline","v": arg0},
				"params":{"t": "IPropertySet","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'multiPolylineToPipeLine', 1, state)


	def polygonToBuilding(self,arg0,arg1):  # 先定义函数 
		args = {
				"polygon":{"t": "IPolygon","v": arg0},
				"params":{"t": "IPropertySet","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'polygonToBuilding', 1, state)


	def polylineToPipeLine(self,arg0,arg1):  # 先定义函数 
		args = {
				"polyline":{"t": "IPolyline","v": arg0},
				"params":{"t": "IPropertySet","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'polylineToPipeLine', 1, state)

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
