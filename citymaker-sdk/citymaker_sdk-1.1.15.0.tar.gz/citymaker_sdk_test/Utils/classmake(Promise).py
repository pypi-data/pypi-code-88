#!/usr/bin/env Python
# coding=utf-8
#作者： tony
import os, sys,types,json
import importlib,asyncio
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from Utils.classPath import ClassFN
from Utils.InstanceActivator import InstanceActivator
import Utils.EventSocketApiServe as socketApiServe
from Utils.Common import is_json
from Utils.mathMake import needGetObject


"""
获取对应_HashCode的Props类型对象  
@param {guid} _HashCode
"""
def getPropsTypeData(_HashCode):
    if _HashCode is None:
        return
    result=socketApiServe.PropsTypeData.get("I" + _HashCode)
    if result is None:
        result =socketApiServe.PropsTypeData["I" + _HashCode]={}
    return result

"""获取对应_HashCode的Props类型信息和值
@param {guid} _HashCode
"""
def getPropsValueData(_HashCode):
    if _HashCode is None:
        return

    result=socketApiServe.PropsValueData.get("I" + _HashCode)
    if result is None:
        result =socketApiServe.PropsValueData["I" + _HashCode] = {}
    return result

"""
获取对应_HashCode的Props类型信息
 @param {guid} _HashCode
 """
def getPropsData(_HashCode):
    if _HashCode is None:
        return
    result = socketApiServe.PropsData.get("I" + _HashCode)
    if result is None:
        result =socketApiServe.PropsData["I" + _HashCode] = {}
    return result


"""
获取对应_HashCode的序列化对象,并反序列化至该_HashCode的值中 
@param {guid} _HashCode 唯一键值 
@param {string} propertyType 实例类型  
@param {string} callName 实例名
"""
def getObject(obj,_HashCode, propertyType, callName):
    if callName in  needGetObject  or "add" in callName or "Add" in callName :
    # if True:
        JsonData = {"api": "GetObject", "_HashCode":_HashCode}
        #await socketApiServe.postMessage({propertyType, _HashCode},"GetObject",JsonData);
        res = socketApiServe.postMessage({propertyType, _HashCode},"GetObject",JsonData)
        if res:
            PropsValueData = getPropsValueData(res["_HashCode"])
            PropsData = getPropsData(res["_HashCode"])
            obj.initParam(res)
            for cn in res:
                PropsValueData[cn] = getClass(res[cn])
                PropsData[cn] =res[cn]
            return True
    return False

"""
 * 获取传输的api名称
 * @param {string} callState 方法名称
 * @param {guid} hCode 唯一键值
 * @param {string} argName 参数名
 * @param {string} state 方法状态
"""
def getApiName(callState,hCode,argName, state):
    PropsData = getPropsData(hCode)
    PropsTypeData = getPropsTypeData(hCode)
    ApiName=""
    aNameU = ""
    cName = PropsData["propertyType"][1:]
    if argName.find("new_") > -1:
        aNameU = argName.replace(argName[0], argName[0].lower())
    else:
        aNameU = argName.replace(argName[0], str(argName[0]).upper())
    if (callState == "prototype"):
        ApiName = cName + "." + aNameU
        if (cName != "RenderControl"):
            ApiName = "{" + hCode + "}." + aNameU
        if (state == "new"):
            ApiName = aNameU
    else:
        if (PropsTypeData.get(argName) is not None and PropsTypeData.get(argName).get("H")) is not None:
            aNameU = argName.replace(argName[0], argName[0].lower())
            ApiName = callState + aNameU
        else:
            ApiName = cName + "." + callState + aNameU
        if (cName != "RenderControl"):
            ApiName = "{" + hCode + "}." + callState + aNameU
    return ApiName

# * 通过反序列化数据 获取实例
# * @param {*} data  数据
def getClass(data):
    if data is not None and type(data) is list:
        for i in data:
            i=getClass(i)
    elif data is not None and type(data) is dict:
        if data.get("propertyType") is not None and ClassFN[data.get("propertyType")]:
            data=InstanceActivator.createInstance(str(ClassFN[data.get("propertyType")])+"."+data.get("propertyType"),data)
        else:
            for key in data:
                key=getClass(key)
    return data

# * 通过实例获取 实例的值
# * @param {*} data
def getClassProps(data):
    if data and type(data) is list:
        data = data
        for i in data:
            i = getClassProps(i)
    elif data and type(data) is dict:
        data = data
        if data is not None and type(data) is not dict:
            data = getPropsData(data["_HashCode"])
        else:
            for key in data:
                data[key] = getClassProps(data[key])
    return data

# * 设置 PropsValueData  PropsData的值
# * @param {guid} _HashCode
# * @param {string} callName
# * @param {any} res
def addPropsValue(_HashCode, callName, resStr):
    if is_json(resStr):
        res = json.loads(resStr)
    else:
        res=resStr
    PropsTypeData = getPropsTypeData(_HashCode)
    PropsValueData = getPropsValueData(_HashCode)
    PropsData = getPropsData(_HashCode)
   # t= PropsTypeData[callName]
    lis=PropsTypeData.get(callName)
    t=dict_get(lis, 't', None)

    if res is None and t is not None and ClassFN.get(t) and PropsValueData.get("propertyType") == "IRenderControl":
        #eval("import "+ClassFN[t]+" as "+t)
        #PropsValueData[callName] =ClassFN[t]()
        PropsValueData[callName] =InstanceActivator.createInstance(ClassFN[t]+"."+t)
        PropsData[callName] = {}
    elif res is not None and type(res) is not dict:
        PropsValueData[callName] = res
        if res is not None and  hasattr(res,"_HashCode"):
            PropsData[callName] = getPropsData(res.get("_HashCode"))
        else:
            PropsData[callName] =res
    else:
        # if res is not None and isinstance(res,object) and "_HashCode" in str(res):
        PropsValueData[callName] = getClass(res)
        PropsData[callName] = res



