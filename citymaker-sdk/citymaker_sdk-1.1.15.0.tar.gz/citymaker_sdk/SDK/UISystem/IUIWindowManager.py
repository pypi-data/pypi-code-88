#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.globalData as glodata
import Utils.wsInit  as wsObj 
Props={"uiRootWindow":{"t":"IUIWindow","v":None,
"F":"g"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IUIWindowManager","F":"g"}}
class IUIWindowManager:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self._uiRootWindow=args.get("uiRootWindow")
		self._HashCode=args.get("_HashCode")
		self._propertyType=args.get("propertyType")

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

	@property
	def uiRootWindow(self):
		if hasattr(self,"_HashCode") is False:
			return
		PropsTypeData = glodata.PropsTypeDataGet(self._HashCode)
		PropsValueData = glodata.PropsValueDataGet(self._HashCode)
		jsonData = CM.setJsonData("get_",PropsValueData.get("_HashCode"),"uiRootWindow",None)
		res=wsObj.postMessage({"propertyType": PropsTypeData["propertyType"]["v"],"_HashCode": PropsValueData["_HashCode"]},"uiRootWindow",jsonData)
		CM.addPropsValue(PropsValueData["_HashCode"], "uiRootWindow", res)
		return PropsValueData["uiRootWindow"]

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
