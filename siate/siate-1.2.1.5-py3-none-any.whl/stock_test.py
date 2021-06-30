# -*- coding: utf-8 -*-


import os; os.chdir("S:/siateng")
from siate import *
#==============================================================================
Kdemo=candlestick_demo("600519.SS", "2021-6-1", "2021-6-5")

p=get_price("0700.HK","2021-6-7","2021-6-11")

p2=get_price("600519.SS","2021-6-7","2021-6-11")


#==============================================================================
compare_security(['^IRX','^TYX'],"Close","2015-1-1","2018-12-31")
compare_security(['^IRX','^TYX'],"Close","2019-1-1","2019-8-31")
compare_security(['^IRX','^TYX'],"Close","2019-9-1","2019-12-31")


#==============================================================================
compare_stock(["000001.SS","399001.SZ"], "Close", "2010-1-1", "2021-5-29",twinx=True)
compare_stock(["000300.SS","000001.SS"], "Close", "2010-1-1", "2021-5-29",twinx=True)

compare_stock(["^HSI","000001.SS"], "Close", "2010-1-1", "2021-5-29",twinx=True)
compare_stock(["^N225","000001.SS"], "Close", "2010-1-1", "2021-5-29",twinx=True)
compare_stock(["^KS11","000001.SS"], "Close", "2010-1-1", "2021-5-29",twinx=True)
compare_stock(["^GSPC","000001.SS"], "Close", "2010-1-1", "2021-5-29",twinx=True)
compare_stock(["^DJI","^GSPC"], "Close", "2010-1-1", "2021-5-29",twinx=True)


compare_stock(["600583.SS","601808.SS"], "Close", "2021-1-1", "2021-5-29")
compare_stock(["600583.SS","600968.SS"], "Close", "2021-1-1", "2021-5-29")
#==============================================================================
fr1=get_stock_profile("0883.HK",info_type='fin_rates')
fr2=get_stock_profile("0857.HK",info_type='fin_rates')

fr1=get_stock_profile("1033.HK",info_type='fin_rates')
fr2=get_stock_profile("2883.HK",info_type='fin_rates')                      
fr3=get_stock_profile("SLB",info_type='fin_rates') 
fr4=get_stock_profile("2222.SR",info_type='fin_rates') 
fr5=get_stock_profile("HAL",info_type='fin_rates') 

info=get_stock_profile("AAPL",info_type='fin_rates')
info=get_stock_profile("AAPL",info_type='market_rates')
info=get_stock_profile("MSFT",info_type='fin_rates')
fs=get_stock_profile("AAPL",info_type='fin_statements')
#==============================================================================
compare_stock(["0883.HK","0857.HK"], "Close", "2010-1-1", "2021-5-18")
compare_stock(["0883.HK","0857.HK"], "Annual Ret%", "2010-1-1", "2021-5-18")
compare_stock(["0883.HK","0857.HK"], "Exp Ret%", "2010-1-1", "2021-5-18")
compare_stock(["0883.HK","0857.HK"], "Annual Ret Volatility%", "2010-1-1", "2021-5-18")
compare_stock(["0883.HK","0857.HK"], "Exp Ret Volatility%", "2010-1-1", "2021-5-18")

from siat.financials import *
compare_history(["0883.HK","0857.HK"], "Cashflow per Share")

tickers=["0883.HK","0857.HK","0386.HK",'XOM','2222.SR','OXY','BP','RDSA.AS']
cr=compare_snapshot(tickers,'Current Ratio')
pbr=compare_snapshot(tickers,'Price to Book')
atr=compare_tax(tickers)
emp=compare_snapshot(tickers,'Employees')
esg=compare_snapshot(tickers,'Total ESG')

tickers2=["0883.HK","0857.HK","0386.HK",'1024.HK','1810.HK','9988.HK','9618.HK','0700.HK']
cfps=compare_snapshot(tickers2,'Cashflow per Share')


from siat.beta_adjustment import *
atr=prepare_hamada_yahoo('XOM')

compare_stock(["000001.SS","^HSI"], "Close", "2010-1-1", "2021-5-18",twinx=True)
compare_stock(["000001.SS","^HSI"], "Exp Ret%", "2021-1-1", "2021-5-18")
compare_stock(["000001.SS","^HSI"], "Exp Ret Volatility%", "2021-1-1", "2021-5-18")

gg_cnooc=get_stock_profile("0883.HK",info_type='officers')
gg_sinopec=get_stock_profile("0386.HK",info_type='officers')
gg_slb=get_stock_profile('RDSA.AS',info_type='officers')
#==============================================================================
compare_stock(["FB", "MSFT"], "Annual Ret LPSD%", "2019-1-1", "2019-12-31")
compare_stock(["FB", "MSFT"], "Exp Ret LPSD%", "2019-1-1", "2019-12-31")

