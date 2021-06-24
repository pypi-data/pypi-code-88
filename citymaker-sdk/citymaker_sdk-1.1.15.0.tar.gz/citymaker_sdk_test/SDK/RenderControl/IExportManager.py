#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IExportManager","F":"g"}}
class IExportManager:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def cancelExport(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'cancelExport', 0, state)


	def export25D(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"box":{"t": "IEnvelope","v": arg1},
				"meterPerPixel":{"t": "N","v": arg2},
				"angle":{"t": "IEulerAngle","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'export25D', 1, state)


	def export25DEx(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"box":{"t": "IEnvelope","v": arg1},
				"meterPerPixel":{"t": "N","v": arg2},
				"angle":{"t": "IEulerAngle","v": arg3},
				"featureClassIds":{"t": "<G>","v": arg4},
				"exportShpOnly":{"t": "B","v": arg5}
		}
		state = ""
		return CM.AddPrototype(self,args, 'export25DEx', 1, state)


	def exportDEM(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"box":{"t": "IEnvelope","v": arg1},
				"meterPerPixel":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'exportDEM', 1, state)


	def exportDOM(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"box":{"t": "IEnvelope","v": arg1},
				"meterPerPixel":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'exportDOM', 1, state)


	def exportOrthoImage(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"width":{"t": "N","v": arg1},
				"center":{"t": "IPoint","v": arg2},
				"angle":{"t": "IEulerAngle","v": arg3},
				"orthoBox":{"t": "IEnvelope","v": arg4},
				"highQuality":{"t": "B","v": arg5},
				"backgroundColor":{"t": "S","v": arg6}
		}
		state = ""
		return CM.AddPrototype(self,args, 'exportOrthoImage', 1, state)


	def exportPanorama(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"width":{"t": "N","v": arg1},
				"center":{"t": "IPoint","v": arg2},
				"angle":{"t": "IEulerAngle","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'exportPanorama', 1, state)


	def exportImage(self,arg0,arg1,arg2,arg3):  # 先定义函数 
		args = {
				"filePath":{"t": "S","v": arg0},
				"w":{"t": "N","v": arg1},
				"h":{"t": "N","v": arg2},
				"highQuality":{"t": "B","v": arg3}
		}
		state = ""
		return CM.AddPrototype(self,args, 'exportImage', 1, state)

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
				super(IExportManager, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
