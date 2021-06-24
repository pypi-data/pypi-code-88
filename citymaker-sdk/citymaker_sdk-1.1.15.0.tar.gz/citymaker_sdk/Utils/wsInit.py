#!/usr/bin/env Python
# coding=utf-8
#作者： tony
# -*- coding: utf-8 -*-
import os, sys,json,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import os, sys,types,json
import Utils.classmake as cmake
import threading
import asyncio
import websockets
from websocket import create_connection
# from Utils.WebSocketInit import WebSocketServer
from Utils.Common import is_json, objtoLowerCase
from Utils.IRenderControlEventClass import *

from ws4py.client.threadedclient import WebSocketClient
from multiprocessing import Queue
from SDK.RenderControl.IRenderControlEvents import IRenderControlEvents


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def SocketApiServe_init(config):
    global _global_ws,rcEvent,wsEvent
    try:
        _global_ws = WebSocketServer(config.serverAddress, protocols=['chat'])
        _global_ws.connect()
        rcEvent = threading.Event()
        wsEvent = threading.Event()

    except Exception:
        raise

def getrcEvent():
    return rcEvent

# async def main_initWs(config):
#     try:
#         _ws = WebSocketServer(config.serverAddress, protocols=['chat'])
#         _ws.connect()
#         _ws.run_forever()
#
#     except KeyboardInterrupt:
#         _ws.close(reason="user exit")
#     return _ws


def postMessage(Props, callName, obj, isMain=True):
        # obj["CallBack"] = "API-{}".format(uuid.uuid1())
        # if Props is not None and callName is not None:
        #     sdkInfo(Props, obj.get("CallBack"), callName, "push")
        # loop = asyncio.get_event_loop()
        # str=loop.run_until_complete(send_msg(obj))
        # str = eventprocess.SendMessage(json.dumps(obj))
        if type(obj) is str:
            res=_global_ws.send_message(obj)
        else:
            res=_global_ws.send_message(str(obj))


        if is_json(res):
            apiData = json.loads(res)
            result = objtoLowerCase(apiData.get("Result"))
            # if apiData.get("CallBack") is not None:
            #     sdkInfo(None, apiData.get("CallBack"), "", "pull")
            #     apiCallback[apiData.get("CallBack")](result)
            #     del apiCallback[apiData.get("CallBack")]
            return result
        elif type(res) is dict:
            return res["Result"]
        else:
            return res







class WebSocketServer(WebSocketClient):
    def opened(self):
        # self.mutex = threading.Lock()
        self.q=Queue()
        msg = json.dumps({"model": 1, "Token": "d7b501d2-fe5d-4a26-a799-1e67e037bfb5"})
        self.send(msg)

    def closed(self, code, reason=None):
        self.close()
        print("Closed down:", code, reason)

    def sendMsg(self,msg,e):
        self.send(msg)
        e.wait()


    def send_message(self,msg):
        th = threading.Thread(target=self.sendMsg, args=(msg,wsEvent))
        th.start()
        th.join()
        return self.q.get()


    def received_message(self, m):
        recevData=json.loads(str(m))
        if "on"+str(recevData.get("api")) in IRenderControlEvents.Events:
            rcEvent.recvData = recevData
            rcEvent.set()
        else:
            # self.mutex.acquire()
            self.q.put(recevData)
            # self.mutex.release()
            wsEvent.set()
        return m


    # def recv_message(self):
    #     while True:
    #         if self.queue.empty():
    #             break
    #         else:
    #             return self.queue.get()


