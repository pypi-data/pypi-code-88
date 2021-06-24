#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
from SDK.FdeGeometry.ICoordinateTransformer import ICoordinateTransformer
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IPolynomialTransformer","F":"g"}}
class IPolynomialTransformer(ICoordinateTransformer):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

	def getCoefficient(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getCoefficient', 1, state)


	def getInverseCoefficient(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'getInverseCoefficient', 1, state)


	def setCoefficient(self,arg0,arg1):  # 先定义函数 
		args = {
				"xArray":{"t": "IDoubleArray","v": arg0},
				"yArray":{"t": "IDoubleArray","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setCoefficient', 1, state)


	def setInverseCoefficient(self,arg0,arg1):  # 先定义函数 
		args = {
				"xCoef":{"t": "IDoubleArray","v": arg0},
				"yCoef":{"t": "IDoubleArray","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setInverseCoefficient', 1, state)


	def setMatchingPointPairs(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"srcArray":{"t": "IDoubleArray","v": arg0},
				"dstArray":{"t": "IDoubleArray","v": arg1},
				"degree":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'setMatchingPointPairs', 1, state)

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
