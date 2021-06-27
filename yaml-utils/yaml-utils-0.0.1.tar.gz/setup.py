# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['yaml_utils']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.4.1,<6.0.0']

setup_kwargs = {
    'name': 'yaml-utils',
    'version': '0.0.1',
    'description': 'This package will help to read and get parent key & child value from yaml',
    'long_description': '# yaml-util\nIt will help to read yaml file\n\n## Installation\n```pip install yaml-utils```\n\n## How to use it?\n```python\nfrom yaml_utils import get_parent_key_and_value\n\ndict1 = [{\'id\': {\'home_welcome_lbl\': \'username\'}},\n         {\'id\': {\'test.test1\': \'test1\', \'test.test2\': \'test2\', \'test.test3\': \'test3\', \'test.test4\': \'test4\'},\n          \'xpath\': {\'test.test5\': \'test5\', \'test.test6\': \'test6\', \'test.test7\': \'test7\', \'test.test8\': \'test8\'}},\n         {\'id\': {\'login_username_txt\': \'username2\', \'login_password_txt\': \'password\'}}]\n\nloc, val = get_parent_key_and_value(dict1, "home_welcome_lbl")\nprint(loc,val)\n\n# Output:\n# id username\n```\n\n## License\nMIT License\n\nCopyright (c) 2021 Muralidharan Rajendran\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.',
    'author': 'Muralidharan Rajendran',
    'author_email': 'muraleedharan005@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/muralidharan92/yaml-util',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
