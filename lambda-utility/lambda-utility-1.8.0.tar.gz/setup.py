# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lambda_utility']

package_data = \
{'': ['*']}

install_requires = \
['aiobotocore>=1.3.0,<2.0.0', 'pydantic>=1.8.1,<2.0.0']

setup_kwargs = {
    'name': 'lambda-utility',
    'version': '1.8.0',
    'description': '',
    'long_description': "# lambda-utility\n[![Python](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)](https://www.python.org/)\n[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)\n[![Checked with mypy](http://www.mypy-lang.org/static/mypy_badge.svg)](http://mypy-lang.org/)\n[![PyPi](https://img.shields.io/pypi/v/lambda-utility.svg)](https://pypi.org/project/lambda-utility/)\n\n\nAWS Lambda에서 자주 사용하는 기능 구현\n\n## Installation\nPython 3.7 +\n```bash\n$ pip install lambda-utility\n```\n\n## Create a layer file\n```bash\n$ python layer\n\n...\nComplete -> 'lambda-utility.zip'\n```\nor\n```bash\n$ python layer -o {filename}\n\n...\nComplete -> '{filename}'\n```\n",
    'author': 'Pie',
    'author_email': 'pie.pie@kakaoent.com',
    'maintainer': 'Pie',
    'maintainer_email': 'pie.pie@kakaoent.com',
    'url': 'https://github.com/kakao-webtoon/lambda-utility',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
