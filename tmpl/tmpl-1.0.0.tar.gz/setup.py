# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['tmpl']

package_data = \
{'': ['*']}

entry_points = \
{'markdown.extensions': ['pymdgen = pymdgen.md:Extension']}

setup_kwargs = {
    'name': 'tmpl',
    'version': '1.0.0',
    'description': 'Template abstraction for using multiple template engine backends in same code.',
    'long_description': '\n# tmpl\n\n[![PyPI](https://img.shields.io/pypi/v/tmpl.svg?maxAge=60)](https://pypi.python.org/pypi/tmpl)\n[![PyPI](https://img.shields.io/pypi/pyversions/tmpl.svg?maxAge=600)](https://pypi.python.org/pypi/tmpl)\n[![Tests](https://github.com/20c/tmpl/workflows/tests/badge.svg)](https://github.com/20c/tmpl)\n![LGTM Grade](https://img.shields.io/lgtm/grade/python/github/20c/tmpl)\n[![Codecov](https://codecov.io/gh/20c/tmpl/branch/master/graph/badge.svg?token=lxqOsemDTz)](https://codecov.io/gh/20c/tmpl)\n\nTemplate abstraction for using multiple template engine backends in same code.\n\n## Installation\n\n```sh\npip install tmpl\n```\n\n## Documentation\n\nIs lacking!\n\n\n## Changes\n\nThe current change log is available at <https://github.com/20c/tmpl/blob/master/CHANGELOG.md>\n\n\n## License\n\nCopyright 2016-2021 20C, LLC\n\nLicensed under the Apache License, Version 2.0 (the "License");\nyou may not use this software except in compliance with the License.\nYou may obtain a copy of the License at\n\n   http://www.apache.org/licenses/LICENSE-2.0\n\nUnless required by applicable law or agreed to in writing, software\ndistributed under the License is distributed on an "AS IS" BASIS,\nWITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\nSee the License for the specific language governing permissions and\nlimitations under the License.\n\n',
    'author': '20C',
    'author_email': 'code@20c.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/20c/tmpl',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0',
}


setup(**setup_kwargs)
