import json
import requests
import pandas 
from flatten_json import flatten

defaultConfig = dict()
defaultConfig['api'] = 'https://boringstonks.com/graphql'
defaultConfig['timeout'] = 50

def getStocks(query, access_token, periods = 0, config = defaultConfig):
    mod_query = '{"query": "{ getStocks(periods: %d) { %s } } "}' % (periods, query)
    headers = {'Content-Type': 'application/json', 'Access-Token': access_token}
    x = requests.post(config['api'], data=mod_query, timeout=config['timeout'], headers=headers)
    stocks = x.json()['data']['getStocks']
    fl = [flatten(d) for d in stocks]
    frame = pandas.DataFrame(fl) 
    return frame

