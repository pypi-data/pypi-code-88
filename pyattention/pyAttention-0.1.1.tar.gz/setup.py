# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyattention']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyattention',
    'version': '0.1.1',
    'description': 'A library to monitor information sources',
    'long_description': "# pyAttention\nA library to monitor information sources\n\n![build](https://github.com/dhrone/pyattention/actions/workflows/test.yml/badge.svg) [![codecov](https://codecov.io/gh/dhrone/pyAttention/branch/master/graph/badge.svg?token=ZCAT8XRG4W)](https://codecov.io/gh/dhrone/pyAttention)\n\n## Key Features\n\n* Retrieves data from TCP servers, socketIO services, RSS feeds, and SQL databases\n* Retrieves basic system data from linux-based computers (disk space, IP address, temperatures)\n* Provides a queue interface for retrieving received information\n* Supports polling and asynchronous monitoring\n* Sources can be run individually or monitored together as a collection\n* Sources run in their own thread or can share a thread across a collection\n\n## Installation\n\n```shell\n# Installation from pypi\npip pyAttention\n\n# or\n# Installation from github\n$ git clone https://github.com/dhrone/pyAttention\n\n# Install optional dependencies\n# Databases\n$ pip install sqlalchemy\n$ pip install aiosqlite  # For sqlite database support\n$ pip install asyncpg    # For PostgreSQL\n$ pip install aiomysql   # For mySQL\n\n# RSS Feeds\n$ pip install httpx lxml beautifulsoup4\n\n# socketIO services\n$ pip install python-socketio[client]==4.6.* aiohttp\n\n# Local system data\n$ pip install psutil netifaces\n```\n\n## Quickstart\n\nTo retrieve data from a RSS feed\n\n```python\nfrom pyattention.source import rss\n\n# EXAMPLE: Pull 3 day forecast of Manchester, UK from the BBC News RSS feed\nurl = 'https://weather-broker-cdn.api.bbci.co.uk/en/forecast/rss/3day/2643123'\nfrom pyattention.source import rss\nsrc = rss(url, frequency=21600)  # Query feed every 6 hours\nweather = src.get()\n```\n\nTo retrieve data from a socketIO service\n\n```python\n# EXAMPLE: monitor Volumio metadata from its socketIO API (see https://volumio.org)  \nfrom pyattention.source import socketIO\nurl = 'http://localhost:3000'\nsrc = socketIO(url)\n\nasync def callback(data):\n  await src.put(data)\n\nsrc.subscribe('pushState', callback)\nsrc.emit('getState')  # Command needed to get Volumio to send a pushState message\nstate = src.get()\n```\n\nTo retrieve data from a database\n\n```python\n# EXAMPLE: pull data from a locally stored sqlite database\n# Create test db\nimport sqlite3\ncon = sqlite3.connect('songs.db')\ncur = con.cursor()\ncur.execute('''CREATE TABLE songs (artist text, title text, album text)''')\ncur.execute('''INSERT INTO songs VALUES ('Billie Eilish', 'bad guy', 'When We All Fall Asleep, Where Do We Go?')''')\ncur.close()\n\nfrom pyattention.source import database\nuri = 'sqlite+aiosqlite:///./songs.db'\nsrc = database(uri, 'select * from songs')\nsongs = src.get()\n```\n",
    'author': 'dhrone',
    'author_email': 'dhrone@dhrone.xyz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/dhrone/pyAttention',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
