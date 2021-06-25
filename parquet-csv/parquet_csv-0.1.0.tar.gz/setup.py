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
    'version': '0.1.0',
    'description': 'Parquet from and to CSV format converter',
    'long_description': '# parquet_csv\nParquet to and from CSV converter\n',
    'author': 'Jiayu Liu',
    'author_email': 'jiayu@hey.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Jimexist/parquet_csv',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
