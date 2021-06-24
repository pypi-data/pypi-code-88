#!/usr/bin/env Python
# coding=utf-8#
#作者： tony1
import os, sys,json
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import Utils.classmake as CM
import Utils.classPath as CP
import Utils.SocketApiServe as socketApi 
Props={"slideRootGroup":{"t":"Guid","v":"",
"F":"gs"},"showSlide":{"t":"bool","v":False,
"F":"gs"},"notInTreeID":{"t":"Guid","v":"",
"F":"g"},"rootID":{"t":"Guid","v":"",
"F":"g"},"slidePopup":{"t":"bool","v":True,
"F":"gs"},"_HashCode":{"t":"S","v":"","F":"g"},
"propertyType":{"t":"S","v":"IProjectTree","F":"g"}}
class IProjectTree:
	def __init__(self,args):
		CM.AddProps(self, Props, args)
		#CM.AddDefineProperty(self, Props)

	def initParam(self,args):
		self.slideRootGroup=args.get("slideRootGroup")
		self.showSlide=args.get("showSlide")
		self.notInTreeID=args.get("notInTreeID")
		self.rootID=args.get("rootID")
		self.slidePopup=args.get("slidePopup")
		self._HashCode=args.get("_HashCode")
		self.propertyType=args.get("propertyType")

	def createLockedGroup(self,arg0,arg1):  # 先定义函数 
		args = {
				"groupName":{"t": "S","v": arg0},
				"parentGroupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createLockedGroup', 1, state)


	def getProjectTreeList(self,):  # 先定义函数 
		args = {}
		state = "new"
		return CM.AddPrototype(self,args, 'GetProjectTreeList', 1, state)


	def getProjectTreeGroups(self,):  # 先定义函数 
		args = {}
		state = "new"
		return CM.AddPrototype(self,args, 'GetProjectTreeGroups', 1, state)


	def findItem(self,arg0):  # 先定义函数 
		args = {
				"path":{"t": "S","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'findItem', 1, state)


	def getClientData(self,arg0,arg1):  # 先定义函数 
		args = {
				"iD":{"t": "G","v": arg0},
				"name":{"t": "S","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getClientData', 1, state)


	def getGroupSlideImageName(self,arg0):  # 先定义函数 
		args = {
				"groupID":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getGroupSlideImageName', 1, state)


	def getItemName(self,arg0):  # 先定义函数 
		args = {
				"iD":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getItemName', 1, state)


	def getNextItem(self,arg0,arg1):  # 先定义函数 
		args = {
				"iD":{"t": "G","v": arg0},
				"code":{"t": "N","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getNextItem', 1, state)


	def getVisibility(self,arg0):  # 先定义函数 
		args = {
				"iD":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'getVisibility', 1, state)


	def highlightGroup(self,arg0,arg1):  # 先定义函数 
		args = {
				"groupId":{"t": "G","v": arg0},
				"colorValue":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'highlightGroup', 0, state)


	def isGroup(self,arg0):  # 先定义函数 
		args = {
				"iD":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'isGroup', 1, state)


	def isLocked(self,arg0):  # 先定义函数 
		args = {
				"iD":{"t": "G","v": arg0}
		}
		state = ""
		return CM.AddPrototype(self,args, 'isLocked', 1, state)


	def loadCepLayer(self,arg0,arg1):  # 先定义函数 
		args = {
				"cepURL":{"t": "S","v": arg0},
				"parentGroupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'loadCepLayer', 1, state)


	def lockGroup(self,arg0,arg1):  # 先定义函数 
		args = {
				"groupID":{"t": "G","v": arg0},
				"lock":{"t": "B","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'lockGroup', 0, state)


	def saveAsCep(self,arg0,arg1):  # 先定义函数 
		args = {
				"cepName":{"t": "S","v": arg0},
				"groupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'saveAsCep', 1, state)


	def setClientData(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"iD":{"t": "G","v": arg0},
				"name":{"t": "S","v": arg1},
				"value":{"t": "S","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setClientData', 0, state)


	def setGroupSlideImageName(self,arg0,arg1):  # 先定义函数 
		args = {
				"groupID":{"t": "G","v": arg0},
				"imageName":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setGroupSlideImageName', 0, state)


	def setVisibility(self,arg0,arg1):  # 先定义函数 
		args = {
				"iD":{"t": "G","v": arg0},
				"visibleMask":{"t": "N","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'setVisibility', 0, state)


	def traverse(self,):  # 先定义函数 
		args = {}
		state = ""
		return CM.AddPrototype(self,args, 'traverse', 1, state)


	def unhighlightGroup(self,arg0):  # 先定义函数 
		args = {
				"groupId":{"t": "G","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'unhighlightGroup', 0, state)


	def createGroup(self,arg0,arg1):  # 先定义函数 
		args = {
				"groupName":{"t": "S","v": arg0},
				"parentGroupID":{"t": "G","v": arg1}
		}
		state = ""
		return CM.AddPrototype(self,args, 'createGroup', 1, state)


	def getProjectTreeList(self,):  # 先定义函数 
		args = {}
		state = "new"
		return CM.AddPrototype(self,args, 'GetProjectTreeList', 1, state)


	def getProjectTreeGroups(self,):  # 先定义函数 
		args = {}
		state = "new"
		return CM.AddPrototype(self,args, 'GetProjectTreeGroups', 1, state)


	def setParent(self,arg0,arg1,arg2):  # 先定义函数 
		args = {
				"guid":{"t": "G","v": arg0},
				"groupID":{"t": "G","v": arg1},
				"index":{"t": "N","v": arg2}
		}
		state = ""
		CM.AddPrototype(self,args, 'setParent', 0, state)


	def renameGroup(self,arg0,arg1):  # 先定义函数 
		args = {
				"groupID":{"t": "G","v": arg0},
				"groupName":{"t": "S","v": arg1}
		}
		state = ""
		CM.AddPrototype(self,args, 'renameGroup', 0, state)


	def deleteItem(self,arg0):  # 先定义函数 
		args = {
				"iD":{"t": "G","v": arg0}
		}
		state = ""
		CM.AddPrototype(self,args, 'deleteItem', 0, state)

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
				super(IProjectTree, self).__setattr__(name, value)

	def to_json(self):
		result={}
		for k, v in self.__dict__.items():
			if k=="_HashCode":
				result[k] = v
			else:
				result[k.strip("_")] = v
		return result
