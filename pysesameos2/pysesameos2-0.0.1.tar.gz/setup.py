# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pysesameos2', 'tests']

package_data = \
{'': ['*']}

install_requires = \
['aenum>=3.1.0,<4.0.0', 'bleak>=0.12.0,<0.13.0', 'cryptography>=3.4.7,<4.0.0']

extras_require = \
{'doc': ['livereload>=2.6.3,<3.0.0',
         'mkdocs>=1.1.2,<2.0.0',
         'mkdocstrings>=0.15.0,<0.16.0',
         'mkdocs-autorefs>=0.2.1,<0.3.0',
         'mkdocs-include-markdown-plugin>=3.1.3,<4.0.0',
         'mkdocs-material>=7.1.8,<8.0.0']}

setup_kwargs = {
    'name': 'pysesameos2',
    'version': '0.0.1',
    'description': 'Unofficial library to control smart devices running Sesame OS2.',
    'long_description': "# pysesameos2\n\n_Unofficial Python Library to communicate with SESAME 3 series products via Bluetooth connection._\n\n[![PyPI](https://img.shields.io/pypi/v/pysesameos2)](https://pypi.python.org/pypi/pysesameos2)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/pysesameos2)\n![GitHub Workflow Status (branch)](https://img.shields.io/github/workflow/status/mochipon/pysesameos2/dev%20workflow/main)\n[![Documentation Status](https://readthedocs.org/projects/pysesameos2/badge/?version=latest)](https://pysesameos2.readthedocs.io/en/latest/?badge=latest)\n[![codecov](https://codecov.io/gh/mochipon/pysesameos2/branch/main/graph/badge.svg?token=EOkDeLXeG2)](https://codecov.io/gh/mochipon/pysesameos2)\n![PyPI - License](https://img.shields.io/pypi/l/pysesameos2)\n\n## Introduction\n\nThis project aims to control smart devices running **Sesame OS2** via **Bluetooth connection**. If you want to control them via the cloud service, please check [pysesame3](https://github.com/mochipon/pysesame3).\n\nTo be honest, this is my first time to use [`Bleak`](https://github.com/hbldh/bleak) which provides an asynchronous, cross-platform Bluetooth API. PRs are heavily welcome.\n\n* Free software: MIT license\n* Documentation: [https://pysesameos2.readthedocs.io](https://pysesameos2.readthedocs.io)\n\n## Tested Environments\n\n* macOS 10.15.7, Python 3.9.5\n* Raspberry Pi Zero W (Raspbian GNU/Linux 10, Raspberry Pi reference 2021-05-07), Python 3.7.3\n\n## Features\n\nPlease note that `pysesameos2` can only control [SESAME 3 Smart Lock](https://jp.candyhouse.co/products/sesame3) at this moment. Although all types of devices running Sesame OS2 are technically supportable, I don't actually have or need those devices. PRs are always welcome to help out!\n\n* Scan all SESAME locks using BLE advertisements.\n* Receive state changes (locked, handle position, etc.) that are proactively sent by the device.\n* Needless to say, locking and unlocking!\n\n## Consideration\n\n- The results of this project are merely from reverse engineering of the official SDK so you might run into some issues. Please do let me know if you find any problems!\n- `pysesameos2` only supports devices that have already been initially configured using the official app. That is, `pysesameos2` cannot configure the locking position of your device.\n- `pysesameos2` does not have, and will not have, any functionality related to the operation history of locks.  According to [the document](https://doc.candyhouse.co/ja/flow_charts#sesame-%E5%B1%A5%E6%AD%B4%E6%A9%9F%E8%83%BD), your lock's operation history is not stored in the lock itself, but on the cloud service. I personally recommend you to bring a Wi-Fi module to get the operation history uploaded and retrive it by [the API](https://doc.candyhouse.co/ja/SesameAPI#sesame%E3%81%AE%E5%B1%A5%E6%AD%B4%E3%82%92%E5%8F%96%E5%BE%97).\n\n## Usage\n\nPlease take a look at the [`example`](https://github.com/mochipon/pysesameos2/tree/main/example) directory.\n\n## Credits & Thanks\n\n* A huge thank you to all who assisted with [CANDY HOUSE](https://jp.candyhouse.co/).\n* Many thanks to [bleak](https://github.com/hbldh/bleak) and [pyzerproc](https://github.com/emlove/pyzerproc).\n",
    'author': 'Masaki Tagawa',
    'author_email': 'masaki@tagawa.email',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/mochipon/pysesameos2',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
