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
    'version': '0.0.4',
    'description': 'This package will help to read and get parent key & target value for given target key from yaml',
    'long_description': '# yaml-utils\nIt will help to read and get parent key & target value for given target key from yaml\n\n## Installation\n```pip install yaml-utils```\n\n## How to use it?\n```python\nfrom yaml_utils import get_parent_key_and_target_value\n\ndict_data = [{\'id\': {\'home_welcome_lbl\': \'username\'}},\n         {\'id\': {\'test.test1\': \'test1\', \'test.test2\': \'test2\', \'test.test3\': \'test3\', \'test.test4\': \'test4\'},\n          \'xpath\': {\'test.test5\': \'test5\', \'test.test6\': \'test6\', \'test.test7\': \'test7\', \'test.test8\': \'test8\'}},\n         {\'id\': {\'login_username_txt\': \'username123\', \'login_password_txt\': \'password\'}}]\n\nloc, val = get_parent_key_and_target_value(dict_data, "login_username_txt")\nprint(loc,val)\n\n# Output:\n# id username123\n```\n\n## Available methods and usage sample\n```python\nfrom yaml_utils import get_file_list,\n                        yaml_reader,\n                        get_parent_key_and_target_value,\n                        get_parent_and_dynamic_target_value\n\ndir_name_list = get_file_list(dir_name)\n\ndict_data = yaml_reader(dir_name_list)\n\nparent_key, target_value = get_parent_key_and_target_value(dict_data, tarket_key)\n\ndynamic_parent_key, dynamic_target_value = get_parent_and_dynamic_target_value(dict_data, tarket_key, replace_list, replaceable_word="replace")\n\n```\n\n## License\nMIT License\n\nCopyright (c) 2021 Muralidharan Rajendran\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.',
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
