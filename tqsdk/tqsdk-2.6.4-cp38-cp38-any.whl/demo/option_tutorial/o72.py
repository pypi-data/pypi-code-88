from tqsdk import TqApi, TqAuth
from datetime import datetime
from tqsdk.tafunc import time_to_datetime

'''
获取标的对应看涨期权的期权和距离下市的剩余天数
'''
api = TqApi(auth=TqAuth("信易账户", "账户密码"))

# 获取沪深300股指期权的认购在市合约
ls = api.query_options("SSE.000300", "CALL", expired=False)

# 批量获取这些合约的quote合约信息
quote_ls = api.get_quote_list(ls)

option_ls = {}

# 遍历quote合约信息，将合约和其对期权剩余到期天数组成字典
for i in quote_ls:
    option_ls[i.instrument_id] = (time_to_datetime(i.expire_datetime) - datetime.now()).days

print(option_ls)

api.close()
