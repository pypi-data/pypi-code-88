# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['hirakanadic']

package_data = \
{'': ['*']}

install_requires = \
['SudachiDict-core>=20210608,<20210609',
 'jaconv>=0.2.4,<0.3.0',
 'sudachidict_full>=20210608,<20210609',
 'sudachipy>=0.5.2,<0.6.0']

entry_points = \
{'console_scripts': ['hirakanadic = hirakanadic.cli:cli']}

setup_kwargs = {
    'name': 'hirakanadic',
    'version': '0.0.3',
    'description': '',
    'long_description': '# hirakanadic\n\n[![PyPi version](https://img.shields.io/pypi/v/hirakanadic.svg)](https://pypi.python.org/pypi/hirakanadic/)\n![PyTest](https://github.com/po3rin/hirakanadic/workflows/PyTest/badge.svg)\n[![](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/release/python-390/)\n\n## Install\n\n```sh\n$ pip install hirakanadic\n```\n\n## Usage\n\n```sh\n$ hirakanadic example/input.txt -o out.txt\n```\n\ninput file\n\n```\nコレステロール値\n陰のうヘルニア\n濾胞性リンパ腫\nコリネバクテリウム・ウルセランス感染症\n```\n\nresult\n\n```\nこれすてろーる,5146,5146,7000,これすてろーる,名詞,普通名詞,一般,*,*,*,コレステロール,コレステロール,*,*,*,*,*\nへるにあ,5146,5146,7000,へるにあ,名詞,普通名詞,一般,*,*,*,ヘルニア,ヘルニア,*,*,*,*,*\nこりねばくてりうむ,5146,5146,7000,こりねばくてりうむ,名詞,普通名詞,一般,*,*,*,コリネバクテリウム,コリネバクテリウム,*,*,*,*,*\nうるせらんす,5146,5146,7000,うるせらんす,名詞,普通名詞,一般,*,*,*,ウルセランス,ウルセランス,*,*,*,*,*\n```\n',
    'author': 'po3rin',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'http://github.com/po3rin/hirakanadic',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
