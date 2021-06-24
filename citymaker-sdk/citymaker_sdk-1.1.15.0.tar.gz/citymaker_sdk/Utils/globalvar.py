#!/usr/bin/env Python
# coding=utf-8
#作者： tony

import os, sys,json,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import os, sys,types,json
from multiprocessing import Process,Event
import Utils.classmake as cmake
# from websocket import create_connection
import Utils.globalvar as glo
import Utils.wsInit as socketApiServe

# from Utils.SocketApiServe import renderControl
# import Utils.RenderViewer3D as r3d
# from Utils.RenderViewer3D_ import _renderControl
import asyncio
import websockets
import threading
import Utils.wsInit as wsObj
import Utils.globalData as glodata

_renderControl="renderControl"
_config="config"
_rcEvent="rcEvent"
_eventprocess="eventprocess"
_global_ws="_global_ws"
_global_wse="_global_wse"
_curloop="curloop"
_eventloop="eventloop"
def _initAxControl(conf):#初始化
    glodata._init()
    wsObj.SocketApiServe_init(conf)


    global _global_dict
    _global_dict = {}
    # renderViewer3D = r3d.renderViewer3D(conf)
    # renderControl= renderViewer3D.getRenderControl()
    # _global_dict[_renderControl]= renderControl
    # _global_dict[_config] = conf
    # rcEvent = Event()
    # eventprocess = EventProcess(rcEvent, conf.serverAddress,renderControl)


def set_value(key,value):#""" 定义一个全局变量 """
    _global_dict[key] = value


def get_value(key,defValue=None): #""" 获得一个全局变量,不存在则返回默认值 """
    try:
        return _global_dict[key]
    except KeyError:
        return defValue

# def getRenderControl():
#     try:
#         return _global_dict[_renderControl]
#     except KeyError:
#         return None
# def getNewRenderControl():
#     try:
#         renderViewer3D = r3d.renderViewer3D()
#         return renderViewer3D.getRenderControl()
#     except KeyError:
#         return None

# def getConfig():
#     try:
#         return _global_dict[_config]
#     except KeyError:
#         return None

# async def getWebSockets():
#     try:
#         return _global_dict[_global_ws]
#     except KeyError:
#         return None

# def postMessage(Props, callName, obj):
#     return eventprocess.postMessage(Props, callName, obj)
#