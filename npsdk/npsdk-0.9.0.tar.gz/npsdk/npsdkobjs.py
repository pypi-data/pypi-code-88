#:!/usr/bin/env python
#:  -*- coding: utf-8 -*-
__author__ = 'xxg'

from Stockdrv import *
from ctypes import *

"""
NPSDK 全局常量定义
"""

NPSDKAPI_APPID_NPSDKAPI  = 'npsdkapi'
NPSDKAPI_APPID_NPSDKDATA = 'npsdkdata'

NPSDKAPI_MESSAGEID_GETQUOTE_REQ     = 'get_quote'
NPSDKAPI_MESSAGEID_GETQUOTE_RES     = 'get_quote_response'
NPSDKAPI_MESSAGEID_GETKLINES_REQ    = 'get_klines'
NPSDKAPI_MESSAGEID_GETKLINES_RES    = 'get_klines_response'

NPSDKAPI_MESSAGEID_WSCOMMAND_REQ    = 'ws_command_request'
NPSDKAPI_MESSAGEID_WSCOMMAND_RES    = 'ws_command_response'    

NPSDKAPI_SUCCESS        = 'npsdkapi_success'
NPSDKAPI_ERROR          = 'npsdkapi_error'
NPSDKAPI_TIMEOUT        = 'npsdkapi_timeout'

NPSDKAPI_TIMEOUT_VAL    = 0.5 # 单位:secs, 命令请求超时阈值

NPSDKAPI_WS_CONNECTED           = 10
NPSDKAPI_WS_DISCONNECTED        = 0

NPSDKAPI_QUEUESZIE_WARNING      = 5000 # Websocket接收数据队列大小监控阈值，队列长度太大表示消息已经堆积

NPSDKAPI_PLAYMODE_WEBSOCKET     = 'websocket'   
NPSDKAPI_PLAYMODE_BACKTEST     = 'backtest'


#from tqsdk.diff import _get_obj
#from entity import Entity

""" Pika BasicProperties  详细说明https://www.pianshen.com/article/19451397954/
        content_type            用于描述消息内容的数据格式，如：text/plain
        content_encoding        消息内容编码
        headers                 设置消息的header,类型为Map<String,Object>
        delivery_mode           1（nopersistent）非持久化，2（persistent）持久化
        priority                消息的优先级
        correlation_id          关联ID
        reply_to                用于指定回复的队列的名称
        expiration              消息的失效时间
        message_id              消息ID
        timestamp               消息的时间戳
        type                    类型
        user_id                 用户ID
        app_id                  应用程序ID
        cluster_id              集群ID

"""

class AplEventContentObject(object):
    """ 
    NpSdkApi user-defined event content object class (application level)
    """
    def __init__(self):
        self.apl_tid_source = ''        # application level ID,such as 'DATA_POOL_ID','WS_SOCKET_ID','NPSDKAPI_ID'
        self.apl_tid_destination = ''
        self.apl_event_name = None
        self.apl_event_body = ''


class NpApiDataObj(object):
    """ 
    NpApi user-defined data object class 
    """
    def __init__(self):
        
        """
        应用ID, 用来标识应用 
                * NPSDKAPI_APPID_NPSDKAPI   策略程序
                * NPSDKAPI_APPID_NPSDKDATA  数据服务器
                * ......
        """
        self.app_id = None

        """
        消息ID，用来描述函数命令： 
                * NPSDKAPI_MESSAGEID_GETQUOTE_REQ            获取实时数据命令
                * NPSDKAPI_MESSAGEID_GETQUOTE_RES            获取实时数据响应
                * NPSDKAPI_MESSAGEID_GETKLINES_REQ           获取K线数据命令
                * NPSDKAPI_MESSAGEID_GETKLINES_RES           获取K线数据响应
                *
                * NPSDKAPI_MESSAGEID_WSCOMMAND_REQ           ws command 请求命令
                * NPSDKAPI_MESSAGEID_WSCOMMAND_RES           ws command 请求命令响应
                * .....
        """
        self.message_id = None 

        # 回复队列
        self.reply_to = None

        #: 关联ID
        self.correlation_id = None

        #: 请求消息参数体
        self.request_body = None

        """
        响应消息类型, 对应BasicProperties里的tpye
                * NPSDKAPI_SUCCESS:     命令请求成功
                * NPSDKAPI_ERROR:       命令请求出错
                * NPSDKAPI_TIMEOUT:     命令请求超时
                * ....
        """
        self.response_type = None 

        #: 响应消息体
        self.response_body = None

    def _instance_entity(self, path):
        pass
        #super(Quote, self)._instance_entity(path)
        #self.trading_time = copy.copy(self.trading_time)
        #self.trading_time._instance_entity(path + ["trading_time"])

