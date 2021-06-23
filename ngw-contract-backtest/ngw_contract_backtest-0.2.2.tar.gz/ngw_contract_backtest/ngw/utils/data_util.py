from ngw_contract_backtest.ngw.data.data_api import get_TradeDatetime

def get_variety_code(symbol_exchange):
    symbol = symbol_exchange.split('.')[0]
    if 'M' in symbol and symbol[0] != 'M':
        variety_code = symbol.replace('M', '')
        return variety_code
    if symbol == 'MAM':
        # print('MA')
        return 'MA'


def isin_TradeDatetimeList(datetimeStr=None, TradeDatetimeList=None):
    for b_e in TradeDatetimeList:
        begin = b_e.get('begin')
        end = b_e.get('end')
        datetimeStr = str(str(datetimeStr)[:19])
        datetimeStr = str(datetimeStr).replace('-', '').replace(' ', '').replace(':', '')
        if datetimeStr >= begin and datetimeStr < end:
            return True
    return False


if __name__ == '__main__':
    TradeDatetimeList = get_TradeDatetime(variety='ap', start='2021-04-21', end='2021-04-29')
    print(TradeDatetimeList)
    a = isin_TradeDatetimeList(datetimeStr='2021-04-26 08:31:00', TradeDatetimeList=TradeDatetimeList)
    print(a)








