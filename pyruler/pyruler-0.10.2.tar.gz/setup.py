# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pyruler']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'pyruler',
    'version': '0.10.2',
    'description': 'Simple and powerful rule engine to generate complex data validations on an easy way',
    'long_description': '[![codecov](https://codecov.io/gh/danteay/pyruler/branch/master/graph/badge.svg?token=WZ9QXIJ3Z7)](https://codecov.io/gh/danteay/pyruler)\n\n# Pyruler\n\nSimple and powerful rule engine to generate complex data validations on an easy way.\n\n## Requirements\n\n- Python >= 3.6\n\n### Usage\n\n#### Installation\n\n```bash\npip3 install pyruler\n```\n\n### Documentation\n\n[Github Wiki](https://github.com/danteay/pyruler/wiki)\n',
    'author': 'Eduardo Aguilar',
    'author_email': 'dante.aguilar41@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/danteay/pyruler',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
