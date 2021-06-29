# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['elasticlogger']

package_data = \
{'': ['*']}

install_requires = \
['certifi>=2021.5.30,<2021.6.0',
 'elasticsearch>=7.13.2,<7.14.0',
 'python-json-logger>=2.0.1,<2.1.0',
 'setuptools>=53.0.0,<53.1.0',
 'urllib3>=1.26.3,<1.27.0']

setup_kwargs = {
    'name': 'elasticlogger',
    'version': '2.1.0',
    'description': 'Standardized logger compatible with ElasticSearch',
    'long_description': '# ElasticLogger\n\nSimple standardized logger tool that implements python-json-logger formatter and a simple\nelastic search integration.\n\n## Requirements\n\n- Python >= 3.6\n\n## Documentation\n\n[Readthedocs](https://elasticsearch.readthedocs.io)\n',
    'author': 'Eduardo Aguilar',
    'author_email': 'dante.aguilar41@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/danteay/elasticlogger',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
