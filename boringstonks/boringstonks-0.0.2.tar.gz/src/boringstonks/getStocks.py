import json
import requests
import pandas 

defaultConfig = dict()
defaultConfig['api'] = 'https://boringstonks.com/graphql'
defaultConfig['timeout'] = 50

def getStocks(query, periods = 0, config = defaultConfig):
    mod_query = '{"query": "{ getStocks(periods: %d) { %s } } "}' % (periods, query)
    headers = {'Content-type': 'application/json'}
    x = requests.post(config['api'], data=mod_query, timeout=config['timeout'], headers=headers)
    stocks = x.json()['data']['getStocks']
    frame = pandas.json_normalize(stocks)
    return frame

