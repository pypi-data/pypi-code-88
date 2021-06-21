# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['destination']

package_data = \
{'': ['*']}

extras_require = \
{':python_version <= "3.7"': ['importlib-metadata>=4.0.1,<5.0.0']}

setup_kwargs = {
    'name': 'destination',
    'version': '1.3.0',
    'description': 'A Regex Based Path Routing Library.',
    'long_description': '===========\nDestination\n===========\n.. image:: https://github.com/futursolo/destination/actions/workflows/everything.yml/badge.svg\n   :target: https://github.com/futursolo/destination/actions/workflows/everything.yml\n\n.. image:: https://coveralls.io/repos/github/futursolo/destination/badge.svg?branch=master\n   :target: https://coveralls.io/github/futursolo/destination?branch=master\n\nDestination is a framework agnostic regular expression based path routing\nlibrary.\n\nInstallation\n============\n\n.. code-block:: shell\n\n   $ pip install -U destination\n\nThread Safety\n=============\nCurrently, destination is not thread safe. Hence, you should deepcopy\ninstances or add a mutex lock before using dispatchers and rules in the\nother threads.\n\nUsage\n=====\nThe default implementation of url parsing uses regular expressions. This is\nsimilar to Django and Tornado. You can create rules and dispatchers to\nresolve and parse your url using regular expressions set in the rules.\n\nGenerally, you should start with :code:`ReRule` and\n:code:`Dispatcher`. You can create a :code:`ReRule` with the regular expression\nthat is going to be used to parse (and possibly compose) the url, and an\noptional identifier to help you identify which rule is parsed, if an identifier\nis not provided or its value is set to :code:`None`, the rule itself will be\nused as an identifier. A :code:`Dispatcher` may be instantiated with no\narguments as a storage of multiple rules. You can add or remove rules at\nany time.\n\n:code:`ReSubDispatcher` is a sub-dispatcher that can be added to a dispatcher\nas a rule. It uses regular expressions to chop off the part matched to the\nregular expression and dispatches the rest part to the rules added to it.\n\n:code:`BaseRule` and :code:`BaseDispatcher` can be used to create custom rules\nand dispatchers.\n\nLicence\n=======\nMIT License\n\nCopyright (c) 2021 Kaede Hoshikawa\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.\n',
    'author': 'Kaede Hoshikawa',
    'author_email': 'futursolo@icloud.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/futursolo/destination',
    'packages': packages,
    'package_data': package_data,
    'extras_require': extras_require,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
