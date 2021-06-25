#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import socket
import websocket
from websocket import create_connection
from multiprocessing import Process, Queue, JoinableQueue
import asyncio
import threading
import configparser
import os
import time
import functools
import struct
import ctypes
import inspect

from npsdkobjs import *
from Stockdrv import *

import logging
LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
#logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
formatter = logging.Formatter(LOG_FORMAT)

handler = logging.FileHandler("npdatapoolthread.log")
handler.setLevel(logging.INFO)
handler.setFormatter(formatter)

console = logging.StreamHandler()
console.setLevel(logging.INFO)
console.setFormatter(formatter)
logger.addHandler(handler)
#logger.addHandler(console)

doc="""
	    #历史K线标准周期：分时、分笔、1分K线、5分钟K线、日线。15、30、60分钟由5分钟组成；周、月、季、年K线由日线生成。

	    #初始化：市场代码表、除权、财务、实时行情等，第一次连接，自动申请一次，市场代码有变动，主服务器会主动推送。
        #init = "类型=初始化&编码=unicode"  # unicode 比 utf-8 快很多
	    #self.Send(init)

	    #复权：0 无复权或不填写(默认)；-1 向前复权：历史方向(通常做法)；1 向后复权：未来方向

	    #当天数据：0 不包括当天数据；
	    #格式：0 结构体(默认)、1 Json
        #setPqram  = "类型=K线参数&当天数据=1&复权=0&格式=0&版本=OEM_Ver2020"  #按约定格式传回K线数据
        #self.Send(setPqram)

        #split    = "代码=SH600000&类型=除权"
        #finance  = "代码=SH600000&类型=财务"
        #splitFin = "代码=SH600000&类型=除权财务"
        #f10       = "代码=SH600000&类型=F10资料"
        #report   = "代码=SH600000&类型=实时行情"
        
        #print("正在申请%s \r\n" % (split))
        #self.send_command_over_ws(split)
        #self.send_command_over_ws(finance)
        #self.send_command_over_ws(splitFin)
        #self.send_command_over_ws(f10)
        #self.send_command_over_ws(report)
        
        #day      = "代码=SH600000&类型=日线&数量=0&开始=0"  #申请日线，数量：K线根数，0 使用面板设置值；开始：从最新往历史方向第几根
        day      = "代码=SH000001&类型=日线&数量=1000&开始=1000"  #申请日线，数量：K线根数，0 使用面板设置值；开始：从最新往历史方向第几根
        #week     = "代码=SH000001&类型=周线&数量=5000"         #申请周线(未支持)
        #month    = "代码=SH600000&类型=月线&数量=5000"         #申请月线(未支持)
        #quarter  = "代码=SH600000&类型=季线&数量=5000"         #申请季线(未支持)
        #year     = "代码=SH600000&类型=年线&数量=5000"         #申请年线(未支持)
        min1     = "代码=SH600000&类型=1分钟线&数量=3000"      #申请1分钟线
        min5     = "代码=SH600000&类型=5分钟线&数量=3000"      #申请5分钟线
        #min15    = "代码=SH600000&类型=15分钟线&数量=3000"     #申请15分钟线(未支持)
        #min30    = "代码=SH600000&类型=30分钟线&数量=3000"     #申请30分钟线(未支持)
        #min60    = "代码=SH600000&类型=60分钟线&数量=3000"     #申请60分钟线(未支持)
        #trace    = "代码=SH600000&类型=分笔&数量=0"            #申请分笔(每3秒)
        #tick     = "代码=SH600000&类型=分时&数量=3000"         #分时(每分钟)(未支持)
        
        #print("正在申请%s \r\n" % (day))
        #self.send_command_over_ws(day)
        #self.send_command_over_ws(week)
        #self.send_command_over_ws(month)
        #self.send_command_over_ws(quarter)
        #self.send_command_over_ws(year)
        #self.send_command_over_ws(min1)
        #self.send_command_over_ws(min5)
        #self.send_command_over_ws(min15)
        #self.send_command_over_ws(min30)
	    #self.send_command_over_ws(min60)
        #self.send_command_over_ws(trace)
        #self.send_command_over_ws(tick)
        
        #wprintf("正在申请%s \r\n", askDay)
        #self.send_command_over_ws(askDay)
        
        #提示：申请某个板块，可以自行建立一个函数，连续申请，后台自动向服务器申请数据。
        
        #close  = "类型=关闭接口"
        #hide   = "类型=隐藏接口"
        #show   = "类型=显示接口"
        #market = "类型=市场代码表"
        
        #self.send_command_over_ws(close)
        #self.send_command_over_ws(hide)
        #self.send_command_over_ws(show)
        #self.send_command_over_ws(market)
"""

