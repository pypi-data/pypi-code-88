# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['themis_imager_readfile']

package_data = \
{'': ['*']}

install_requires = \
['numpy>=1.19.2,<2.0.0']

setup_kwargs = {
    'name': 'themis-imager-readfile',
    'version': '1.0.10',
    'description': 'Read functions for THEMIS ASI PGM raw files',
    'long_description': '# THEMIS All-Sky Imager Raw PGM Data Readfile\n\n[![Github Actions - Tests](https://github.com/ucalgary-aurora/themis-imager-readfile/workflows/tests/badge.svg)](https://github.com/ucalgary-aurora/themis-imager-readfile/actions?query=workflow%3Atests)\n[![PyPI version](https://img.shields.io/pypi/v/themis-imager-readfile.svg)](https://pypi.python.org/pypi/themis-imager-readfile/)\n[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)\n[![PyPI Python versions](https://img.shields.io/pypi/pyversions/themis-imager-readfile.svg)](https://pypi.python.org/pypi/themis-imager-readfile/)\n\nPython library for reading THEMIS All-Sky Imager (ASI) stream0 raw PGM-file data. The data can be found at https://data.phys.ucalgary.ca or http://themis.igpp.ucla.edu/index.shtml.\n\n## Installation\n\nThe themis-imager-readfile library is available on PyPI:\n\n```console\n$ python3 -m pip install themis-imager-readfile\n```\n\n## Supported Python Versions\n\nthemis-imager-readfile officially supports Python 3.6+.\n\n## Examples\n\nExample Python notebooks can be found in the "examples" directory. Further, some examples can be found in the "Usage" section below.\n\n## Usage\n\nImport the library using `import themis_imager_readfile`\n\n### Read a single file\n\n```python\n>>> import themis_imager_readfile\n>>> filename = "path/to/data/2020/01/01/atha_themis02/ut06/20200101_0600_atha_themis02_full.pgm.gz"\n>>> img, meta, problematic_files = themis_imager_readfile.read(filename)\n```\n\n### Read multiple files\n\n```python\n>>> import themis_imager_readfile, glob\n>>> file_list = glob.glob("path/to/files/2020/01/01/atha_themis02/ut06/*full.pgm*")\n>>> img, meta, problematic_files = themis_imager_readfile.read(file_list)\n```\n\n### Read using multiple worker processes\n\n```python\n>>> import themis_imager_readfile, glob\n>>> file_list = glob.glob("path/to/files/2020/01/01/atha_themis02/ut06/*full.pgm*")\n>>> img, meta, problematic_files = themis_imager_readfile.read(file_list, workers=4)\n```\n\n## Development\n\nClone the repository and install dependencies using Poetry.\n\n```console\n$ git clone https://github.com/ucalgary-aurora/themis-imager-readfile.git\n$ cd themis-imager-readfile/python\n$ make install\n```\n\n## Testing\n\n```console\n$ make test\n[ or do each test separately ]\n$ make test-flake8\n$ make test-pylint\n$ make test-pytest\n```\n',
    'author': 'Darren Chaddock',
    'author_email': 'dchaddoc@ucalgary.ca',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ucalgary-aurora/themis-imager-readfile',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
