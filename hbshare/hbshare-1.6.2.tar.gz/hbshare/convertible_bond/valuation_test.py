"""
可转债估值测试
"""
import hbshare as hbs
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
from cb_pricing_BS import cbPricingBlackScholes
from cb_pricing_Tree import cbPricingTree
from cb_pricing_MC import cbPricingMC


class CbValuation:
    """
    计算对应正股的波动率和股票价格
    """
    def __init__(self, date, stock_ticker):
        self.date = date
        self.stock_ticker = stock_ticker
        self._load_data()

    def _load_data(self):
        pre_dt = datetime.strptime(self.date, '%Y/%m/%d') - timedelta(days=400)
        pre_date = pre_dt.strftime('%Y%m%d')
        end_date = datetime.strptime(self.date, '%Y/%m/%d').strftime('%Y%m%d')
        sql_script = "SELECT SYMBOL, TDATE, TCLOSE FROM finchina.CHDQUOTE WHERE" \
                     " TDATE >= {} and TDATE <= {} and SYMBOL = {}".format(pre_date, end_date, self.stock_ticker)
        res = hbs.db_data_query('readonly', sql_script, page_size=5000)
        data = pd.DataFrame(res['data']).rename(
            columns={"SYMBOL": "ticker", "TDATE": "trade_date", "TCLOSE": "price"})
        data['trade_date'] = data['trade_date'].apply(lambda x: str(x))
        data = data[data['price'] > 0]

        self.vol = data['price'].pct_change()[-250:].std() * np.sqrt(250)
        self.stock_price = data.set_index('trade_date').loc[end_date, 'price']


if __name__ == '__main__':
    # 可转债的基本资料
    term_CB = {
        "ConvPrice": 10.66,
        "Maturity": "2021/2/1",
        "ConvertStart": 5.5,
        "Coupon": [0.2, 0.5, 1.0, 1.5, 1.5, 106.6],
        "Recall": [5.5, 15, 30, 130],
        "Resell": [2, 30, 30, 70, 103]
    }

    now_date = '2015/9/22'
    ticker = '601727'

    cb_value = CbValuation(date=now_date, stock_ticker=ticker)
    vol, stock_price = cb_value.vol, cb_value.stock_price
    # 同等级/期限的企业债收益率
    rate = 0.029659

    cb_price_bs = cbPricingBlackScholes(stock_price, term_CB, now_date, vol, rate)
    cb_price_tree = cbPricingTree(stock_price, term_CB, now_date, vol, rate)
    term_CB['Recall'][-1] *= term_CB['ConvPrice'] / 100
    term_CB['Resell'][-2] *= term_CB['ConvPrice'] / 100
    term_CB['Resell'][-1] *= term_CB['ConvPrice'] / 100
    cb_price_mc = cbPricingMC(stock_price, term_CB, now_date, vol, rate)