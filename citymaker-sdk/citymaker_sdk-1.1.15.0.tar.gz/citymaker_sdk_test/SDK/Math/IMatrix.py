#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"HasMirror":{"t":"bool","v":False,
"F":"g"},"HasShear":{"t":"bool","v":False,
"F":"g"},"IsIdentity":{"t":"bool","v":False,
"F":"g"},"M11":{"t":"double","v":0,
"F":"gs"},"M12":{"t":"double","v":0,
"F":"gs"},"M13":{"t":"double","v":0,
"F":"gs"},"M14":{"t":"double","v":0,
"F":"gs"},"M21":{"t":"double","v":0,
"F":"gs"},"M22":{"t":"double","v":0,
"F":"gs"},"M23":{"t":"double","v":0,
"F":"gs"},"M24":{"t":"double","v":0,
"F":"gs"},"M31":{"t":"double","v":0,
"F":"gs"},"M32":{"t":"double","v":0,
"F":"gs"},"M33":{"t":"double","v":0,
"F":"gs"},"M34":{"t":"double","v":0,
"F":"gs"},"M41":{"t":"double","v":0,
"F":"gs"},"M42":{"t":"double","v":0,
"F":"gs"},"M43":{"t":"double","v":0,
"F":"gs"},"M44":{"t":"double","v":0,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IMatrix","F":"g"}}
class IMatrix:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.HasMirror=args.get("HasMirror")
		self.HasShear=args.get("HasShear")
		self.IsIdentity=args.get("IsIdentity")
		self.M11=args.get("M11")
		self.M12=args.get("M12")
		self.M13=args.get("M13")
		self.M14=args.get("M14")
		self.M21=args.get("M21")
		self.M22=args.get("M22")
		self.M23=args.get("M23")
		self.M24=args.get("M24")
		self.M31=args.get("M31")
		self.M32=args.get("M32")
		self.M33=args.get("M33")
		self.M34=args.get("M34")
		self.M41=args.get("M41")
		self.M42=args.get("M42")
		self.M43=args.get("M43")
		self.M44=args.get("M44")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def clone(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'Clone', 1, state)


	def compose(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"trans":{"t": "IVector3","v": arg0},
				"scale":{"t": "IVector3","v": arg1},
				"euler":{"t": "IEulerAngle","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'compose', 0, state)


	def compose2(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"trans":{"t": "IVector3","v": arg0},
				"scale":{"t": "IVector3","v": arg1},
				"rotationAngle":{"t": "N","v": arg2},
				"rotationDir":{"t": "IVector3","v": arg3},
				"shearAngle":{"t": "N","v": arg4},
				"shearDir":{"t": "IVector3","v": arg5}
		}
		state = ""
		CM.AddPrototype(self,args, 'compose2', 0, state)


	def decompose(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"trans":{"t": "IVector3","v": arg0},
				"scale":{"t": "IVector3","v": arg1},
				"euler":{"t": "IEulerAngle","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'Decompose', 1, state)


	def decompose2(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"trans":{"t": "IVector3","v": arg0},
				"scale":{"t": "IVector3","v": arg1},
				"rotationAngle":{"t": "N","v": arg2},
				"rotationDir":{"t": "IVector3","v": arg3}
		}
		state = ""
		CM.AddPrototype(self,args, 'decompose2', 0, state)


	def getRotation(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'GetRotation', 1, state)


	def getScale(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'GetScale', 1, state)


	def getTranslate(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'GetTranslate', 1, state)


	def interpolatePosition(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"mat1":{"t": "IMatrix","v": arg0},
				"velocity1":{"t": "N","v": arg1},
				"time1":{"t": "N","v": arg2},
				"mat2":{"t": "IMatrix","v": arg3},
				"velocity2":{"t": "N","v": arg4},
				"time2":{"t": "N","v": arg5},
				"time":{"t": "N","v": arg6}
		}
		state = ""
		CM.AddPrototype(self,args, 'interpolatePosition', 0, state)


	def inverse(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'inverse', 0, state)


	def makeIdentity(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'makeIdentity', 0, state)


	def multiplyVector(self,arg0,arg1):  # 先定义函数 
		args = {
				"src":{"t": "IVector3","v": arg0},
				"pVal":{"t": "IVector3","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'multiplyVector', 0, state)


	def set(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6,arg7,arg8,arg9,arg10,arg11,arg12,arg13,arg14,arg15):  # 先定义函数 
		args = {
				"a00":{"t": "N","v": arg0},
				"a01":{"t": "N","v": arg1},
				"a02":{"t": "N","v": arg2},
				"a03":{"t": "N","v": arg3},
				"a10":{"t": "N","v": arg4},
				"a11":{"t": "N","v": arg5},
				"a12":{"t": "N","v": arg6},
				"a13":{"t": "N","v": arg7},
				"a20":{"t": "N","v": arg8},
				"a21":{"t": "N","v": arg9},
				"a22":{"t": "N","v": arg10},
				"a23":{"t": "N","v": arg11},
				"a30":{"t": "N","v": arg12},
				"a31":{"t": "N","v": arg13},
				"a32":{"t": "N","v": arg14},
				"a33":{"t": "N","v": arg15}
		}
		state = ""
		CM.AddPrototype(self,args, 'set', 0, state)


	def setByMatrix(self,arg0):  # 先定义函数 
		args = {
				"val":{"t": "IMatrix","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setByMatrix', 0, state)


	def setRotation(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IEulerAngle","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setRotation', 0, state)


	def setScale(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IVector3","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setScale', 0, state)


	def setTranslate(self,arg0):  # 先定义函数 
		args = {
				"newVal":{"t": "IVector3","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'setTranslate', 0, state)


	def transpose(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'transpose', 0, state)


	def valid(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'Valid', 1, state)

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
				super(IMatrix, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
