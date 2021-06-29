# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['librelingo_fakes']

package_data = \
{'': ['*']}

install_requires = \
['librelingo-types>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'librelingo-fakes',
    'version': '3.0.1',
    'description': 'Fake data for testing LibreLingo-related packages',
    'long_description': '<a name="librelingo_fakes"></a>\n# librelingo\\_fakes\n\n<a name="librelingo_fakes.fakes"></a>\n# librelingo\\_fakes.fakes\n\nThis package contains fake data for testing LibreLingo-related packages.\n\nThe fake data is returned using the types from [librelingo-types](https://pypi.org/project/librelingo-types/).\n\n## Usage\n```python\n\nfrom librelingo_fakes import fakes\n\nfakes.course1  # This is a Course() object\nfakes.course2  # This is another Course() object\nfakes.courseEmpty  # This is an empty course\n```\n\nFor the full list of fakes, use the autocomplete or check out the [this file](https://github.com/kantord/LibreLingo/blob/main/apps/librelingo_fakes/librelingo_fakes/fakes.py).\n\n### Customizing fakes\n\nYou can use `fakes.customize` to change some attributes on a fake object.\nIf you want to change the modules on `fakes.course1`, you\'d do it like this:\n\n```python\nfake_course = fakes.customize(fakes.course1, modules=[\n    fake_module_1, fake_module_2\n])\n```\n\n',
    'author': 'Dániel Kántor',
    'author_email': 'git@daniel-kantor.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