#==============================================================================
price=stock_price("600519.SS","2020-6-10","2020-7-10")

compare_stock("MSFT", ["Open", "Close"], "2020-3-16", "2020-3-31")
price = stock_price("GOOG", "2019-7-1", "2019-12-31")

prices = compare_stock(["DAI.DE","BMW.DE"], "Close", "2020-1-1", "2020-3-31")
compare_stock("7203.T", ["High", "Low"], "2020-3-1", "2020-3-31")

compare_stock(["FB", "TWTR"], "Daily Ret%", "2020-3-1", "2020-3-31")
compare_stock("CDI.PA", ["Daily Ret", "log(Daily Ret)"], "2020-1-1", "2020-3-31")

compare_stock("IBM", ["Annual Ret%", "Daily Ret%"], "2019-1-1", "2019-12-31")

compare_stock(["000002.SZ", "600266.SS"], "Annual Ret%", "2020-1-1", "2020-3-31")
compare_stock(["BABA", "JD"], "Annual Ret%", "2020-1-1", "2020-3-31")
compare_stock(["0700.HK", "1810.HK"], "Annual Ret%", "2019-10-1", "2019-12-31")
compare_stock(["MSFT", "AAPL"], "Annual Ret%", "2019-1-1", "2020-3-31")

info=stock_ret("MSFT", "2010-1-1", "2020-12-31", type="Exp Ret%")
compare_stock(["JD", "AMZN"], "Exp Adj Ret%", "2019-1-1", "2020-12-31")

pv=stock_price_volatility("000002.SZ", "2019-1-1", "2020-12-31", "Weekly Price Volatility")
pv=stock_price_volatility("000002.SZ", "2019-1-1", "2020-12-31", "Annual Price Volatility")
compare_stock(["JD", "BABA"], "Annual Price Volatility", "2019-1-1", "2019-12-31")

compare_stock(["JD", "BABA"], "Exp Price Volatility", "2019-1-1", "2019-12-31")

info=stock_ret_volatility("AAPL", "2019-1-1", "2019-12-31", "Weekly Ret Volatility%")
info=stock_ret_volatility("AAPL", "2019-1-1", "2019-12-31", "Annual Ret Volatility%",power=0)
info=stock_ret_volatility("AAPL", "2019-1-1", "2019-12-31", "Exp Ret Volatility%")

compare_stock(["AAPL", "MSFT"], "Annual Ret Volatility%", "2019-1-1", "2019-12-31")

compare_stock(["AAPL", "MSFT"], "Exp Ret Volatility%", "2019-1-1", "2019-12-31")

compare_stock("QCOM", ["Annual Ret LPSD%", "Annual Ret Volatility%"], "2019-1-1", "2019-12-31")

compare_stock("QCOM", ["Exp Ret LPSD%", "Exp Ret Volatility%"], "2019-1-1", "2019-12-31")

compare_stock("QCOM", ["Exp Ret LPSD%", "Exp Ret%"], "2019-1-1", "2019-12-31")

compare_stock(["FB", "MSFT"], "Annual Ret LPSD%", "2019-1-1", "2019-12-31")

#==============================================================================
price = stock_price("GOOG", "2019-7-1", "2019-12-31")
prices = compare_stock(["DAI.DE","BMW.DE"], "Close", "2020-1-1", "2020-3-31")
info=candlestick_demo("005930.KS", "2020-1-13", "2020-1-17")
info=candlestick("TCS.NS", "2020-3-1", "2020-3-31")
info=candlestick("0700.HK","2020-2-1","2020-3-31",mav=2,volume=True,style='blueskies')

compare_stock(["FB", "TWTR"], "Daily Ret%", "2020-3-1", "2020-3-31")

compare_stock("UBSG.SW", ["Daily Ret", "log(Daily Ret)"], "2020-1-1", "2020-1-10")
compare_stock("CDI.PA", ["Daily Ret", "log(Daily Ret)"], "2020-1-1", "2020-3-31")

compare_stock("IBM", ["Annual Ret%", "Daily Ret%"], "2019-1-1", "2019-12-31")
compare_stock(["000002.SZ", "600266.SS"], "Annual Ret%", "2020-1-1", "2020-3-31")
compare_stock(["BABA", "JD"], "Annual Ret%", "2020-1-1", "2020-3-31")
compare_stock(["0700.HK", "1810.HK"], "Annual Ret%", "2019-10-1", "2019-12-31")
compare_stock(["MSFT", "AAPL"], "Annual Ret%", "2019-1-1", "2020-3-31")

