#!/usr/bin/env Python
# coding=utf-8
#作者： tony

import os, sys,json,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


def _init():#初始化
    global PropsTypeData,PropsValueData,PropsData,websocketcallback,sdkInfoData,state,apiCallback,websocket,msg,eventCallback
    _global_dict={}
    PropsTypeData={}
    PropsValueData={}
    PropsData={}
    websocketcallback = None
    sdkInfoDat={}
    state = "F"
    apiCallback={}
    websocket = None
    msg = {}
    eventCallback = {}
    # rcEvent = Event()
    # eventprocess = EventProcess(rcEvent, conf.serverAddress,renderControl)

def PropsTypeDataGet(key):
    if key is None:
        return
    result=PropsTypeData.get("I"+key)
    if result is None:
        PropsTypeData["I"+key]={}
    return PropsTypeData["I"+key]

def PropsTypeDataSet(key,val):
    PropsTypeData["I"+key]=val
    return val

def PropsValueDataGet(key):
    if key is None:
        return
    result=PropsValueData.get("I"+key)
    if result is None:
        PropsValueData["I"+key]={}
    return PropsValueData["I"+key]

def PropsValueDataSet(key,val):
    PropsValueData["I"+key]=val
    return val

def PropsDataGet(key):
    if key is None:
        return
    result = PropsData.get("I"+key)
    if result is None:
        PropsData["I"+key] = {}
    return PropsData["I"+key]

def PropsDataSet(key,val):
    PropsData["I"+key]=val
    return val

def sdkInfoDataGet(key):
    if key is None:
        return
    result = sdkInfoData.get(key)
    if result is None:
        sdkInfoData[key] = {}
    return sdkInfoData[key]

def sdkInfoDataSet(key,val):
    sdkInfoData[key]=val
    return val

def apiCallbackGet(key):
    if key is None:
        return
    result = apiCallback.get(key)
    if result is None:
        apiCallback[key] = {}
    return apiCallback[key]

def apiCallbackSet(key,val):
    apiCallback[key]=val
    return val

def eventCallbackGet(key):
    if key is None:
        return
    result = eventCallback.get(key)
    if result is None:
        eventCallback[key] = {}
    return eventCallback[key]

def eventCallbackGet(key,val):
    eventCallback[key]=val
    return val