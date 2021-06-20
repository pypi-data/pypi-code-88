# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bitsharesscripts']

package_data = \
{'': ['*']}

install_requires = \
['bitshares>=0.5.0,<0.6.0', 'click>=7.1.1,<8.0.0', 'uptick>=0.2.4,<0.3.0']

setup_kwargs = {
    'name': 'bitsharesscripts',
    'version': '3.1.0',
    'description': 'A set of scripts for BitShares',
    'long_description': "bitshares-scripts\n=================\n\nThis is a small scripts collection for doing various stuff in Bitshares\n\n* `balances_as_btc.py` - Summarize all assets on all accounts and show BTC value\n* `cancel_all_orders.py` - Cancel all orders on the specified account\n* `create_account.py` - Create new account with random password and providing all keys to stdout\n* `get_account.py` - Display account object\n* `get_worker.py` - Display worker object\n* `get_asset.py` - Display asset object\n* `get_balance.py` - Display account balances\n* `get_balance_multi.py` - Display summarized balance of multiple accounts\n* `get_feeds.py` - Show price feeds for specified asset\n* `get_keys.py` - Generate private and public keys from account name and password\n* `get_op_id.py` - Display operation id numbers and corresponding name\n* `get_witness.py` - Display witness object\n* `update_keys.py` - Change account keys using generated random password and providing all keys to stdout\n\n**Note:** some scripts are sending transactions, you need to add private active keys for your accounts via `uptick addkey`\n\nInstallation via poetry\n-----------------------\n\n1. Make sure you have installed required packages: `apt-get install gcc make libssl-dev`\n2. Install [poetry](https://python-poetry.org/docs/)\n3. Run `poetry install` to install the dependencies\n4. Copy `common.yml.example` to `common.yml` and change variables according to your needs\n5. Now you're ready to run scripts:\n\n\n```\npoetry shell\n./script.py\n```\n\nReusable parts\n--------------\n\nReusable parts are being moved slowly into `bitsharesscripts` package namespace. It can be installed via `pip install bitsharesscripts`.\n",
    'author': 'Vladimir Kamarzin',
    'author_email': 'vvk@vvk.pp.ru',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/bitfag/bitshares-scripts',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
