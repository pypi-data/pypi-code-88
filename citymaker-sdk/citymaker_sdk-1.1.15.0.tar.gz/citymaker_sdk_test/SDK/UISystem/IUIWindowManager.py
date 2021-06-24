#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"uiRootWindow":{"t":"IUIWindow","v":None,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IUIWindowManager","F":"g"}}
class IUIWindowManager:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.uiRootWindow=args.get("uiRootWindow")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def createImageButton(self,arg0,arg1,arg2,arg3,arg4,arg5,arg6):  # 先定义函数 
		args={}
		state=""
		if type(arg0) in [int,float] and type(arg1) in [int,float] and type(arg2) in [int,float] and type(arg3) in [int,float] and (type(arg4) in [int,float] or type(arg4) is str) and (type(arg5) in [int,float] or type(arg5) is str) and (type(arg6) in [int,float] or type(arg6) is str):
			args={
				"left":{"t": "N","v": arg0},
				"top":{"t": "N","v": arg1},
				"width":{"t": "N","v": arg2},
				"height":{"t": "N","v": arg3},
				"normalImg":{"t": "S","v": arg4},
				"pushedImg":{"t": "S","v": arg5},
				"hoverImg":{"t": "S","v": arg6}
			}
			state="new"
		else:
			pass
		args={
		
					}
		return CM.AddPrototype(self,args, 'createImageButton', 1, state)


	def createImageFromFile(self,arg0):  # 先定义函数 
		args = {
				"imageFileName":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createImageFromFile', 1, state)


	def createImageFromMemory(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"binaryBuffer":{"t": "IBinaryBuffer","v": arg0},
				"imageWidth":{"t": "N","v": arg1},
				"imageHeight":{"t": "N","v": arg2}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createImageFromMemory', 1, state)


	def createStaticImage(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args={}
		state=""
		if type(arg0) in [int,float] and type(arg1) in [int,float] and type(arg2) in [int,float] and type(arg3) in [int,float] and (type(arg4) in [int,float] or type(arg4) is str) and (type(arg5)  is bool or arg5 == 1 or arg5 == 0):
			args={
				"left":{"t": "N","v": arg0},
				"top":{"t": "N","v": arg1},
				"width":{"t": "N","v": arg2},
				"height":{"t": "N","v": arg3},
				"imgName":{"t": "S","v": arg4},
				"flag":{"t": "B","v": arg5}
			}
			state="new"
		else:
			pass
		args={
		
					}
		return CM.AddPrototype(self,args, 'createStaticImage', 1, state)


	def createStaticLabel(self,arg0,arg1,arg2,arg3,arg4,arg5):  # 先定义函数 
		args={}
		state=""
		if type(arg0) in [int,float] and type(arg1) in [int,float] and type(arg2) in [int,float] and (type(arg3) in [int,float] or type(arg3) is str) and (type(arg4) in [int,float] or type(arg4) is str) and (type(arg5)  is bool or arg5 == 1 or arg5 == 0):
			args={
				"left":{"t": "N","v": arg0},
				"top":{"t": "N","v": arg1},
				"font":{"t": "N","v": arg2},
				"text":{"t": "S","v": arg3},
				"color":{"t": "S","v": arg4},
				"flag":{"t": "B","v": arg5}
			}
			state="new"
		else:
			pass
		args={
		
					}
		return CM.AddPrototype(self,args, 'createStaticLabel', 1, state)


	def createTextButton(self,arg0,arg1,arg2,arg3,arg4):  # 先定义函数 
		args={}
		state=""
		if type(arg0) in [int,float] and type(arg1) in [int,float] and type(arg2) in [int,float] and type(arg3) in [int,float] and (type(arg4) in [int,float] or type(arg4) is str):
			args={
				"left":{"t": "N","v": arg0},
				"top":{"t": "N","v": arg1},
				"width":{"t": "N","v": arg2},
				"height":{"t": "N","v": arg3},
				"text":{"t": "S","v": arg4}
			}
			state="new"
		else:
			pass
		args={
		
					}
		return CM.AddPrototype(self,args, 'createTextButton', 1, state)


	def createUIFont(self,arg0,arg1):  # 先定义函数 
		args = {
				"fontSize":{"t": "N","v": arg0},
				"fontFilePath":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createUIFont', 1, state)


	def deleteImage(self,arg0):  # 先定义函数 
		args = {
				"imageGuid":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteImage', 0, state)


	def deleteUIFont(self,arg0):  # 先定义函数 
		args = {
				"fontGuid":{"t": "S","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteUIFont', 0, state)


	def destroyAllWindows(self,):  # 先定义函数 
		args = {}
		state = ""
		CM.AddPrototype(self,args, 'destroyAllWindows', 0, state)


	def destroyWindow(self,arg0):  # 先定义函数 
		args = {
				"windowToDel":{"t": "IUIWindow","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'destroyWindow', 0, state)

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
				super(IUIWindowManager, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