"""
class Quote(Entity):
    #Quote 是一个行情对象 

    def __init__(self, api):
        self._api = api
        #: 行情从交易所发出的时间(北京时间), 格式为 "2017-07-26 23:04:21.000001"
        self.datetime = ""
        #: 卖一价
        self.ask_price1 = float("nan")
        #: 卖一量
        self.ask_volume1 = 0
        #: 买一价
        self.bid_price1 = float("nan")
        #: 买一量
        self.bid_volume1 = 0
        #: 卖二价
        self.ask_price2 = float("nan")
        #: 卖二量
        self.ask_volume2 = 0
        #: 买二价
        self.bid_price2 = float("nan")
        #: 买二量
        self.bid_volume2 = 0
        #: 卖三价
        self.ask_price3 = float("nan")
        #: 卖三量
        self.ask_volume3 = 0
        #: 买三价
        self.bid_price3 = float("nan")
        #: 买三量
        self.bid_volume3 = 0
        #: 卖四价
        self.ask_price4 = float("nan")
        #: 卖四量
        self.ask_volume4 = 0
        #: 买四价
        self.bid_price4 = float("nan")
        #: 买四量
        self.bid_volume4 = 0
        #: 卖五价
        self.ask_price5 = float("nan")
        #: 卖五量
        self.ask_volume5 = 0
        #: 买五价
        self.bid_price5 = float("nan")
        #: 买五量
        self.bid_volume5 = 0
        #: 最新价
        self.last_price = float("nan")
        #: 当日最高价
        self.highest = float("nan")
        #: 当日最低价
        self.lowest = float("nan")
        #: 开盘价
        self.open = float("nan")
        #: 收盘价
        self.close = float("nan")
        #: 当日均价
        self.average = float("nan")
        #: 成交量
        self.volume = 0
        #: 成交额
        self.amount = float("nan")
        #: 持仓量
        self.open_interest = 0
        #: 结算价
        self.settlement = float("nan")
        #: 涨停价
        self.upper_limit = float("nan")
        #: 跌停价
        self.lower_limit = float("nan")
        #: 昨持仓量
        self.pre_open_interest = 0
        #: 昨结算价
        self.pre_settlement = float("nan")
        #: 昨收盘价
        self.pre_close = float("nan")
        #: 合约价格变动单位
        self.price_tick = float("nan")
        #: 合约价格小数位数
        self.price_decs = 0
        #: 合约乘数
        self.volume_multiple = 0
        #: 最大限价单手数
        self.max_limit_order_volume = 0
        #: 最大市价单手数
        self.max_market_order_volume = 0
        #: 最小限价单手数
        self.min_limit_order_volume = 0
        #: 最小市价单手数
        self.min_market_order_volume = 0
        #: 标的合约
        self.underlying_symbol = ""
        #: 行权价
        self.strike_price = float("nan")
        #: 合约类型
        self.ins_class = ""
        #: 交易所内的合约代码
        self.instrument_id = ""
        #: 交易所代码
        self.exchange_id = ""
        #: 合约是否已下市
        self.expired = False
        #: 交易时间段
        self.trading_time = TradingTime(self._api)
        #: 到期具体日
        self.expire_datetime = float("nan")
        #: 到期月
        self.delivery_month = 0
        #: 到期年
        self.delivery_year = 0
        #: 期权方向
        self.option_class = ""
        #: 品种代码
        self.product_id = ""
        #: ETF实时单位基金净值
        self.iopv = float("nan")

    def _instance_entity(self, path):
        super(Quote, self)._instance_entity(path)
        self.trading_time = copy.copy(self.trading_time)
        self.trading_time._instance_entity(path + ["trading_time"])
"""

