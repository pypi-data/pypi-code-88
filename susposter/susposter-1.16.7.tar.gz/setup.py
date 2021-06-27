# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['susposter']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'susposter',
    'version': '1.16.7',
    'description': 'so sussy',
    'long_description': '# susposter\nsussy imposter\n',
    'author': 'Cryptex',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Cryptex-github',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
