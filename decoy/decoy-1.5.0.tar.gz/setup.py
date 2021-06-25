# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['decoy', 'decoy.mypy']

package_data = \
{'': ['*']}

entry_points = \
{'pytest11': ['decoy = decoy.pytest_plugin']}

setup_kwargs = {
    'name': 'decoy',
    'version': '1.5.0',
    'description': 'Opinionated, typed stubbing and verification library for Python',
    'long_description': '<div align="center">\n    <h1>Decoy</h1>\n    <img src="https://mike.cousins.io/decoy/img/decoy.png" width="256px">\n    <p>Opinionated, typed stubbing and verification library for Python</p>\n    <p>\n        <a href="https://github.com/mcous/decoy/actions">\n            <img title="CI Status" src="https://flat.badgen.net/github/checks/mcous/decoy/main">\n        </a>\n        <a href="https://pypi.org/project/decoy/">\n            <img title="PyPI Version" src="https://flat.badgen.net/pypi/v/decoy">\n        </a>\n        <a href="https://github.com/mcous/decoy/blob/main/LICENSE">\n            <img title="License" src="https://flat.badgen.net/github/license/mcous/decoy">\n        </a>\n    </p>\n    <p>\n        <a href="https://mike.cousins.io/decoy/">Usage guide and documentation</a>\n    </p>\n</div>\n\nThe Decoy library allows you to create, stub, and verify fully-typed, async/await friendly mocks in your Python unit tests, so your tests are:\n\n-   Less prone to insufficient tests due to unconditional stubbing\n-   Easier to fit into the Arrange-Act-Assert pattern\n-   Covered by typechecking\n\nThe Decoy API is heavily inspired by / stolen from the excellent [testdouble.js][] and [Mockito][] projects.\n\n[testdouble.js]: https://github.com/testdouble/testdouble.js\n[mockito]: https://site.mockito.org/\n\n## Install\n\n```bash\n# pip\npip install decoy\n\n# poetry\npoetry add --dev decoy\n```\n\n## Setup\n\n### Pytest setup\n\nDecoy ships with its own [pytest][] plugin, so once Decoy is installed, you\'re ready to start using it via its pytest fixture, called `decoy`.\n\n```python\n# test_my_thing.py\nfrom decoy import Decoy\n\ndef test_my_thing_works(decoy: Decoy) -> None:\n    # ...\n```\n\nThe `decoy` fixture is function-scoped and will ensure that all stub and spy state is reset between every test.\n\n[pytest]: https://docs.pytest.org/\n\n### Mypy Setup\n\nDecoy\'s API can be a bit confusing to [mypy][]. To suppress mypy errors that may be emitted during valid usage of the Decoy API, we have a mypy plugin that you should add to your configuration file:\n\n```ini\n# mypi.ini\n\n# ...\nplugins = decoy.mypy\n# ...\n```\n\n[mypy]: https://mypy.readthedocs.io/\n',
    'author': 'Mike Cousins',
    'author_email': 'mike@cousins.io',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://mike.cousins.io/decoy/',
    'packages': packages,
    'package_data': package_data,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
