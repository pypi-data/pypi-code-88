# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['rpi_flash']

package_data = \
{'': ['*']}

install_requires = \
['humanize>=3.9.0,<4.0.0',
 'pydantic>=1.8.2,<2.0.0',
 'requests>=2.25.1,<3.0.0',
 'typer>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['flash = rpi_flash']}

setup_kwargs = {
    'name': 'rpi-flash',
    'version': '0.1.3',
    'description': '',
    'long_description': '# rpi-flash\n\nScript to flash and configure a disk image. Image may be local or via http, and may be gz compressed. To minimise flash writes, each block is read and compared first.\n\nMade specifically for my Raspberry Pi flashing process, it may not be suitable for you. Currently supports macOS only.\n\n## Configuraton\n\nConfiguration assumes a partition with `.configure_me` in its root. If not found this will be skipped.\nThe configuration is compatible with my custom [`rpi-base`](https://github.com/hillnz/rpi-image-base) image.\n\nRun with `--write-env` to generate a .env file with variables and docs.\n',
    'author': 'Jono Hill',
    'author_email': 'jono@hillnz.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/jonohill/rpi-flash',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