info=stock_ret("MSFT", "2010-1-1", "2020-12-31", type="Exp Ret%")

compare_stock(["JD", "AMZN"], "Exp Adj Ret%", "2019-1-1", "2020-12-31")


pv=stock_price_volatility("000002.SZ", "2019-1-1", "2020-12-31", "Weekly Price Volatility")
pv=stock_price_volatility("000002.SZ", "2019-1-1", "2020-12-31", "Annual Price Volatility")

compare_stock(["JD", "BABA"], "Annual Price Volatility", "2019-1-1", "2019-12-31")

compare_stock(["JD", "BABA"], "Exp Price Volatility", "2019-1-1", "2019-12-31")

info=stock_ret_volatility("AAPL", "2019-1-1", "2019-12-31", "Weekly Ret Volatility%")
info=stock_ret_volatility("AAPL", "2019-1-1", "2019-12-31", "Annual Ret Volatility%")
info=stock_ret_volatility("AAPL", "2019-1-1", "2019-12-31", "Exp Ret Volatility%")

compare_stock(["AAPL", "MSFT"], "Annual Ret Volatility%", "2019-1-1", "2019-12-31")
compare_stock(["AAPL", "MSFT"], "Exp Ret Volatility%", "2019-1-1", "2019-12-31")

compare_stock("QCOM", ["Annual Ret LPSD%", "Annual Ret Volatility%"], "2019-1-1", "2019-12-31")
compare_stock("QCOM", ["Exp Ret LPSD%", "Exp Ret Volatility%"], "2019-1-1", "2019-12-31")
compare_stock("QCOM", ["Exp Ret LPSD%", "Exp Ret%"], "2019-1-1", "2019-12-31")

compare_stock(["FB", "MSFT"], "Annual Ret LPSD%", "2019-1-1", "2019-12-31")


#==============================================================================
dfr=stock_ret('AAPL','2020-1-1','2021-4-8',type="Daily Adj Ret%")


compare_stock(["000002.SZ", "600266.SS"], "Annual Ret%", "2020-1-1", "2020-3-31")
compare_stock(["BABA", "JD"], "Annual Ret%", "2020-1-1", "2020-3-31")
compare_stock(["0700.HK", "1810.HK"], "Annual Ret%", "2020-1-1", "2020-3-31")
compare_stock(["MSFT", "AAPL"], "Annual Ret%", "2019-1-1", "2020-3-31")

info=stock_ret("MSFT", "2010-1-1", "2020-3-31", type="Exp Ret%")




#==============================================================================
vix=security_price("^VIX", "2020-1-1", "2021-3-31",power=15)
vix=security_price("^VIX", "2021-1-1", "2021-3-31",power=10)

compare_security(['^VIX','^GSPC'],'Close','2011-1-1','2020-12-31',twinx=True)


compare_stock("AAPL", ["Close", "Adj Close"], "2019-1-1", "2019-12-31")
compare_stock("000002.SZ", ["Close", "Adj Close"], "2019-1-1", "2019-7-31")



pricedf=get_price('^HSI',"1991-1-1","2021-2-28")


df=security_price('AAPL','2021-1-1','2021-1-31',datatag=True,power=4)

info=get_stock_profile("AAPL")
info=get_stock_profile("MSFT",info_type='officers')
info=get_stock_profile("AAPL",info_type='officers')
info=stock_info('AAPL')
sub_info=stock_officers(info)

div=stock_dividend('600519.SS','2011-1-1','2020-12-31')
split=stock_split('600519.SS','2000-1-1','2020-12-31')

ticker='AAPL'
info=stock_info(ticker)
info=get_stock_profile("AAPL",info_type='officers')

info=get_stock_profile("AAPL")

info=get_stock_profile("MSFT",info_type='officers')
info=get_stock_profile("GS",info_type='officers')

info=stock_info('JD')
sub_info=stock_officers(info)
info=get_stock_profile("JD",info_type='officers')

info=stock_info('BABA')
sub_info=stock_officers(info)
info=get_stock_profile("BABA",info_type='officers')

info=stock_info('0700.HK')
sub_info=stock_officers(info)
info=get_stock_profile("0700.HK",info_type='officers')

info=stock_info('600519.SS')
sub_info=stock_officers(info)
info=get_stock_profile("600519.SS",info_type='officers')

info=get_stock_profile("0939.HK",info_type='risk_esg')


market={'Market':('China','^HSI')}
stocks={'0700.HK':3,'9618.HK':2,'9988.HK':1}
portfolio=dict(market,**stocks)
esg=portfolio_esg2(portfolio)



