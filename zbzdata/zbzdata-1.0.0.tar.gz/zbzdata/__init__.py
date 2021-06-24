"""zdzdata 是知本竹数据(上海)有限公司针对银行估值风险计算需要用到的市场数据的python包
   涉及到的API主要包括：
   get_history：负责获取外汇(FX)、利率(IR)、商品(CM)、权益(EQ)四大类资产的历史行情数据
   get_bond_history：负责获取债券类资产的历史行情数据，来源包括上交所(SSE)，深交所(SZSE)和外汇交易中心(CFETS)
"""


__version__ = "0.1.0"
__author__ = ""


from zbzdata.history import (
     get_history,
     get_bond_history,
 )

