#!/usr/bin/env Python
# coding=utf-8
#作者： tony

import os, sys,json,time
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import json
from ws4py.client.threadedclient import WebSocketClient
from multiprocessing import Queue
from SDK.RenderControl.IRenderControlEvents import IRenderControlEvents
import threading

class WebSocketServer(WebSocketClient):

    def opened(self):
        self.EventQueue=Queue()
        self.queue=Queue()
        # self.e=threading.Event()

        msg = json.dumps({"model": 1, "Token": "d7b501d2-fe5d-4a26-a799-1e67e037bfb5"})
        self.send(msg)

    def closed(self, code, reason=None):
        self.close()
        print("Closed down:", code, reason)

    def send_message(self,msg):
        self.send(msg)
        # while self.queue.qsize > 0:
        #     self.queue.get()
        while True:
            if not self.queue.empty():
               return self.queue.get()

    def aa(self,msg):
        self.send(msg)
        self.e.wait()

    def post(self,msg):
        th = threading.Thread(target=self.aa, args=(msg))
        th.start()
        return self.d


    def received_message(self, m):
        recevData=json.loads(str(m))
        if  "on"+str(recevData.get("api")) in IRenderControlEvents.Events:
            self.EventQueue.put(recevData)
        else:
            self.queue.put(recevData)
        return m


    # def recv_message(self):
    #     while True:
    #         if self.queue.empty():
    #             break
    #         else:
    #             return self.queue.get()

    def recv(self):
        while True:
            if self.EventQueue.empty():
                continue
            else:
                return self.EventQueue.get()



