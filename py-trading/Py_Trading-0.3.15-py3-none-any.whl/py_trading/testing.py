from requests import get 
from bs4 import BeautifulSoup
from datetime import datetime
import pickle
from pathlib import Path
import pandas as pd

HEADERS = {'User-Agent': "'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) AppleWebKit/537.36 " # Telling the website what browser I am "using"
                            "(KHTML, like Gecko) Chrome/29.0.1547.62 Safari/537.36'"}

def _get_soup(url):
    response = get(url, headers=HEADERS, timeout=20)
    assert response.status_code == 200
    return BeautifulSoup(response.content, 'lxml')

def find_competition(ticker):
    BASE_URL = f'https://finviz.com/quote.ashx?t={ticker}'
    soup = _get_soup(BASE_URL)

    td = soup.find_all('td', {'class': 'fullview-links'})[1]
    sectors = td.find_all('a', {'class': 'tab-link'})
    # sector_urls = ([str('https://finviz.com/' + i['href']) for i in sectors])
    # for url in sector_urls: # Find stocks with similar P/E ratios and market cap, then track difference in performance
    # 	print(url)

    sectors = [sector.get_text() for sector in sectors]
    return sectors

print(find_competition('TSM'))