class NpDataPoolThread(threading.Thread): #(Process)
    
    internal_lock = threading.Lock()

    def __init__(self,  command_queue, response_queue, playmode = NPSDKAPI_PLAYMODE_WEBSOCKET, exePpath = ".\\网际风\\"):

        threading.Thread.__init__(self)
        #super().__init__()

        self._command_queue = command_queue     # command queue for requesting data
        self._response_queue = response_queue   # response queue for sending data
        
        self._ws_message_queue = JoinableQueue()    # queue for data received from websocket  
        self._ws_command_queue = JoinableQueue()    # queue for command sent to websocket
        logger.info('get and create internal queues...')

        self.processqueuethread_stopevent = threading.Event()
        self.sendwscommandthread_stopevent = threading.Event()

        self._playmode = playmode
        self._backtest_rawdata_queue = JoinableQueue() # 测试 数据包回放
        self._start_backtest_flag = False

        self._stopped_flag = False 

        #os.environ["CUDA_DEVICES_ORDER"]   = "PCI_BUS_IS"
        #os.environ["CUDA_VISIBLE_DEVICES"] = '0'  #表示调用0块GPU
        self.m_ws   = None
        self.m_stop = False
        self.m_url  = "ws://127.0.0.1:39398/"
        self.m_logined = NPSDKAPI_WS_DISCONNECTED
        #websocket.enableTrace(True)

        file = exePpath + "用户\\配置文件.ini"

        config = configparser.ConfigParser() # 创建配置文件对象
        config.read(file, encoding='utf-16') # 读取文件
        ip   = config.get('第三方调用', '连接地址01')
        port = config.get('第三方调用', '端口01')
        self.m_url = 'ws://' + ip +':' + port

        if self._playmode == NPSDKAPI_PLAYMODE_BACKTEST: # 数据包回放测试，准备数据包
            #self.prepare_backtest_klinesdata('backtest-4.dat', 'klines1min.dat', '1分钟线') # 从混合数据中分拣出K线数据
            self.prepare_backtest_queue('backtest0531-2.dat')


    """    
    向_ws_message_queue中压入从ws收到的数据
    返回：bool
    """
    def put_ws_message_queue(self, msg):  
        try:
            #with self.internal_lock:                
                if self._stopped_flag: 
                    return False 

                if not self._ws_message_queue.full():
                    self._ws_message_queue.put(msg) #put_nowait()
                    return True
                else:
                    return False
        except Exception as e:
            logger.warning('put_wsmessage_queue() exception: %r'% e)
            return False

    #停止线程函数
    def _async_raise(self, tid, exctype):
        """raises the exception, performs cleanup if needed"""
        tid = ctypes.c_long(tid)
        if not inspect.isclass(exctype):
            exctype = type(exctype)
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, ctypes.py_object(exctype))
        print("res:%s"% res)
        if res == 0:
            raise ValueError("invalid thread id")
        elif res != 1:
            # """if it returns a number greater than one, you're in trouble,
            # and you should call it again with exc=NULL to revert the effect"""
            ctypes.pythonapi.PyThreadState_SetAsyncExc(tid, None)
            raise SystemError("PyThreadState_SetAsyncExc failed")

    #是否K线格式
    def is_klines_type(self, type)-> bool:   
        arr = ["1分钟线", "5分钟线", "15分钟线", "30分钟线", "60分钟线", "日线", "周线", "月线", "季线", "年线", "多日线"]
        #x = arr.count(type)
        return type in arr

    #发送基于websocket的数据请求命令
    def send_command_over_ws(self, ask):
        if self.m_logined == NPSDKAPI_WS_DISCONNECTED:   #网络断开
            print("数据接口连接已断开")
            return
        try:
            ask = "股票数据?" + ask + "&版本=20210310"
            #logger.info('wscmd: '+ask)
            self.m_ws.send(ask)
        except Exception as e:
            error = "数据接口连接已断开"
            self.on_error(error)

            logger.warning('send_command_over_ws() exception: %r'% e)
            
    def on_message(self, message): #实时全推数据处理量大，建议拷贝数据后，扔到队列去 其它线程去处理
        """ 
        把原始数据压入_ws_message_queue队列，留给子线程后续处理
        """
        # 纪录历史数据包，以备数据包回测用
        #with open('backtest0531-2.dat','ab') as fo:
        #    fo.write(message)
        #fo.close()

        #print('-------------------on_message type: %s '%type(message))
        self.put_ws_message_queue(message)

    def on_error(self, error):
        print(error)

    def on_close(self):
        print("关闭数据接口连接")
        self.m_logined = NPSDKAPI_WS_DISCONNECTED

    def on_open(self):
        print("数据接口连接成功")
        self.m_logined = NPSDKAPI_WS_CONNECTED

        init = "类型=初始化&编码=unicode"  # unicode 比 utf-8 快很多
        self.send_command_over_ws(init)

        #当天数据：0 不包括当天数据；
	    #格式：0 结构体(默认)、1 Json
        #setPqram  = "类型=K线参数&当天数据=1&复权=0&格式=0&版本=OEM_Ver2020"  #按约定格式传回K线数据
        setPqram = "类型=K线参数&当天数据=1&复权=0&格式=0"  # 按约定格式传回K线数据
        self.send_command_over_ws(setPqram)

    def Connect(self):
        try:
            self.m_ws = create_connection(self.m_url, sockopt = ((socket.IPPROTO_TCP, socket.TCP_NODELAY, 1),))
        except Exception as e:
            error = "数据接口连接失败"
            self.on_error(error)
            self.on_close()
            return
        try:
            self.on_open()
            while True:
                if self.m_stop: 
                    break         
                rcv = self.m_ws.recv()
                self.on_message(rcv)
        except Exception as e:
            error = "数据接口连接已断开"
            self.on_error(error)
            
            logger.warning('websocket exception:%r'% e)
        finally:
            self.m_stop = True
            self.on_close()
            self.m_ws.close()
            return

    # ----------------------------------------------------------------------        
    def prepare_backtest_klinesdata(self, infilename, outfilename, ktype):

        # 数据包回放测试。先从混合数据文件分拣出指定K线类型数据包（wshead + wsbody）

        filesize = os.path.getsize(infilename)  
        with open(infilename,'rb') as fo:
            bktestdata = fo.read(filesize)
        fo.close()
 
        i = 0
        while(len(bktestdata)>0):
            #t = time.perf_counter()
            wshead_unit = OEM_DATA_HEAD()
            wshead_unit.decode(bktestdata)  #把字节流 转成 ctypes结构体
            #wsheadinfo = "ws data head info:\r\n[oemVer:%s] x [type:%s] x [label:%s] x [name:%s] x [flag:%s] x [askId:%s] x [len:%s] x [count:%s]" \
            #    % (wshead_unit.oemVer, wshead_unit.type, wshead_unit.label, wshead_unit.name, wshead_unit.flag, wshead_unit.askId, wshead_unit.len, wshead_unit.count)
            #print(wsheadinfo)

            length_unit = sizeof(OEM_DATA_HEAD) + wshead_unit.len
            wsbody_unit = bktestdata[0: length_unit]

            if wshead_unit.type == ktype:
                i = i + 1
                print('%s : 第%s条'%(ktype, i))
                with open(outfilename,'ab') as fo:
                    fo.write(wsbody_unit)
                fo.close()
            
            bktestdata = bktestdata[length_unit : ] #取出一段完整的命令响应
            #print(f'coast:{time.perf_counter() - t:.8f}s')

    # ----------------------------------------------------------------------        
    def prepare_backtest_queue(self, filename):
        # 数据包回放测试。把数据包压入回测队列queue

        filesize = os.path.getsize(filename)  
        with open(filename,'rb') as fo:
            while True:
                #t = time.perf_counter()
                datahead = fo.read(sizeof(OEM_DATA_HEAD))
                if datahead:
                    wshead_unit = OEM_DATA_HEAD()
                    wshead_unit.decode(datahead)  #把字节流 转成 ctypes结构体
                    #wsheadinfo = "ws data head info:\r\n[oemVer:%s] x [type:%s] x [label:%s] x [name:%s] x [flag:%s] x [askId:%s] x [len:%s] x [count:%s]" \
                    #    % (wshead_unit.oemVer, wshead_unit.type, wshead_unit.label, wshead_unit.name, wshead_unit.flag, wshead_unit.askId, wshead_unit.len, wshead_unit.count)
                    #print(wsheadinfo)
                     
                    databody = fo.read(wshead_unit.len)
                    databody1 = databody
                    
                    if databody:
                        self._backtest_rawdata_queue.put(datahead + databody)
                        """
                        #过滤数据包： 只取指定代码的实时行情 和 K线
                        #if self.is_klines_type(wshead_unit.type) and (wshead_unit.label =='SH600000' or wshead_unit.label =='SH600007' or wshead_unit.label =='SH600010'):
                        #    self._backtest_rawdata_queue.put(datahead + databody)
                        if wshead_unit.type == '实时数据':
                            for i in range(wshead_unit.count):
                                reportbody = OEM_REPORT()
                                reportbody.decode(databody1)               #字节流 转成 ctypes结构体

                                if reportbody.label == 'SH600000' or reportbody.label =='SH600007' or reportbody.label =='SH600010':
                                    self._backtest_rawdata_queue.put(datahead + databody)

                                databody1 = databody1[sizeof(OEM_REPORT) : ]  #删除一个结构体
                        else:
                            self._backtest_rawdata_queue.put(datahead + databody)
                        """
                        

                    else: # 已经读到文件尾
                        break

                else: # 已经读到文件尾
                    break
                #print(f'coast:{time.perf_counter() - t:.8f}s')
        fo.close()

        """ bytes切片超级慢，还不如直接读文件快
        while(len(bktestdata)>0):
            #t = time.perf_counter()
            wshead_unit = OEM_DATA_HEAD()
            wshead_unit.decode(bktestdata)  #把字节流 转成 ctypes结构体
            #wsheadinfo = "ws data head info:\r\n[oemVer:%s] x [type:%s] x [label:%s] x [name:%s] x [flag:%s] x [askId:%s] x [len:%s] x [count:%s]" \
            #    % (wshead_unit.oemVer, wshead_unit.type, wshead_unit.label, wshead_unit.name, wshead_unit.flag, wshead_unit.askId, wshead_unit.len, wshead_unit.count)
            #print(wsheadinfo)

            length_unit = sizeof(OEM_DATA_HEAD) + wshead_unit.len
            wsbody_unit = bktestdata[0: length_unit]

            self._backtest_rawdata_queue.put_nowait(wsbody_unit)
            
            bktestdata = bktestdata[length_unit : ] #取出一段完整的命令响应
            #print(f'coast:{time.perf_counter() - t:.8f}s')
        """
                


    def start_me(self):

        # 启动队列处理子线程 
        self.processqueuethread_stopevent.clear()
        self.processqueuethread = threading.Thread(target=self.process_queue_thread, args=(self.processqueuethread_stopevent,))
        self.processqueuethread.start()
        
        self.sendwscommandthread_stopevent.clear()
        self.sendwscommandthread = threading.Thread(target=self.send_wscommand_thread, args=(self.sendwscommandthread_stopevent,))
        self.sendwscommandthread.start()  

        if self._playmode == NPSDKAPI_PLAYMODE_BACKTEST: # 数据包回放测试，准备数据包
            print('数据包回放测试...')
            print('数据包个数： %s'%self._backtest_rawdata_queue.qsize())
            self._start_backtest_flag = True
            

        """ 主线程体 """
        while True:
            if self._playmode == NPSDKAPI_PLAYMODE_WEBSOCKET: # 正常情况连接Websocket
                self.Connect()
                if self.m_stop: 
                    break

            time.sleep(0.1)
        #print("websocket close and exit from the loop")
    
    
    def stop_me(self):
        self._stopped_flag = True #停止使用Queue发送消息

        self.m_logined = NPSDKAPI_WS_DISCONNECTED
        self.m_stop = True
        self.on_close()
        self.m_ws.close() #关闭websocket

        self.processqueuethread_stopevent.set() # 停止该线程: 设置Event为True,使之从while loop中退出
        self.processqueuethread.join()
        self.sendwscommandthread_stopevent.set() # 停止该线程: 设置Event为True,使之从while loop中退出
        self.sendwscommandthread.join()

        # 如果使用了Queue, Python会派生daemon性质的QueueFeederThread, 需要释放Queue
        self._ws_message_queue.join()
        self._ws_message_queue.close()
        self._ws_command_queue.join()
        self._ws_command_queue.close()
        #self._async_raise(self.sendwscommandthread.ident, SystemExit)
        logger.info("当前线程数量: %d  \r\n线程是：%s" % (len(threading.enumerate()), str(threading.enumerate())))

    """
    主线程入口函数：调用npdatapoolthread.start()即进入run()
    """
    def run(self):
        self.start_me()  



    # ----------------------------------------------------------------------
    """""""""""""""""""""""""""""""""""""""""""""
    子线程（队列处理线程）: 功能：
    1. 接收并分析来自websocket的业务数据, 
       更新内存数据池中的业务数据字典
    .....
    2. 接收并分析来自npsdkapi的命令
    """""""""""""""""""""""""""""""""""""""""""""
    def process_queue_thread(self, stop_event):

        """ added by xxg in 2021.5.5
        本地业务数据内存截面
        1. 市场代码表 
        2. 实时行情 
        3. ...
        4. ...
        """
        glb_marketinfo_dict = {} # 市场表 证券代码表 数据字典
        glb_marketinfo_dict.clear()

        glb_stk_report_dict = {} # 证券实时行情 数据字典
                                        # {
                                        #   'SH600000':OEM_REPORT,
                                        #   'SH600007':OEM_REPORT,
                                        #   ......
                                        #   'SH600100':OEM_REPORT,
                                        #   'SH600101':OEM_REPORT,
                                        # }
        glb_stk_report_dict.clear()

        #["1分钟线", "5分钟线", "15分钟线", "30分钟线", "60分钟线", "日线", "周线", "月线", "季线", "年线", "多日线"]
        glb_stk_klines_dict = {} # 证券K线数据 数据字典 
                                        # {                      [RCV_KLINE,RCV_KLINE,RCV_KLINE,]
                                        #   'SH600000':{'1分钟线':原始数据字节流,    
                                        #               '5分钟线':原始数据字节流, 
                                        #               ......
                                        #              },
                                        #   ......
                                        #   'SH600007':{'1分钟线':原始数据字节流,
                                        #               '日线':   原始数据字节流, 
                                        #               ......
                                        #              },
                                        # }
        glb_stk_klines_dict.clear()

        glb_wscommands_set = set()       # websocket commands set


        """    
        从_ws_message_queue中取出wsmessage
        返回：元组(bool, message)
        """
        def get_wsmessage_queue():   
            wsmessage = ''
            
            try:
                #with self.internal_lock:    
                    if self._stopped_flag: 
                        return False, wsmessage 
                
                    if not self._ws_message_queue.empty():
                        wsmessage = self._ws_message_queue.get()  #get_nowait() 
                        #self._ws_message_queue.task_done()
                        return True, wsmessage  
                    else:
                        return False, wsmessage  
            except Exception as e:
                logger.warning('get_wsmessage_queue() exception: %r'% e)
                return False, wsmessage 


        """""""""""""""""""""""""""""""""""""""""""""    
        检查来自websocket的数据
        """""""""""""""""""""""""""""""""""""""""""""
        def check_queue_from_npdatapool():

            bret, wsmessage = get_wsmessage_queue()
            if bret: #成功取得一条message   
                
                if len(wsmessage) == 0 or len(wsmessage) < sizeof(OEM_DATA_HEAD) :
                    # 接收到的消息长度为0 或者 小于OEM_DATA_HEAD结构体长度，则为错误消息，立即返回
                    print('错误消息: 接收到的消息 长度为0或者小于OEM_DATA_HEAD结构体长度')
                    logger.error('错误消息: 接收到的消息 长度为0或者小于OEM_DATA_HEAD结构体长度')
                    return 

                """
                message = HEAD + BODY
                HEAD: (100字节)
                """
                wshead = OEM_DATA_HEAD()
                wshead.decode(wsmessage)  #把字节流 转成 ctypes结构体
                
                wsheadinfo = "ws data head info:\r\n[oemVer:%s] x [type:%s] x [label:%s] x [name:%s] x [flag:%s] x [askId:%s] x [len:%s] x [count:%s]" \
                % (wshead.oemVer, wshead.type, wshead.label, wshead.name, wshead.flag, wshead.askId, wshead.len, wshead.count)
                #print(wsheadinfo)
                logger.info(wsheadinfo)

                """
                message = HEAD + BODY
                BODY: (可变长度)
                """
                wsbody = wsmessage
                wsbody = wsmessage[sizeof(OEM_DATA_HEAD) : ] # 取出 wsbody

                msgtype   = wshead.type            #消息类型
                #headsize   = sizeof(OEM_DATA_HEAD)  #100 字节

                """
                # 这里默认为websocket server 一次性发送的字节流都是完整的业务数据流，不存在没发完的残留数据
                # 需要大消息体测试 (比如一次性收 几千根Kline数据)
                """ 

                if msgtype == '代码表':
                    pass
                
                
                #-"""实时行情数据处理"""-#
                elif msgtype == '实时数据':  
                    if len(wsbody) == 0 or len(wsbody) != wshead.count * sizeof(OEM_REPORT):
                        # 接收到的实时行情消息体长度为0 或者 实际长度不等于count*sizeof(OEM_REPORT)，则为错误消息，立即返回
                        print('错误消息: 接收到的实时行情消息体长度为0 或者 实际长度不等于count*sizeof(OEM_REPORT)')
                        logger.error('错误消息: 接收到的实时行情消息体长度为0 或者 实际长度不等于count*sizeof(OEM_REPORT)')
                        return 

                    for i in range(wshead.count):
                        reportbody = OEM_REPORT()
                        reportbody.decode(wsbody)               #字节流 转成 ctypes结构体
                        wsbody = wsbody[sizeof(OEM_REPORT) : ]  #删除一个结构体
                        #print(reportbody.label, reportbody.name)
                        #print('wsbody len%s'% len(wsbody))

                        """
                        待加功能：在代码表里检查 reportbody.label 是否为有效证券代码
                        """
                        
                         #以证券代码为key值 更新实时行情字典 
                        glb_stk_report_dict[reportbody.label] = reportbody   
                        #print('更新实时行情数据字典: %s len of dict：%s'% (reportbody.label, len(glb_stk_report_dict)))

                        """
                        if reportbody.label == 'SH600000' :
                            tm = time.localtime(reportbody.time)
                            tmStr = time.strftime('%Y-%m-%d %H:%M:%S', tm)
                            print("接收到实时行情: %s(%s) : time:%s close : %0.2f" % (reportbody.label, reportbody.name, tmStr, reportbody.close))
                        """
                    #print('---------------len(report dict):%s'%len(glb_stk_report_dict))
                
                #-"""K线数据处理"""-#
                elif self.is_klines_type(msgtype):

                    #logger.info(wsbody) 
                    if len(wsbody) == 0 or len(wsbody) != wshead.count * sizeof(RCV_KLINE):
                        # 接收到的实时行情消息体长度为0 或者 实际长度不等于count*sizeof(RCV_KLINE)，则为错误消息，立即返回
                        print('错误消息: 接收到的K线数据消息体长度为0 或者 实际长度不等于count*sizeof(RCV_KLINE)')
                        logger.error('错误消息: 接收到的K线数据消息体长度为0 或者 实际长度不等于count*sizeof(RCV_KLINE)')
                        return

                    symbol = wshead.label       #证券代码
                    klines_type = wshead.type   #Klines类型字符串

                    """
                    待加功能：在代码表里检查 wshead.label 是否为有效证券代码
                    """

                    #以证券代码为key值 更新K线数据一级字典。以K线类型为key值 更新K线数据二级字典。
                    if  symbol in glb_stk_klines_dict.keys():
                        glb_stk_klines_dict[symbol][klines_type] = wsbody 
                    else: # 该证券代码第一次传送K线数据
                        klines_dict = {}
                        klines_dict[klines_type] = wsbody
                        glb_stk_klines_dict[symbol] = klines_dict
                    
                    """
                    if wshead.label == 'SH600000' :
                        tm = time.localtime()
                        tmStr = time.strftime('%Y-%m-%d %H:%M:%S', tm)
                        print("接收到K线数据: %s(%s) : time:%s " % (wshead.label, wshead.name, tmStr))
                    """
                
                elif msgtype == '分时' or msgtype == '分笔' :
                    pass
                
                elif msgtype == '除权':
                    pass

                elif msgtype == '财务' :
                    pass

                elif msgtype == 'F10资料' :                 
                    pass


        """    
        从command_queue中取出命令
        返回：元组(bool, NpApiDataObj)
        """
        def get_command_queue():   
            npapidataobj = NpApiDataObj()
            
            try:
                #with self.internal_lock:                   
                    if self._stopped_flag: 
                        return False, npapidataobj 

                    if not self._command_queue.empty():
                        npapidataobj = self._command_queue.get()  #get_nowait() 
                        #self._command_queue.task_done()
                        return True, npapidataobj  
                    else:
                        return False, npapidataobj  
            except Exception as e:
                logger.warning('get_command_queue() exception: %r'% e)
                return False, npapidataobj 

        """    
        向response_queue中压入命令数据响应
        返回：bool
        """
        def put_response_queue(npapidataobj):  
            try:
                #with self.internal_lock:                      
                    if self._stopped_flag: 
                        return False 
             
                    if not self._response_queue.full():
                        self._response_queue.put(npapidataobj) #put_nowait()
                        return True
                    else:
                        return False
            except Exception as e:
                logger.warning('put_response_queue() exception: %r'% e)
                return False

        """    
        向ws_command_queue中压入wscommand命令
        返回：bool
        """
        def put_wscommands_queue(_wscommands):  
            try:
                #with self.internal_lock:                      
                    if self._stopped_flag: 
                        return False 
             
                    if not self._ws_command_queue.full():
                        self._ws_command_queue.put(_wscommands) #put_nowait()
                        return True
                    else:
                        return False
            except Exception as e:
                logger.warning('put_wscommands_queue() exception: %r'% e)
                return False
        
        """""""""""""""""""""""""""""""""""""""""""""    
        检查是否有NpSdkApi队列任务
        """""""""""""""""""""""""""""""""""""""""""""
        def check_queue_from_npsdkapi():

            bret, npapidataobj = get_command_queue()
            #print('datapool: cmd_queue(size:%s:%s) msg_queue(size:%s)'%(self._command_queue.qsize(), bret, self._ws_message_queue.qsize()))

            if bret: #成功取得一条命令
                app_id = npapidataobj.app_id

                if app_id == NPSDKAPI_APPID_NPSDKAPI: #该消息为策略程序请求命令
                    #print("got command from command_queue...app_id: %s, message_id: %s, request_body: %s"%\
                    #    (npapidataobj.app_id, npapidataobj.message_id, npapidataobj.request_body))
                    
                    if npapidataobj.message_id == NPSDKAPI_MESSAGEID_GETQUOTE_REQ: 
                        """
                        获取指定代码的实时行情
                        """
                        bsuc, npapiobj = get_quote_remote(npapidataobj) 
                        
                        """
                        返回指定代码的实时行情数据
                        """
                        if bsuc:
                            put_response_queue(npapiobj)

                   
                    elif npapidataobj.message_id == NPSDKAPI_MESSAGEID_GETKLINES_REQ: 
                        """
                        获取指定代码的K线数据
                        """
                        bsuc, npapiobj = get_kline_serial_remote(npapidataobj) 
                        
                        """
                        返回指定代码的K线数据
                        """
                        if bsuc:
                            put_response_queue(npapiobj)

                        
                    elif npapidataobj.message_id == NPSDKAPI_MESSAGEID_WSCOMMAND_REQ: #向websocket server发送命令请求数据
                        
                        # 监控队列长度，如果队列长度太大表示消息堆积
                        if self._ws_message_queue.qsize() > NPSDKAPI_QUEUESZIE_WARNING:
                            logger.warning('(wsmsg_queue: %s) (wscmd_queue: %s) (response_queue: %s) (command_queue: %s)' \
                                %(self._ws_message_queue.qsize(), self._ws_command_queue.qsize(), self._response_queue.qsize(), self._command_queue.qsize()))
                        #print('wsmsg_queue:%s wscmd_queue:%s response_queue:%s command_queue:%s'%(self._ws_message_queue.qsize(), self._ws_command_queue.qsize(), self._response_queue.qsize(), self._command_queue.qsize()))
                    
                        if self._playmode == NPSDKAPI_PLAYMODE_WEBSOCKET: # 正常情况连接Websocket
                            logger.info('send ws command: %s' % npapidataobj.request_body)
                            logger.info(npapidataobj.request_body)
                            self.send_command_over_ws(npapidataobj.request_body)

                            glb_wscommands_set.add(npapidataobj.request_body) # 汇集各路websocket commands命令用set去重
                            #print(glb_wscommands_set)
                            #put_wscommands_queue(glb_wscommands_set)

                        elif self._playmode == NPSDKAPI_PLAYMODE_BACKTEST: # 本地数据包回放测试
                            # 数据包回放测试 
                            if self._start_backtest_flag:
                                #print('数据包回放测试...... 第%s个数据包' % self._backtest_rawdata_queue.qsize())
                                message = self._backtest_rawdata_queue.get()
                                self.on_message(message)
                                time.sleep(0.1)

                                if self._backtest_rawdata_queue.qsize() == 0:
                                    self._start_backtest_flag = False
                                    print('数据包回放测试结束')
                        else:
                            pass

                    else: #其它命令
                        pass

                else: # 没有收到来自 NPSDKAPI_APPID_NPSDKAPI 的命令
                    pass


        """
        get_quote_remote函数体
        返回：元组（bool, NpApiDataObj）
        """
        def get_quote_remote(npapiobjsrc):
            """ 
            在数据池里查找实时行情业务数据，
            """         
            npapiobjdes = NpApiDataObj()
            npapiobjdes.app_id = NPSDKAPI_APPID_NPSDKDATA
            npapiobjdes.message_id = NPSDKAPI_MESSAGEID_GETQUOTE_RES
            npapiobjdes.correlation_id = npapiobjsrc.correlation_id
            npapiobjdes.reply_to = npapiobjsrc.reply_to
            npapiobjdes.response_type = ''
            npapiobjdes.response_body = ''

            try:                                      
                codekey = npapiobjsrc.request_body#(npapiobjsrc.request_body).decode()
            except Exception as e:
                logprtstr ='get_quote_remote() exception with codekey: %r'% e
                logger.warning(logprtstr)
                npapiobjdes.response_body = 'error: ' + logprtstr
                npapiobjdes.response_type = NPSDKAPI_ERROR
                return False, npapiobjdes

            # 快速查找实时行情字典
            if  codekey in glb_stk_report_dict: 
                reportbody = glb_stk_report_dict[codekey]
                #print("found codekey:%s label: %s in 实时行情字典"% (codekey, reportbody.label))
                
                if reportbody:
                    #print("在实时行情字典中找到 %s 开盘价(%s) 最新价(%s)" % (reportbody.label, reportbody.open, reportbody.close))
                    #logger.info("在实时行情字典中找到codekey")
                    
                    npapiobjdes.response_body = reportbody.encode() # 把ctypes结构体转成字节流
                    npapiobjdes.response_type = NPSDKAPI_SUCCESS

                    return True, npapiobjdes 
                else:
                    logprtstr = "在实时行情字典中找到codekey：%s，但是对应的数据体为空"% codekey
                    logger.warning(logprtstr)
                    npapiobjdes.response_body = 'error: ' + logprtstr 
                    npapiobjdes.response_type = NPSDKAPI_ERROR
                    return False, npapiobjdes
            
            else:
                logprtstr = "在实时行情字典中没找到codekey:%s "% codekey
                logger.warning(logprtstr)
                npapiobjdes.response_body = 'error: ' +  logprtstr
                npapiobjdes.response_type = NPSDKAPI_ERROR  
                return False, npapiobjdes

        """
        get_kline_serial_remote函数体
        返回：元组（bool, NpApiDataObj）
        """
        def get_kline_serial_remote(npapiobjsrc):
            """ 
            在数据池里查找K线业务数据，
            """         
            npapiobjdes = NpApiDataObj()
            npapiobjdes.app_id = NPSDKAPI_APPID_NPSDKDATA
            npapiobjdes.message_id = NPSDKAPI_MESSAGEID_GETKLINES_RES
            npapiobjdes.correlation_id = npapiobjsrc.correlation_id
            npapiobjdes.reply_to = npapiobjsrc.reply_to
            npapiobjdes.response_type = ''
            npapiobjdes.response_body = ''

            try:                               
                # 分析参数  symbol + '?' + klines_type_str  # 格式: 格式: 'SH600000?1分钟线'  
                requestbody = npapiobjsrc.request_body.split('?')
                codekey = requestbody[0] #指定代码
                klines_type = requestbody[1] #K线类型

            except Exception as e:
                logprtstr = 'get_kline_serial_remote() exception with requestbody: %r'% e
                logger.warning(logprtstr)
                npapiobjdes.response_body = 'error: ' + logprtstr
                npapiobjdes.response_type = NPSDKAPI_ERROR
                return False, npapiobjdes

            # 快速查找K线字典: 在一级字典找到指定代码且同时在二级字典找到K线类别
            
            if  codekey in glb_stk_klines_dict.keys():
                if klines_type in glb_stk_klines_dict[codekey].keys():
                    kline_rawdata = glb_stk_klines_dict[codekey][klines_type]
                    
                    if kline_rawdata:
                        npapiobjdes.response_body = kline_rawdata
                        npapiobjdes.response_type = NPSDKAPI_SUCCESS
                        return True, npapiobjdes 
                    else:
                        logprtstr = "在K线数据字典中找到(codekey %s:klinestype %s), 但是对应的数据体为空"% (codekey, klines_type)
                        logger.warning(logprtstr)
                        npapiobjdes.response_body = 'error: ' + logprtstr
                        npapiobjdes.response_type = NPSDKAPI_ERROR
                        return False, npapiobjdes
                else:
                    logprtstr = "在K线数据字典中找到codekey %s 但没找到klinestype %s"% (codekey, klines_type)
                    logger.warning(logprtstr)
                    npapiobjdes.response_body = 'error: ' + logprtstr
                    npapiobjdes.response_type = NPSDKAPI_ERROR
                    return False, npapiobjdes
            else:
                logprtstr = "在K线数据字典中没找到codekey:%s "% codekey
                logger.warning(logprtstr)
                npapiobjdes.response_body = 'error: ' + logprtstr
                npapiobjdes.response_type = NPSDKAPI_ERROR  
                return False, npapiobjdes

        """
        子线程（队列处理线程）线程体
        """
        while not stop_event.is_set():
            # check queue if has ws message from npdata and update data in memory dict
            check_queue_from_npdatapool()

            # check queue from npsdkapi if has data request
            check_queue_from_npsdkapi()

            """
            由于websocket的数据消息可能会很多, check_queue_from_npdatapool()函数会占有大量时间片
            为了尽快处理来自npsdkapi发来的_command_queue任务，sleep值不能太大
            """
            time.sleep(0.0001)  
        #print('process_queue_thread exit from the loop')




    # ----------------------------------------------------------------------
    """
    子线程（基于websocket的数据请求命令线程）: 功能：
    1. 根据业务类型设置定时器任务发送数据请求命令 （避免频繁发送命令）
    2. 发送基于websocket的数据请求命令
    """
    def send_wscommand_thread(self, stop_event): 

        """    
        从_ws_command_queue中取出wscommand
        返回：元组(bool, command)
        """
        def get_wscommands_queue()->set:   
            _wscommands = set()
            
            try:
                #with self.internal_lock:    
                    if self._stopped_flag: 
                        return False, _wscommands 
                
                    if not self._ws_command_queue.empty():
                        _wscommands = self._ws_command_queue.get()  #get_nowait() 
                        #self._ws_command_queue.task_done()
                        return True, _wscommands  
                    else:
                        return False, _wscommands  
            except Exception as e:
                logger.warning('get_wscommands_queue() exception: %r'% e)
                return False, _wscommands 

        #子线程（队列处理线程）线程体
        while not stop_event.is_set():
            
            #print('wscommand_queue:%s '%self._ws_command_queue.qsize())
            bret, wscommands = get_wscommands_queue() #把wscommand加入集合达到去重的目的
            if bret: #成功取得一个wscommand命令集合
                #print(wscommands)

                #for wsc in wscommands:
                #    logger.info('send ws command: %s' % wsc)
                #    logger.info(wsc)
                #    self.send_command_over_ws(wsc)
                #    time.sleep(0.2)
                pass

            time.sleep(3)
    
    """
    def OnAsk(self):
        if self.m_logined != NPSDKAPI_WS_CONNECTED:
            return
    """

 
    






        
