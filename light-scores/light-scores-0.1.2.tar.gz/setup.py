# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['light_scores']

package_data = \
{'': ['*']}

install_requires = \
['loguru>=0.5.3,<0.6.0',
 'logzero>=1.7.0,<2.0.0',
 'nltk>=3.6.2,<4.0.0',
 'rank-bm25>=0.2.1,<0.3.0']

setup_kwargs = {
    'name': 'light-scores',
    'version': '0.1.2',
    'description': '',
    'long_description': '# light_scores\n<!--- light_scores  light_scores  light_scores light_scores --->\n[![tests](https://github.com/ffreemt/light_scores/actions/workflows/routine-tests.yml/badge.svg)][![python](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)](https://img.shields.io/static/v1?label=python+&message=3.7%2B&color=blue)[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)[![PyPI version](https://badge.fury.io/py/light_scores.svg)](https://badge.fury.io/py/light_scores)\n\nCalculate bm25 matrix of two lists\n\n## Usage\n\n```python\nfrom light_scores.light_scores import light_scores\n\nres = await light_scores("test me")\nprint(res)\n# \'考我 试探我 测试我 试探\'\n\nprint(await light_scores("test me", to_lang="de"))',
    'author': 'freemt',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ffreemt/light-scores',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
