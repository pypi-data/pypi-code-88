# -*- coding: UTF-8 -*-
import sys
from ..py_api_b import PyApiB
from adbutils import adb
from ..py_file.fileU import FileU
from ..py_recg.imgU import ImgU
from ..py_phone.adbU import AdbU
import time


class PhoneAutoU(PyApiB):
    """
    手机自动化相关工具
    """
    @staticmethod
    def produce(key=None):
        return PyApiB._produce(key, __class__)
    
    def __init__(self):
        self.deviceName = None
        self.projectName = "test"
        self.cachePath = None
        self.shrinkX = 1
        """ 压缩系数X """
        self.shrinkY = 1
        """ 压缩系数Y """
    
    def init(self, projectName):
        self.projectName = projectName
        self.getConfig()
        return self
    
    def getConfig(self):
        """ 获取配置 """
        configPath = f"./{self.projectName}/sourceConfig.json"
        configs = FileU.produce().read_json(configPath)
        if self.cachePath != configs.get("cachePath"):
            ImgU.produce().setCachePath(configs.get("cachePath"))
        return configs
    
    def __saveConfig(self, config):
        """ 保存配置 """
        configPath = f"./{self.projectName}/sourceConfig.json"
        FileU.produce().write_json(configPath,config)
        
    def setDeviceName(self, deviceName):
        """ 设备操作的设备名 """
        self.deviceName = deviceName
        
    def addScence(self, scenceName):
        """ 添加场景的名称，如：welcome """
        config = self.getConfig()
        if "scences" not in config:
            config["scences"] = {}
        if scenceName not in config["scences"]:
            config["scences"][scenceName] = {
                "name":scenceName,
                "sign": []
            }
            print(f"add '{scenceName}' in config['scences']")
            self.__saveConfig(config)
        else:
            print(f"'{scenceName}' has in config['scences']")
            
    def addSign(self, scenceName, area, option):
        """ 添加特征，新建第一项，如果存在会替换整项 """
        pass
    
    def appendSign(self, scenceName, area, option):
        """ 拼接特征，拼接一项，如果不存在则新建一项，如果存在则接在后面 """
        pass
    
    def setSign(self, scenceName, area, option, index):
        """ 拼接特征，拼接一项，如果不存在则新建一项，如果存在则接在后面 """
        pass
        
    def addAction(self, actionName):
        """ 添加动作的名称,如shoot """
        config = self.getConfig()
        if "actions" not in config:
            config["actions"] = {}
        if actionName not in config["actions"]:
            config["actions"][actionName] = {"name":actionName}
            print(f"add '{actionName}' in config['actions']")
            self.__saveConfig(config)
        else:
            print(f"'{actionName}' has in config['actions']")
        
    def addOption(self, actionName, optionName, args:str, isReAdd=False):
        """ 添加操作到动作名称 """
        config = self.getConfig()
        if "actions" not in config:
            config["actions"] = {}
        if actionName not in config["actions"]:
            config["actions"][actionName] = {"name":actionName}
        if isReAdd or "options" not in config["actions"][actionName]:
            config["actions"][actionName]["options"] = []
        config["actions"][actionName]["options"].append({
            "optionName": optionName,
            "args": self.argsToJson(args)
        })
        self.__saveConfig(config)
    
    def doAction(self, actionName):
        """ 执行动作 """
        config = self.getConfig()
        action = config.get(actionName,{})
        options = action.get("options",[])
        img = None
        for option in options:
            img = self.doOption(img, option.get("optionName"), option.get("args"))
        return img
        
    def doOption(self, imgU, optionName, args:str):
        """ 执行动作后，需要执行的操作 """
        optionFun = getattr(self, f"option_{optionName}")
        if optionFun:
            imgU = optionFun(imgU, self.argsToJson(args))
        return imgU
    
    def __valueToStr(self, value):
        """ value转字符串，与__strToValue成对 """
        valueStr = ""
        if value == None:
            return "None"
        if isinstance(value,dict) or isinstance(value,tuple):
            valueStr = ",".join(list(map(lambda x:self.__valueToStr(x),value)))
        else:
            valueStr = str(value)
        return valueStr
    
    def __strToValue(self, valueStr):
        """ 字符串转value，与__valueToStr成对 """
        value = valueStr
        if valueStr != None:
            if "," in valueStr:
                value = list(map(lambda x:self.__strToValue(x),valueStr.split(",")))
            elif valueStr in ["True","true"]:
                return True
            elif valueStr in ["False","false"]:
                return False
            else:
                hasFix = False
                for fun in [int, float]:
                    if hasFix:
                        break
                    try:
                        value = fun(valueStr)
                        hasFix = True
                    except Exception as e:
                        pass
        else:
            return "None"
        return value
    
    def argsToJson(self, args:str):
        """ 参数转json """
        res = {}
        if args:
            if "&" in args:
                aas = args.split("&")
                for aa in aas:
                    rr = self.argsToJson(aa)
                    res.update(rr)
            elif "=" in args:
                key = args.split("=")[0]
                value = args[len(key)+1:]
                res[key] = self.__strToValue(value)
        return res
    
    def jsonToArgs(self, argsJson):
        """ json转参数 """
        args = []
        for key in argsJson:
            value = argsJson[key]
            args.append(f"{key}={self.__valueToStr(value)}")
        return "&".join(args)

    def option_shoot(self, imgU, argsJson):
        """ 
        通用操作：截图 \n
        command: python3 -m pyuts.py_phone ants doOption shoot None savePath=/Users/jack/Downloads/screenTemp.png
        """
        savePath = argsJson.get("savePath")
        if not savePath:
            savePath = ImgU.produce().getRandomPngPath()
        AdbU.produce().screenshot(savePath,serial=self.deviceName)
        return ImgU.produce().initImg(savePath)
    
    def option_imgU(self, imgU, argsJson):
        """ 
        通用操作：图片子方法调用 \n
        command: python3 -m pyuts.py_phone ants doOption imgU /Users/jack/Downloads/screenTemp.png "funName=crop&box=0,0,100,100"
        """
        funName = argsJson.get("funName")
        if funName:
            del argsJson["funName"]
            fun = getattr(imgU,funName)
            if fun:
                return fun(**argsJson)
        
    
    
    
    