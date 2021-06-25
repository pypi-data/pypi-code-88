# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['appman',
 'appman.data',
 'appman.data.formulas',
 'appman.data.packages',
 'appman.data.packages.apps',
 'appman.data.packages.backend',
 'appman.data.packages.drivers',
 'appman.data.packages.extensions',
 'appman.data.packages.fonts',
 'appman.data.packages.provisioned',
 'appman.data.user']

package_data = \
{'': ['*']}

install_requires = \
['PyInquirer>=1.0.3,<2.0.0', 'click>=8.0.1,<9.0.0', 'pyyaml>=5.3.1,<6.0.0']

entry_points = \
{'console_scripts': ['appman = appman.cli:main']}

setup_kwargs = {
    'name': 'appman',
    'version': '0.2.0',
    'description': 'Cross-platform application management aggregator',
    'long_description': '# appman\n\n<a href="https://github.com/basiliskus/appman"><img src="https://user-images.githubusercontent.com/541149/121623429-87264e00-ca24-11eb-97a4-fcb3baebb0b2.png" alt="AppMan" width="200"></a>\n\nappman is cross-platform application management aggregator\n\n[![Build Status](https://travis-ci.com/basiliskus/appman.svg?branch=main)](https://travis-ci.com/basiliskus/appman)\n\n\n## Requirements\n\n- Python 3.9\n\n## Installation\n\nYou can install appman from [PyPI](https://pypi.org/project/appman/):\n\n```bash\n> pip install appman\n```\n\n## How to use\n\nComing soon\n\n## Credits\n\n- Logo by [Lulu Wang](https://luluwang.work/)\n\n## License\n\n© Basilio Bogado. Distributed under the [MIT License](LICENSE).\n',
    'author': 'Basilio Bogado',
    'author_email': '541149+basiliskus@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/basiliskus/appman',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
