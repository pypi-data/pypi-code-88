#!/usr/bin/env Python
# coding=utf-8
#作者： tony
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
from SDK.Global.IGlobal import IGlobal
from SDK.RenderControl.IRenderControl import IRenderControl
import websockets
import asyncio
import websockets
import json
import time
import Utils.SocketApiServe as ws
from Utils.Config import CM
from Utils.Common import check_exsit

class RenderViewer3D:
    def __init__(self):
        self.renderRoot=None
        asyncio.get_event_loop().run_until_complete(ws._init())

    def  setConfig(self,root,config):
        if(self.renderRoot):
            print("Do not repeat initialization!")
            return
        print("Init RenderControl Start!")
        #if(config.renderAddress):
            #socketApiServe.getParam()
            #self.renderRoot=socketApi.createIframe(root,config)
        # if (config.serverAddress):
        #    self.renderRoot = ws(config)
        if config.serverAddress:
            CM["serverAddress"]=config.serverAddress
        if config.clientdir:
            CM["clientdir"] = config.clientdir
            if check_exsit("WebSocket3Dserver.exe") is False:
                os.system(config.clientdir)
                time.sleep(8)
        if config.datadir:
            CM["datadir"] = config.datadir
        #print("Init RenderControl Success!")

    def getGlobal(self):
        if self.renderRoot:
            raise  Exception('Init RenderControl Error!')
        return IGlobal({"_HashCode":"11111111-1111-1111-1111-111111111111"})

    def getRenderControl(self):
        if self.renderRoot is not None:
             raise Exception('Init RenderControl Error!')
        return IRenderControl({"_HashCode":"11111111-1111-1111-1111-111111111111"})





