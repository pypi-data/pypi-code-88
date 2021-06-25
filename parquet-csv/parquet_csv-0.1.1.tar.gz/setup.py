# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['parquet_csv']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0', 'pyarrow>=4.0.1,<5.0.0']

entry_points = \
{'console_scripts': ['parquet_to_csv = '
                     'parquet_csv.parquet_to_csv:parquet_to_csv']}

setup_kwargs = {
    'name': 'parquet-csv',
    'version': '0.1.1',
    'description': 'Parquet from and to CSV format converter',
    'long_description': '# Parquet_CSV\n\n[![CI](https://github.com/Jimexist/parquet_csv/actions/workflows/build.yml/badge.svg)](https://github.com/Jimexist/parquet_csv/actions/workflows/build.yml) | [PyPI](https://pypi.org/project/parquet-csv/)\n\nA Parquet to and from CSV converter that is based on [Apache Arrow](https://arrow.apache.org/) for its speed and memory efficiency.\n\n## How to install\n\n```bash\npip install parquet_csv\n```\n\nUse `pip3` if both Python2 and Python3 are installed. This application only works with Python3.\n\n## How to use\n\n`parquet_to_csv` converts `parquet` files to `csv` files.\n\n```text\nUsage: parquet_to_csv.py [OPTIONS] INPUT_FILE OUTPUT_PATH\n\nOptions:\n  --header / --no-header\n  --verbose BOOLEAN\n  --help                  Show this message and exit.\n```\n',
    'author': 'Jiayu Liu',
    'author_email': 'jiayu@hey.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Jimexist/parquet_csv',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
