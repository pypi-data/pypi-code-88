# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['spatula']

package_data = \
{'': ['*']}

install_requires = \
['attrs[attrs]>=20.3.0,<21.0.0',
 'click>=7.1.2,<8.0.0',
 'cssselect>=1.1.0,<2.0.0',
 'ipython[shell]>=7.19.0,<8.0.0',
 'lxml>=4.6.2,<5.0.0',
 'openpyxl>=3.0.6,<4.0.0',
 'scrapelib>=2.0.6,<3.0.0']

entry_points = \
{'console_scripts': ['spatula = spatula.cli:cli']}

setup_kwargs = {
    'name': 'spatula',
    'version': '0.8.3',
    'description': 'A modern Python library for writing maintainable web scrapers.',
    'long_description': '# Overview\n\n*spatula* is a modern Python library for writing maintainable web scrapers.\n\nSource: [https://github.com/jamesturk/spatula](https://github.com/jamesturk/spatula)\n\nDocumentation: [https://jamesturk.github.io/spatula/](https://jamesturk.github.io/spatula/)\n\nIssues: [https://github.com/jamesturk/spatula/issues](https://github.com/jamesturk/spatula/issues)\n\n[![PyPI badge](https://badge.fury.io/py/spatula.svg)](https://badge.fury.io/py/spatula)\n[![Test badge](https://github.com/jamesturk/spatula/workflows/Test%20&%20Lint/badge.svg)](https://github.com/jamesturk/spatula/actions?query=workflow%3A%22Test+%26+Lint%22)\n\n## Features\n\n- **Page-oriented design**: Encourages writing understandable & maintainable scrapers.\n- **Not Just HTML**: Provides built in [handlers for common data formats](https://jamesturk.github.io/spatula/reference/#pages) including CSV, JSON, XML, PDF, and Excel.  Or write your own.\n- **Fast HTML parsing**: Uses `lxml.html` for fast, consistent, and reliable parsing of HTML.\n- **Flexible Data Model Support**: Compatible with `dataclasses`, `attrs`, `pydantic`, or bring your own data model classes for storing & validating your scraped data.\n- **CLI Tools**: Offers several [CLI utilities](https://jamesturk.github.io/spatula/cli/) that can help streamline development & testing cycle.\n- **Fully Typed**: Makes full use of Python 3 type annotations.\n',
    'author': 'James Turk',
    'author_email': 'dev@jamesturk.net',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jamesturk/spatula/',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
