# -*- coding: utf-8 -*-

import os; os.chdir("S:/siateng")
from siate import *
#==============================================================================
ytmchanges = [-100, -50, -20, -10, -5, 5, 10, 20, 50, 100]
bond_malkiel1(0.06, 8, 0.07, 100, 2, ytmchanges)

maturitylist = [1, 2, 3, 5, 10, 15, 20, 30]
bond_malkiel2(0.06, 8, 0.07, 100, 2, maturitylist)

bond_malkiel3(0.06, 8, 0.07, 100, 2)

bond_malkiel4(0.06, 8, 0.07, 100, 2)

bond_malkiel5(0.06, 8, 0.07, 100, 2)

bond_malkiel5(0.08, 10, 0.1, 100, 4)
#==============================================================================
ibbd=interbank_bond_deal(10,option='1')

ibbd=interbank_bond_deal(10,option='4')
ibbd=interbank_bond_deal(100,option='6')

ebd=exchange_bond_deal(10, option='4')
ebp=exchange_bond_price('sh019521', '2019-7-1', '2020-3-31')
ebp=exchange_bond_price('sz123027', '2021-1-1', '2021-5-31')

#==============================================================================
symbol='sh019521'
fromdate='2019-7-1'
todate='2020-3-31'
power=4

def exchange_bond_price(symbol,fromdate,todate,power=4):
    """
    功能：获得沪深债券市场历史成交行情
    输入：沪深债券代码symbol，起始日期fromdate，截止日期todate。
    返回：历史价格df
    输出：折线图
    """
    #检查日期期间的合理性
    result,start,end=check_period(fromdate, todate)
    if result is None: return None
    
    #抓取历史行情
    import akshare as ak
    try:
        df=ak.bond_zh_hs_daily(symbol=symbol)
    except:
        print("  #Error(exchange_bond_price), failed to get bond info of",symbol)
        return None
    
    #过滤日期期间：比较时需要注意时区
    starttz=start.tz_localize('UTC')
    endtz=end.tz_localize('UTC')
    df1=df.drop(df[df.index < starttz].index)
    df2=df1.drop(df1[df1.index > endtz].index)
    
    #绘图
    titletxt=texttranslate('沪深债券收盘价历史行情：')+codetranslate(symbol)
    import datetime
    today = datetime.date.today().strftime("%Y-%m-%d")
    footnote="\n"+texttranslate("数据来源：新浪财经，")+today    
    plot_line(df2,'close',texttranslate('收盘价'),texttranslate('价格'),titletxt,footnote,power=power)
    
    return df
#==============================================================================
ibbd=interbank_bond_deal(10)
ebp=exchange_bond_price('sh019521', '2021-3-1', '2021-5-25',power=0)
ebp=exchange_bond_price('sh122001', '2021-3-1', '2021-5-25',power=0)
#==============================================================================
def abcefg():
    """
    功能：获取当前函数名
    """
    import sys
    curfunc=sys._getframe().f_code.co_name  #获取当前函数名
    print(curfunc)
    
    uplfunc=sys._getframe(1).f_code.co_name #调用该函数的函数的名字，如果没有被调用，则返回<module>
    print(uplfunc)
    return

#==============================================================================
ibbq=interbank_bond_deal(10)
ibbq=interbank_bond_deal(10, option='5')

#==============================================================================
ebp=exchange_bond_price('sh019521', '2019-7-1', '2020-3-31')
ebp=exchange_covbond_price('sz128086','2020-1-1','2020-4-30')

cbp=country_bond_price('中国','中国1年期国债','2020-1-1','2020-4-30')
cbp=country_bond_price('美国','美国10年期国债','2020-1-1','2020-4-30')
cbp=country_bond_price('意大利','意大利30年期国债','2020-1-1','2020-4-30')


#==============================================================================
ibbi=interbank_bond_issue_detail('2012-1-1', '2020-12-31')
ibbim=interbank_bond_issue_monthly(ibbi,'2019-1-1', '2020-12-31')


#==============================================================================
if __name__=='__main__':
    search_bond_index_china(keystr='债')
    search_bond_index_china(keystr='国债') 
    search_bond_index_china(keystr='综合') 
    search_bond_index_china(keystr='金融') 
    search_bond_index_china(keystr='企业')
    search_bond_index_china(keystr='公司')
    search_bond_index_china(keystr='地方政府债')
    
    bond_index_china('中债-综合指数','2020-1-1','2021-2-8')
    bond_index_china('中债-国债总指数','2020-1-1','2021-2-8')
    bond_index_china('中债-交易所国债指数','2020-1-1','2021-2-8')    
    bond_index_china('中债-银行间国债指数','2010-1-1','2021-2-8')
    bond_index_china('中债-银行间债券总指数','2020-1-1','2021-2-8')
    
    bond_index_china('中债-5年期国债指数','2020-1-1','2021-2-8')
    bond_index_china('中债-0-3个月国债指数','2020-1-1','2021-2-8')




#==============================================================================
import os; os.chdir("S:/siat")
from siat.stock import *

compare_security(["300148.SZ","000001.SS"],"Close","2000-1-1","2020-6-30",twinx=True)

compare_security(["FRI","^GSPC"],"Exp Adj Ret%","2010-1-1","2020-6-30")

compare_security(["FRI","^GSPC"],"Exp Adj Ret Volatility%","2010-1-1","2020-6-30")

compare_security(["ICF","^DJI"],"Exp Adj Ret%","2010-1-1","2020-6-30")

compare_security(["ICF","^DJI"],"Exp Adj Ret Volatility%","2010-1-1","2020-6-30")



info=stock_price("510050.SS","2020-4-1","2020-6-30")
info=stock_price("510210.SS","2020-4-1","2020-6-30")

compare_security(["510210.SS","000001.SS"],"Close","2020-4-1","2020-6-30",twinx=True)

compare_security(["510210.SS","000001.SS"],"Close","2015-7-1","2020-6-30",twinx=True)

compare_security(["SPY","^GSPC"],"Exp Ret%","2010-1-1","2020-6-30")

compare_security(["VOO","^GSPC"],"Exp Ret%","2010-1-1","2020-6-30")

compare_security(["IVV","^GSPC"],"Exp Ret%","2010-1-1","2020-6-30")

compare_security(["SPY","^GSPC"],"Exp Ret Volatility%","2010-1-1","2020-6-30")

compare_security(["VOO","^GSPC"],"Exp Ret Volatility%","2010-1-1","2020-6-30")

compare_security(["IVV","^GSPC"],"Exp Ret Volatility%","2010-1-1","2020-6-30")

compare_security(["SPY","SPYD"],"Exp Ret%","2019-1-1","2020-6-30")

compare_security(["SPY","SPYG"],"Exp Ret%","2019-1-1","2020-6-30")

compare_security(["SPY","SPYV"],"Exp Ret%","2019-1-1","2020-6-30")


compare_security(["SPY","SPYD"],"Exp Ret Volatility%","2019-1-1","2020-6-30")

compare_security(["SPY","SPYG"],"Exp Ret Volatility%","2019-1-1","2020-6-30")

compare_security(["SPY","SPYV"],"Exp Ret Volatility%","2019-1-1","2020-6-30")



fsym = "ETH"; tsym = "USD"
begdate="2020-03-01"; enddate="2020-05-31"
markets=fetchCrypto_Exchange(fsym,tsym)
cp=fetchCrypto_Price_byExchList(fsym,tsym,markets,begdate,enddate)
dist1,dist2=calcSpread_in2Markets(cp)
print("Average inter-market spread:", dist1)
print("Inter-market spread volatility:", dist2)
