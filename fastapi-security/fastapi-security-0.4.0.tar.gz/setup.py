# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fastapi_security']

package_data = \
{'': ['*']}

install_requires = \
['PyJWT[crypto]>=2,<3', 'aiohttp>=3,<4', 'fastapi>=0,<1', 'pydantic>=1,<2']

setup_kwargs = {
    'name': 'fastapi-security',
    'version': '0.4.0',
    'description': 'Add authentication and authorization to your FastAPI app via dependencies.',
    'long_description': '# FastAPI Security\n\n[![Continuous Integration Status](https://github.com/jmagnusson/fastapi-security/actions/workflows/ci.yml/badge.svg)](https://github.com/jmagnusson/fastapi-security/actions/workflows/ci.yml)\n[![Continuous Delivery Status](https://github.com/jmagnusson/fastapi-security/actions/workflows/cd.yml/badge.svg)](https://github.com/jmagnusson/fastapi-security/actions/workflows/cd.yml)\n[![Python Versions](https://img.shields.io/pypi/pyversions/fastapi-security.svg)](https://pypi.org/project/fastapi-security/)\n[![Code Coverage](https://img.shields.io/codecov/c/github/jmagnusson/fastapi-security?color=%2334D058)](https://codecov.io/gh/jmagnusson/fastapi-security)\n[![PyPI Package](https://img.shields.io/pypi/v/fastapi-security?color=%2334D058&label=pypi%20package)](https://pypi.org/project/fastapi-security)\n\nAdd authentication and authorization to your FastAPI app via dependencies.\n\n## Installation\n\n```bash\npip install fastapi-security\n```\n\n## Documentation\n\n[The documentation for FastAPI-Security is found here](https://jmagnusson.github.io/fastapi-security/).\n',
    'author': 'Jacob Magnusson',
    'author_email': 'm@jacobian.se',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://jmagnusson.github.io/fastapi-security/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
