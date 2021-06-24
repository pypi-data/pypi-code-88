


#! /usr/bin/env python
# -*- coding:utf-8 -*-
# install ws4py
# pip install ws4py
# easy_install ws4py
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json,uuid,datetime
import asyncio
from Utils.Common import is_json, objtoLowerCase
# from Utils.Common import is_json
from Utils.Config import CM
# from ws4py.client.threadedclient import WebSocketClient

from websocket import create_connection
import json
import time
import _thread

PropsTypeData={}
PropsValueData={}
PropsData={}
websocketcallback=None
sdkInfoData={}
state = "F"
apiCallback={}
websocket =None
msg={}
eventCallback={}
# 全局ws 例子：socketApi._init()#先必须在主模块初始化（只在Main模块需要一次即可），然后其他的任何文件只需要导入即可使用，不需要再初始化了（目前问题在于@property属性装饰器内，无法使用。有待查看）
def _init():
    global _global_ws
    try:
        _global_ws= create_connection(CM["serverAddress"])
        msg = json.dumps({"model": 1, "Token": "d7b501d2-fe5d-4a26-a799-1e67e037bfb5"})
        _global_ws.send(msg)
        # _global_ws.run_forever()
    except KeyboardInterrupt:
        _global_ws.close()

def gen_coroutine(f):
    def wrapper(*args, **kwargs):
        gen_f = f(*args, **kwargs)  # gen_f为生成器PostMessage()
        r = gen_f.__next__()  # r为生成器onMessage
        def fun(g):
            ret = g.__next__() # 执行生成器onMessage
            try:
                gen_f.send(ret) # 将结果返回给PostMessage并使其继续执行
            except StopIteration:
                pass
        _thread.start_new_thread(fun, (r,))
    return wrapper

def postMessage(Props, callName, obj):
    # obj["CallBack"] = "API-{}".format(uuid.uuid1())
    # if Props is not None and callName is not None:
    #     sdkInfo(Props, obj.get("CallBack"), callName, "push")
    str=PostMessage(json.dumps(obj))
    if is_json(str):
        apiData=json.loads(str)
        result = objtoLowerCase(apiData.get("Result"))
        # if apiData.get("CallBack") is not None:
        #     sdkInfo(None, apiData.get("CallBack"), "", "pull")
        #     apiCallback[apiData.get("CallBack")](result)
        #     del apiCallback[apiData.get("CallBack")]
        return result
    else:
        return str
# def postMessage(msg):
#     loop = asyncio.get_event_loop()
#     loop.run_until_complete(send_msg(msg))

def sdkInfo(Props, cbName, callName, type):
    if cbName is None:
        return
    if type == "on":
        pass
    elif type == "pull":
        if sdkInfoData[cbName] is not None:
            className, _HashCode, time = sdkInfoData[cbName]
            # console.info(className, _HashCode,"耗时",(performance.now() - time).toFixed(3) + "ms")
            del sdkInfoData[cbName]
    elif type == "push":
        sdkInfoData[cbName] = {"time": datetime.datetime.now(),
                                    "className": Props["propertyType"]["v"] + "." + callName,
                                    "_HashCode": Props["_HashCode"]}
    else:
        pass

def setCallBack(name,callback):
    eventCallback[name]=callback


@gen_coroutine
def PostMessage(msg):
    _global_ws.send(msg)
    # print( "开始处理请求req_a")
    ret = yield _global_ws.recv()
    # print( "ret%s: %s" % (i,ret))
    return ret
    # print( "完成处理请求req_a")




def AsyncPostMessage(msg):
    _global_ws.send(msg)
#
# class MyWebsocket(WebSocketClient):
#     def opened(self):
#         msg = json.dumps({"model": 1, "Token": "d7b501d2-fe5d-4a26-a799-1e67e037bfb5"})
#         self.send(msg)
#
#     def closed(self, code, reason=None):
#         print("Closed down", code, reason)
#
#     def received_message(self, m):
#         # msg= json.dumps(m)
#         msg = str(m)
#         if len(msg) > 0:
#             apiData = json.loads(msg)
#             # apiData = apiData.get("Result")
#             if "api" in apiData and "CallBack" in apiData:
#                 funName = apiData.get("api")
#                 if apiData.get("ErrorCode") is not None and apiData.get("ErrorCode") > 0:
#                     raise Exception(apiData.get("Exception"))
#                 result = objtoLowerCase(apiData.get("Result"))
#                 if eventCallback["on" + funName]:
#                     sdkInfo(None, funName, "", "on")
#                     eventCallback["on" + funName](result)
#                 else:
#                     sdkInfo(None, apiData["CallBack"], "", "pull")
#                     apiCallback[apiData["CallBack"]](result)
#                     del apiCallback[apiData["CallBack"]]
#
#
#


