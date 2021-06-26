# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['state']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pystates3',
    'version': '0.1.2',
    'description': 'State aware system implemented in python',
    'long_description': '# ![pystates3](resources/logo.svg)\n\n# pystates3\nState aware system implemented in python\n',
    'author': 'Jaschar Domann',
    'author_email': 'jasjisdo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jasjisdo/pystates3',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
