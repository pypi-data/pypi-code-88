# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fear_greed_index']

package_data = \
{'': ['*']}

install_requires = \
['Pillow>=8.2.0,<9.0.0',
 'Sphinx>=4.0.2,<5.0.0',
 'bs4>=0.0.1,<0.0.2',
 'lxml>=4.6.3,<5.0.0',
 'm2r2>=0.2.7,<0.3.0',
 'matplotlib>=3.4.2,<4.0.0',
 'requests>=2.25.1,<3.0.0',
 'sphinx-rtd-theme>=0.5.2,<0.6.0']

setup_kwargs = {
    'name': 'fear-greed-index',
    'version': '0.1.2',
    'description': 'CNN Fear and Greed Index',
    'long_description': "# Unofficial CNN Fear and Greed Index\n\n## About the project\n\nThis module scrapes https://money.cnn.com/data/fear-and-greed/ to extract CNN Fear and Greed Index.\n\nIt has been created with the intention of adding this data to the economy menu of [GamestonkTerminal](https://github.com/GamestonkTerminal/GamestonkTerminal).\n\n## Usage\n\nBy doing:\n```python\nfrom fear_greed_index.CNNFearAndGreedIndex import CNNFearAndGreedIndex\n\ncnn_fg = CNNFearAndGreedIndex()\n\n# plot Fear and Greed charts\nfig = plt.figure(figsize=(20, 7))\ncnn_fg.plot_all_charts(fig)\nplt.show()\n\n# print Fear and Greed complete report\nprint(cnn_fg.get_complete_report())\n```\n\nYou can expect something like:\n\n![Fear-and-Greed-Charts](https://user-images.githubusercontent.com/25267873/122658705-5e126580-d168-11eb-8d55-61fe7d6a89fd.png)\n\n```\nFear & Greed Now: 30 (Fear)\n   Previous Close: 41 (Fear)\n   1 Week Ago: 54 (Neutral)\n   1 Month Ago: 35 (Fear)\n   1 Year Ago: 51 (Neutral)\n\nJunk Bond Demand: Greed                                                                             [Updated Jun 17 at 8:00pm]\n   Investors in low quality junk bonds are accepting 2.03 percentage points in additional yield over safer investment grade corporate bonds. This spread is down from recent levels and indicates that investors are pursuing higher risk strategies.\n   (Last changed Jun 8 from an Extreme Greed rating)\n\nMarket Volatility: Neutral                                                                          [Updated Jun 18 at 4:14pm]\n   The CBOE Volatility Index (VIX) is at 20.70. This is a neutral reading and indicates that market risks appear low.\n   (Last changed May 12 from an Extreme Fear rating)\n\nPut and Call Options: Fear                                                                          [Updated Jun 18 at 5:55pm]\n   During the last five trading days, volume in put options has lagged volume in call options by 55.47% as investors make bullish bets in their portfolios. However, this is still among the highest levels of put buying seen during the last two years, indicating fear on the part of investors.\n   (Last changed Jun 17 from a Greed rating)\n\nMarket Momentum: Fear                                                                               [Updated Jun 18 at 5:09pm]\n   The S&P 500 is 4.44% above its 125-day average. During the last two years, the S&P 500 has typically been further above this average than it is now, indicating that investors are committing capital to the market at a slower rate than they had been previously.\n   (Last changed Jun 17 from a Neutral rating)\n\nStock Price Strength: Extreme Fear                                                                  [Updated Jun 18 at 4:01pm]\n   The number of stocks hitting 52-week highs exceeds the number hitting lows but is at the lower end of its range, indicating extreme fear.\n   (Last changed May 20 from a Fear rating)\n\nStock Price Breadth: Extreme Fear                                                                   [Updated Jun 18 at 4:07pm]\n   The McClellan Volume Summation Index measures advancing and declining volume on the NYSE. During the last month, approximately 10.43% more of each day's volume has traded in declining issues than in advancing issues, pushing this indicator towards the lower end of its range for the last two years.\n   (Last changed Jun 17 from a Fear rating)\n\nSafe Heaven Demand: Extreme Fear                                                                    [Updated Jun 17 at 8:00pm]\n   Stocks and bonds have provided similar returns during the last 20 trading days. However, this has been among the weakest periods for stocks relative to bonds in the past two years and indicates investors are fleeing risky stocks for the safety of bonds.\n   (Last changed Apr 30 from a Fear rating)\n```\n\n",
    'author': 'Didier Rodrigues Lopes',
    'author_email': 'dro.lopes@campus.fct.unl.pt',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/DidierRLopes/fear-greed-index',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
