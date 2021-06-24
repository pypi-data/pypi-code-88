#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
from SDK.FdeGeometry.ICirculeArc import ICirculeArc
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"CirculeArc","F":"g"}}
class CirculeArc(ICirculeArc):
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def moveModel(self,arg0):  # 先定义函数 
		args = {
				"deltaPos":{"t": "IVector3","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'MoveModel', 1, state)


	def rotateModel(self,arg0,arg1):  # 先定义函数 
		args = {
				"rotateCenter":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'RotateModel', 1, state)


	def scaleModel(self,arg0):  # 先定义函数 
		args = {
				"scaleRatio":{"t": "IVector3","v": arg0}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'ScaleModel', 1, state)


	def moveFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"deltaPos":{"t": "IVector3","v": arg0},
				"mode":{"t": "N","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'MoveFeature', 1, state)


	def rotateFeature(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"rotateCenter":{"t": "IVector3","v": arg0},
				"angle":{"t": "IEulerAngle","v": arg1},
				"mode":{"t": "N","v": arg2}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'RotateFeature', 1, state)


	def scaleFeature(self,arg0,arg1):  # 先定义函数 
		args = {
				"scaleRatio":{"t": "IVector3","v": arg0},
				"mode":{"t": "N","v": arg1}
		}
		state = "new"
		return CM.AddPrototype(self,args, 'ScaleFeature', 1, state)


	def move2D(self,arg0,arg1):  # 先定义函数 
		args = {
				"dX":{"t": "N","v": arg0},
				"dY":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'move2D', 0, state)


	def move3D(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"dX":{"t": "N","v": arg0},
				"dY":{"t": "N","v": arg1},
				"dZ":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'move3D', 0, state)


	def rotate2D(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"centerX":{"t": "N","v": arg0},
				"centerY":{"t": "N","v": arg1},
				"angle":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'rotate2D', 0, state)


	def rotate3D(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"axisX":{"t": "N","v": arg0},
				"axisY":{"t": "N","v": arg1},
				"axisZ":{"t": "N","v": arg2},
				"centerX":{"t": "N","v": arg3},
				"centerY":{"t": "N","v": arg4},
				"centerZ":{"t": "N","v": arg5},
				"angle":{"t": "N","v": arg6}
		}
		state = ""
		CM.AddPrototype(self,args, 'rotate3D', 0, state)


	def scale2D(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"scaleX":{"t": "N","v": arg0},
				"scaleY":{"t": "N","v": arg1},
				"centerX":{"t": "N","v": arg2},
				"centerY":{"t": "N","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'scale2D', 0, state)


	def scale3D(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"scaleX":{"t": "N","v": arg0},
				"scaleY":{"t": "N","v": arg1},
				"scaleZ":{"t": "N","v": arg2},
				"centerX":{"t": "N","v": arg3},
				"centerY":{"t": "N","v": arg4},
				"centerZ":{"t": "N","v": arg5}
		}
		state = ""
		CM.AddPrototype(self,args, 'scale3D', 0, state)

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
				super(CirculeArc, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
