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
import Utils.wsInit as sk
# from websocket import create_connection
import websockets
from Utils.Common import is_json, objtoLowerCase

class EventThead(threading.Thread):
    def __init__(self, e, address,loop):
        super().__init__()
        self.e = e
        self.address = address
        asyncio.set_event_loop(loop)
        self.eventLoop=loop
        loop.run_until_complete(self.initWs())
        # self.ws=_ws
        # self.ws=_ws.connect(address)
        # self.ws = create_connection(self.address)
        # msg = json.dumps({"model": 1, "Token": "d7b501d2-fe5d-4a26-a799-1e67e037bfb5"})
        # self.ws.send(msg)

    def run(self):
        # ws= create_connection(self.address)
        while True:
            if self.e.is_set():
                model =self.onMessage()
                backData=json.loads(model).get("api")
                if self.postData["EventName"]=="on"+backData:
                    cmake.AddRenderEventCB_ep(model, self.fn, self.fnName, self.eventArgs)
                self.e.wait()
                # self.e.clear()
            else:
                self.e.set()
                # print('runing')

    async def initWs(self):
        self._event_ws = await websockets.connect(self.address)

    async def recv(self):
        return await self._event_ws.recv()

    async def send(self,msg):
        s= await self._event_ws.send(msg)
        return  await self._event_ws.recv()

    def onMessage(self):
        msg = self.eventLoop.run_until_complete(self.recv())
        # print("recv_onmessage")
        return msg

    def SendMessage(self,msg):
        # _global_ws=await glo.getWebSockets()
        return self.eventLoop.run_until_complete(self.send(msg))



def eventprocess_init(config,loop):
    global eventprocess,eventLoop
    try:
        rcEvent = threading.Event()
        # ws= websocket.WebSocket()
        eventprocess = EventThead(rcEvent,config.serverAddress,loop)
        # _global_ws.run_forever()
        event_loop=loop
    except KeyboardInterrupt:
        raise

def postMessage(Props, callName, obj, isBack=True):
        # obj["CallBack"] = "API-{}".format(uuid.uuid1())
        # if Props is not None and callName is not None:
        #     sdkInfo(Props, obj.get("CallBack"), callName, "push")
        # loop = asyncio.get_event_loop()
        # str=loop.run_until_complete(send_msg(obj))
        str = eventprocess.SendMessage(json.dumps(obj))
        if is_json(str):
            apiData = json.loads(str)
            result = objtoLowerCase(apiData.get("Result"))
            # if apiData.get("CallBack") is not None:
            #     sdkInfo(None, apiData.get("CallBack"), "", "pull")
            #     apiCallback[apiData.get("CallBack")](result)
            #     del apiCallback[apiData.get("CallBack")]
            return result
        else:
            return str

def EventProcessStart(fn,fnName,eventArgs,Props,callName,postData):
    eventprocess.fn = fn
    eventprocess.fnName = fnName
    eventprocess.eventArgs = eventArgs
    eventprocess.Props=Props
    eventprocess.callName=callName
    eventprocess.postData=postData
    eventprocess.start()






