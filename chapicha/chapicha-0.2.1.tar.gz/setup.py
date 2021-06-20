# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['chapicha', 'chapicha.ui']

package_data = \
{'': ['*']}

install_requires = \
['PyQt5>=5.15.4,<6.0.0',
 'click>=7.1.2,<8.0.0',
 'numpy>=1.20.2,<2.0.0',
 'opencv-python>=4.5.1,<5.0.0',
 'pytesseract>=0.3.7,<0.4.0',
 'rich>=10.1.0,<11.0.0']

entry_points = \
{'console_scripts': ['chapicha = chapicha.cli:main']}

setup_kwargs = {
    'name': 'chapicha',
    'version': '0.2.1',
    'description': 'A semi-automated image editing tool',
    'long_description': '# Chapicha\n\nA semi-automated image editing tool\n\n## Installation \n\nInstall chapicha from source using [Poetry](https://python-poetry.org/)\n\n```bash \n  git clone https://github.com/julius383/chapicha\n  cd chapicha\n  poetry install\n```\n\nInstall using pip\n\n```bash\npip install chapicha\n```\n    \n## Usage/Examples\n\n```\n\nUsage: chapicha [OPTIONS] COMMAND [ARGS]...\n\nOptions:\n  --version       Show the version and exit.\n  --verbose TEXT\n  --help          Show this message and exit.\n\nCommands:\n  color  Find the most dominant colors in image\n  crop   Crop images to given dimensions\n  ocr    Try and recognize text present in an image\n  scale  Scale down an image by a given factor\n```\n  \n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n\n  \n',
    'author': 'Julius Kibunjia',
    'author_email': 'kibunjiajulius@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/julius383/chapicha',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
