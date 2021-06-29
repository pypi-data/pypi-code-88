# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['s_tool', 's_tool.utils']

package_data = \
{'': ['*']}

install_requires = \
['selenium>=3.141.0,<4.0.0', 'webdriver-manager>=3.4.2,<4.0.0']

setup_kwargs = {
    'name': 's-tool',
    'version': '0.0.1.post0',
    'description': 'Selenium wrapper to make your life easy.',
    'long_description': '# s-tool\n\nSelenium wrapper to make your life easy.\n\n## Features\n\n- [X] Manage multiple webdrivers.\n- [X] Click any type of element.\n- [X] Extract Page source.\n- [X] Select different type of elements.\n- [X] Retrive cookies.\n- [X] take fullpage and elementwise screenshots.\n- [X] display and hide elements.\n\n## TODO\n\n- [ ] Fill information(forms)\n- [ ] horizontal and vertical scrolling\n- [ ] Handeling alerts and popup\n- [ ] Switching windows,tabs,frames.\n- [ ] adding universal login functionality with forms\n- [ ] handling iframe windows.\n- [ ] Writing Parser to extract data from WebDriver.\n- [ ] Logging driver activities\n',
    'author': 'Ravishankar Chavare',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/Python-World/s-tool',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
