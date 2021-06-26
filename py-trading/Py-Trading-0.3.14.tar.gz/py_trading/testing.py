from requests import get 
from bs4 import BeautifulSoup
from datetime import datetime
import pickle
from pathlib import Path
import pandas as pd

def get_nasdaq(): # Nasdaq + NYSE + AMEX
    dfs = []
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        request = get(f'https://www.advfn.com/nasdaq/nasdaq.asp?companies={letter.upper()}')
        soup = BeautifulSoup(request.text, 'lxml')
        table = soup.find('table', {'class': 'market tab1'})
        df = pd.read_html(str(table))[0]
        df.columns = df.iloc[1].tolist()
        df = df.iloc[2:]
        df = df.reset_index()
        df = df[['Symbol', 'Equity']]
        df.columns = ['ticker', 'name']
        dfs.append(df)
        
    for letter in 'abcdefghijklmnopqrstuvwxyz':           
        request = get(f'http://eoddata.com/stocklist/NASDAQ/{letter}.htm')
        soup = BeautifulSoup(request.text, 'lxml')
        table = soup.find('table', {'class': 'quotes'})
        df = pd.read_html(str(table))[0]
        df = df[['Code', 'Name']]
        df.columns = ['ticker', 'name']
        dfs.append(df)
  
    df = pd.concat(dfs)
    df = df.reset_index()
    df = df[['ticker', 'name']]
    print(df)
    # if as_list:
        # return df.set_index('ticker').to_dict()
    return df

def get_nyse(): # Test to see if duplicate tickers on backend or Django webapp
    dfs = []
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        request = get(f'https://www.advfn.com/nyse/newyorkstockexchange.asp?companies={letter.upper()}')
        soup = BeautifulSoup(request.text, 'lxml')
        table = soup.find('table', {'class': 'market tab1'})
        df = pd.read_html(str(table))[0]
        df.columns = df.iloc[1].tolist()
        df = df.iloc[2:]
        df = df.reset_index()
        print(df)
        df = df[['Symbol', 'Equity']]
        df.columns = ['ticker', 'name']
        dfs.append(df)
        
    for letter in 'abcdefghijklmnopqrstuvwxyz':       
        request = get(f'https://eoddata.com/stocklist/NYSE/{letter}.htm')
        soup = BeautifulSoup(request.text, 'lxml')
        table = soup.find('table', {'class': 'quotes'})
        try:
            df = pd.read_html(str(table))[0]
        except:       
            df = pd.read_html(str(table))            
        print(df)
        df = df[['Code', 'Name']]
        df.columns = ['ticker', 'name']
        dfs.append(df)
        
    	# Will this work since they are series?
    df = pd.concat(dfs)
    df = df.reset_index()
    df = df[['ticker', 'name']]
    # df['ticker'] = df['ticker'].unique()
    # df['name'] = df['name'].unique()
    # if as_list:
    #     return sorted(df.tolist())
    return df.sort_values(by='ticker', ascending=True)

print(get_nasdaq())        
print(get_nyse())
