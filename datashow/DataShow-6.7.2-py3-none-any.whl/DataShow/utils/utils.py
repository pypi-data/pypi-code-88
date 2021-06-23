# -*- coding:utf-8 -*-

from threading import Thread
import inspect
import ctypes
from multiprocessing import Process
# from ..data.uart_process import RadarPort
# import time

class RecvProcess(Process):
    def __init__(self, uart, out_queue):
        super(RecvProcess, self).__init__()
        self.out_queue = out_queue
        self.uart = uart
        
    def run(self):
        # uart = RadarPort()
        # uart.writeFrameToUart(-1)
        # time.sleep(0.1)
        # uart.radar_port.reset_input_buffer()
        while True:
            temp_buffer = self.uart.getMsg(5000)
            print(temp_buffer)


class ThreadWithResult(Thread):
    def __init__(self, func, args=()):
        super(ThreadWithResult, self).__init__()
        self.func = func
        self.args=args
        self.msg_queue = args[0]
        self.result=None
    def run(self):
        while True:
            self.result=self.func()
            if self.result is not None:
                if not self.msg_queue.full():
                    self.msg_queue.put(self.result)
                else:
                    raise Exception("Error: the msg-queue is full!")

    def getResult(self):
        if self.result is not None:
            return self.result


def _async_raise(tid, exctype):
    """raises the exception, performs cleanup if needed"""
    tid = ctypes.c_long(tid)
    if not inspect.isclass(exctype):
        exctype = type(exctype)
    res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
    if res == 0:
        raise ValueError("invalid thread id")
    elif res != 1:
        # """if it returns a number greater than one, you're in trouble,
        # and you should call it again with exc=NULL to revert the effect"""
        ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
        raise SystemError("PyThreadState_SetAsyncExc failed")

def stopThread(thread):
    _async_raise(thread.ident, SystemExit)