# * 由获取到的数据反序列化实例属性数据,属性赋值
# * @param {class} that
# * @param {object} Props
# * @param {any} args
def AddProps(obj, Props, args):
    #obj._HashCode=args["_HashCode"]
    if args is not None and args["_HashCode"] is not None:
        if hasattr(obj,"_HashCode") is False:
            setattr(obj,"_HashCode",args["_HashCode"])
    if hasattr(obj,"_HashCode") and obj._HashCode is None:
        raise Exception("Missing unique key value:_HashCode!")
    elif hasattr(obj,"_HashCode") and obj._HashCode is not None:
        #Props = Props
        if getPropsTypeData(obj._HashCode) is None:
            socketApiServe.PropsTypeData["I" + obj._HashCode] = {}
        if getPropsValueData(obj._HashCode) is None:
            socketApiServe.PropsValueData["I" + obj._HashCode] = {}
        if getPropsData(obj._HashCode) is None:
            socketApiServe.PropsData["I" + obj._HashCode] = {}
        for callName in Props:
            if callName == "_HashCode" or callName == "propertyType":
                if socketApiServe.PropsTypeData.get("I" + obj._HashCode).get(callName) is None:
                    socketApiServe.PropsTypeData["I" + obj._HashCode][callName] =  Props.get(callName)
            else:
                if socketApiServe.PropsTypeData["I" + obj._HashCode] is None:
                    socketApiServe.PropsTypeData["I" + obj._HashCode]={}
                socketApiServe.PropsTypeData["I" + obj._HashCode][callName] = Props.get(callName)
            arg = args.get(callName) if args is not None and args.get(callName) is not None else Props[callName]["v"]
            addPropsValue(obj._HashCode, callName, arg)

# * api服务端交互数据 校验并处理
# * @param {*} callState //交互类型  属性的set/get 方法
# * @param {*} Props     //类的私有属性对象
# * @param {*} callName  //交互名称
# * @param {*} args      //参数
# * @param {*} state     //方法的类型
def setJsonData(callState, _HashCode, callName, args, state=""):
    PropsData = getPropsData(_HashCode)
    result = {}
    className = PropsData["propertyType"]
    result["api"] = getApiName(callState, _HashCode, callName, state)
    if args:
        for argName in args:
            arg = args[argName]
            argKey=argName[0].upper()+argName[1:]
            t=arg["t"]
            if type(arg["v"]) not in [int,str,tuple,set,dict,float,bool]:
                v= arg["v"].to_json()
            else:
                v= arg["v"]
            argType = ""
            if ClassFN.get(t) is not None:
                C = t
                argType = ClassFN.get(C)
                t = "CT"
            if "gvi" in t:
                N = t
                argType = N
                t = "M"
#           ErrorCheck[t](v, className, callState, callName, argName, argType);
            if type(v) not in [int,str,tuple,set,dict,float,bool]:
                if v is not None and type(v)  in [int,str,tuple,set]:
                    result[argKey] = getPropsData(v["_HashCode"])
                else:
                    result[argKey] = getClassProps(v)
            else:
                if v is None:
                    if t == "str":
                        result[argKey] = ""
                    else:
                        result[argKey] =None
                else:
                    result[argKey]=v
    return result

# 类方法实现
# @param {*} that  //类this
# @param {*} args  //方法参数
# @param {*} callName//方法名
# @param {*} ret //返回值对象
#@param {*} state //方法的类型   原方法  新方法等
async def AddPrototype(obj, args, callName, ret, state):
    Props = getPropsData(obj._HashCode)
    JsonData = setJsonData("prototype",obj._HashCode,callName,args,state)
    res =socketApiServe.postMessage({"propertyType": Props["propertyType"],"_HashCode": Props["_HashCode"]},callName,JsonData)
    getObject(obj,Props["_HashCode"], Props["propertyType"], callName)
    if ret:
        return getClass(res)
    else:
        return None

def AddRenderEventCB(fn,fnName,eventArgs=None):
    # viewmodel = socketApiServe.onMessage()
    # socketApiServe.setCallBack(eve,data)
    def setcallb(eve, viewmodel):
        model = json.loads(viewmodel).get("Result")
        args = []
        if eventArgs is not None:
            for key, arg in eventArgs.items():
                m = dict2obj(model.get(key[0].upper() + key[1:]))
                args.append(m)
            fn(*args)
        else:
            fn()
    socketApiServe.setCallBack(lambda eve, data:setcallb())

# def AddRenderEventCB(fn,fnName,eventArgs=None):
#     def call(result):
#         if eventArgs is not None :
#             args = []
#             for key, arg in eventArgs.items():
#                 m = dict2obj(result.get(key))
#                 args.append(m)
#             fn(*args)
#         else:
#             fn()
#     socketApiServe.setCallBack(fnName,call)
#     socketApiServe.start()



#获取字典中的objkey对应的值，适用于字典嵌套
#dict:字典
#objkey:目标key
#default:找不到时返回的默认值
def dict_get(dict, objkey, default):
    tmp = dict
    if(tmp is None):
        return None
    for k,v in tmp.items():
        if k == objkey:
            return v
        else:
            if type(v).__name__=="dict":
                ret = dict_get(v, objkey, default)
                if ret is not default:
                    return ret
    return default

def ToDict(obj):
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d

def ToModel(d):
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items())
        instance = class_(**args)
    else:
        instance = d
    return instance

def dict2obj(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    d = Dict()
    for k, v in dictObj.items():
        d[k[0].lower()+k[1:]] = dict2obj(v)
    return d
class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__

