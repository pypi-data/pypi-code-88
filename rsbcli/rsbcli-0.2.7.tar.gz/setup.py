# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['rsbcli']
install_requires = \
['PyQt5>=5.15.4,<6.0.0', 'PyQtWebEngine>=5.15.4,<6.0.0', 'click>=8.0.1,<9.0.0']

entry_points = \
{'console_scripts': ['rsb = RSBCLI:main']}

setup_kwargs = {
    'name': 'rsbcli',
    'version': '0.2.7',
    'description': 'A RAM saving cli to run web applications. Update 0.2.7: Added presets. Now you can type the name of certain websites to open them in RSB. Downloads and fullscreen too ',
    'long_description': "# RSB\n\n## A RAM saving cli to run web applications\n\n## Whats New: Now you can download files from RSB and has some preset websites to open. If you click a download link, it downloads in the background but doesn't say anything\n\n## Installation\n\n### Linux\n\n#### For Debian based OS\n\nPaste this in your terminal \n```cd ~/Downloads;wget https://raw.githubusercontent.com/AvanindraC/RSB/master/install.sh; sudo bash install.sh```\n\n#### For all Linux distros and Mac\n\n```pip3 install rsbcli```\n\n### Windows\n\n```pip install rsbcli``` \n\n## How to use\n\n### Windows\n\nOpen powershell and type ```rsb```\n\n#### To open a website regularly:\n\nType ```rsb open (Enter your url)```\n\n#### To open a preset website \n\nType ```rsb open_pre (keyword)```\n\n#### To see the preset keywords\n\nType ```rsb presets```\n\n#### Linux/Mac\n\nOpen the terminal and type ```rsb```\n\n#### To open a website regularly:\n\nType ```rsb open (Enter your url)```\n\n#### To open a preset website \n\nType ```rsb open_pre (keyword)```\n\n#### To see the preset keywords\n\nType ```rsb presets```### Softwares used\n\n## Developer Tools\n\nVisual Studio Code - https://github.com/Microsoft/vscode\n\nPython 3.9.1\n\nSpecial Thanks to https://github.com/arghyagod-coder",
    'author': 'Avanindra Chakraborty',
    'author_email': 'avanindra.d2.chakraborty@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/AvanindraC/RSB',
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
