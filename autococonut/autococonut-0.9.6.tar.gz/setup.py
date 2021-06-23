# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autococonut', 'autococonut.engine']

package_data = \
{'': ['*'], 'autococonut': ['docs/*', 'templates/*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'Pillow>=8.2.0,<9.0.0',
 'evdev>=1.4.0,<2.0.0',
 'mss>=6.1.0,<7.0.0',
 'pynput>=1.7.3,<2.0.0']

entry_points = \
{'console_scripts': ['autococonut = autococonut.autococonut:main',
                     'autococonut-gui = autococonut.autococonut_gui:main']}

setup_kwargs = {
    'name': 'autococonut',
    'version': '0.9.6',
    'description': 'A workflow recording tool.',
    'long_description': '# AutoCoconut, a workflow recording tool for Linux\n\n**AutoCoconut** is a tool that enables tracking mouse and keyboard events to make a workflow report with screenshot illustrations. \nSuch workflow report can be helpful when creating bug reports, tutorials, or test cases for GUI testing frameworks, such as OpenQA\nand others.\n\n**AutoCoconut** works on **X11** sessions only. The current version is **not Wayland ready**.\n\n## Development\n\nCurrently, the development has reached **Phase 4**.\n\nWhich means that the script is able:\n\n* record various events,  mouse buttons and actions (click, double click, drag, vertical scroll), keyboard events (press and release)\n* identify various types of keys (modifiers, special keys, character keys, etc.)\n* find pre-defined patterns in single events and interpret them\n* take screenshots to illustrate the workflow (or create needles for OpenQA)\n* produce various output - *raw* file, *json* file, or a workflow description in adoc and html.\n* it has a GUI version which brings more functionality, such as edit, delete, or create events for the recorded workflow\n* is packaged on PyPi for easy installation.\n\n\n## How to install?\n\nThe script is being developed and tested on Fedora, so the following procedure is related to Fedora. For other distributions, you need to\nmake sure, that the following requirements are met:\n\n* Python development packages.\n* Tkinter libraries\n\nOn Fedora, you can follow this procedure:\n\n1. Install the `python3-devel`.\n2. Install `python3-tkinter`.\n\nThen you can install the application:\n\n1. `pip install --user autococonut`\n\n## How to use?\n\nSee the documentation in the `docs` directory of the `autococonut` package.\n\n',
    'author': 'Lukáš Růžička',
    'author_email': 'lruzicka@redhat.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
