#!/usr/bin/env Python
# coding=utf-8
#作者： tony
import time
import datetime
import shelve

class Config():
    def __init__(self):
        self.serverAddress = 'ws://192.168.3.216:8181/'
        self.renderAddress = ""
        self.clientdir=""
        self.datadir=""
        self.AllShow = True
        self.FullShow = True
        self.LogShow = False
        self.NetWorkerShow = True
        self.isEquivalent = False

# LOGIN_TIME_OUT = 60
# db = shelve.open('user_shelve.db', writeback=True)
# serverAddress = 'ws://192.168.3.216:8181/'
CM={"serverAddress":'ws://127.0.0.1:8181/',"clientdir":"","datadir":""}


