# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['futon', 'futon.brokers', 'futon.data', 'futon.strategy']

package_data = \
{'': ['*']}

install_requires = \
['Requests==2.25.1',
 'TA_Lib==0.4.20',
 'binance==0.3',
 'bokeh==2.3.2',
 'numpy>=1.20.3,<2.0.0',
 'pandas>=1.1.5,<2.0.0',
 'python_binance==1.0.10',
 'tqdm==4.61.1',
 'websocket_client==1.1.0']

setup_kwargs = {
    'name': 'futon',
    'version': '1.0.0',
    'description': 'Create automated bots that trade for you while you sleep',
    'long_description': '<p align="center">\n<img width="341" alt="Logo" src="https://user-images.githubusercontent.com/29514438/122650855-bd657b00-d152-11eb-8296-1407f832bd91.png">\n</p>\n\n<p align="center">\n<img alt="GitHub Workflow Status" src="https://img.shields.io/github/workflow/status/agrawal-rohit/futon/Build">\n<!-- <img alt="PyPI - Status" src="https://img.shields.io/pypi/status/futon"> -->\n<!-- <img alt="Codecov" src="https://img.shields.io/codecov/c/github/agrawal-rohit/futon"> -->\n<img alt="PyPI - Python Version" src="https://img.shields.io/pypi/pyversions/futon">\n<img alt="PyPI" src="https://img.shields.io/pypi/v/futon">\n<img alt="PyPI - Downloads" src="https://img.shields.io/pypi/dm/futon">\n<img alt="CodeFactor Grade" src="https://img.shields.io/codefactor/grade/github/agrawal-rohit/futon">\n<img alt="GitHub" src="https://img.shields.io/github/license/agrawal-rohit/futon">\n</p>\n\n# Installation\n\n```shell\n$ pip install futon\n```\n\n# Usage\n\n## Step 1: Initialize a data provider\n\nA data provider refers to a source from where an instruments historical data can be fetched. Currently, **Binance** is the only supported provider (more are being added actively)\n\n```python\nfrom futon.data.providers import Binance\n\n# Add your developer API keys here\napi_key = \'<API KEY>\'\nsecret_key = \'<API SECRET>\'\n\nbinance = Binance(api_key, secret_key)\n```\n\n## Step 2: Choose an instrument\n\n```python\ncoin = futon.instruments.Crypto(base_asset = \'DOGE\',\n                                quote_asset = \'USDT\',\n                                provider = binance,\n                                interval = \'30-min\',\n                                start_date = \'2021-05-01 00:00:00\')\n```\n\nWhen you initialize an instrument, historical data for the instrument is downloaded by _default_\n\nIf you\'re a chart guy, then you can create an interactive OHLCV chart right in your jupyter notebook:\n\n```python\nfrom bokeh.io import output_notebook, show, push_notebook\noutput_notebook()\n\ncoin.plot_candles()\n```\n\n![Candlestick Plot](imgs/candlestick_plot.png)\n\n## Step 3: Create a trading strategy\n\n```python\nfrom futon.strategy import TradingStrategy\n\nclass MACDCrossover(TradingStrategy):\n    def setup(self):\n        self.macd = futon.indicators.MACD(fastperiod = 6,\n                                            slowperiod = 18,\n                                            signalperiod = 5,\n                                            plot_separately = True)\n\n        self.indicators = [self.macd]\n\n    def logic(self, account, lookback):\n        try:\n            today = lookback.iloc[-1]\n\n            macd_today, signal_today, _ = self.macd.lookback[-1]\n            macd_yest, signal_yest, _ = self.macd.lookback[-2]\n\n            # Buying\n            buy_signal = (macd_today > signal_today) and (macd_yest < signal_yest)\n            if buy_signal:\n                entry_price   = today.close\n                entry_capital = account.buying_power\n                account.buy(entry_capital=entry_capital, entry_price=entry_price)\n\n            # Selling\n            sell_signal = (macd_today < signal_today) and (macd_yest > signal_yest)\n\n            if sell_signal:\n                percent = 1\n                exit_price = today.close\n                account.sell(percent=percent, current_price=exit_price)\n\n        except Exception as e:\n            print(\'ERROR:\', e)\n\nstrat = MACDCrossover(coin)\n```\n\n## Step 4: Run a backtest on historical data\n\n```python\nstrat.backtest(start_date = \'2021-06-1 00:00:00\', commision = 0.001, show_trades = True)\n```\n\n**Output**\n\n```\nPerforming backtest from: 01 June, 2021 (00:00:00) to 21 June, 2021 (16:00:00)\n\n-------------- Results ----------------\n\nRelative Returns: -2.55%\nRelative Profit: -25.49\n\nStrategy     : -36.4%\nNet Profit   : -363.96\n\nBuy and Hold : -33.85%\nNet Profit   : -338.47\n\nBuys        : 75\nSells        : 75\n--------------------\nTotal Trades : 150\n\n---------------------------------------\n```\n\n![Backtest Plot](imgs/backtest.png)\n',
    'author': 'Rohit Agrawal',
    'author_email': 'rohitagrawalofficialmail@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/agrawal-rohit/futon',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
