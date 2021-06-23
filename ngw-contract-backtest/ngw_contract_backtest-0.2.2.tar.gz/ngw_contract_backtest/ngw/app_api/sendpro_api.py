__author__ = 'wangjian'
import json
import requests
import traceback

def exchange2num(exchange):
    if exchange is None:
        return 4
    # 中金所
    elif exchange == 'CFFEX':
        return 3
    # 上期所
    elif exchange == 'SHFE':
        return 4
    # 大商所
    elif exchange == 'DCE':
        return 5
    # 郑商所
    elif exchange == 'CZCE':
        return 6
    # 上海国际能源交易中心
    elif exchange == 'INE':
        return 15

# 策略信号新增
def SendOrderPro(stgyId=None,symbol=None,exchange=None,side=None,quantity=None,price=None):
    exchange_num = exchange2num(exchange)
    side_offset = {'open_long': [66, 1], 'close_long': [83, 2], 'open_short': [83, 1], 'close_short': [66, 2]}
    side_, offset = side_offset[side]
    body = {
          "stgyId": stgyId,
          "symbol": symbol,
          "exchange": exchange_num,
          "orderSide": side_,
          "offset": offset,
          "quantity": int(quantity),
          "price": price,
          "orderType": 1,
          "note": ''
    }
    # print(body)
    # url = 'https://dev-stgyapi.inquant.cn/future/papertrade/sendorder'  # 开发
    # url = 'https://test-stgyapi.inquant.cn/future/papertrade/sendorder'  # 测试
    url = 'https://stgyapi.inquant.cn/future/papertrade/sendorder'  # 线上
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6",
            "Content-Type": "application/x-www-form-urlencoded"}
        response = requests.post(url, data=json.dumps(body), headers=headers)
        response.close()
    except Exception:
        print(traceback.format_exc())
        return None
    else:
        response = response.content.decode()
        response_json = json.loads(response)
        if response_json['error_no'] == 0:
            return int(response_json['data'])
        else:
            print(response_json)
            return 0
