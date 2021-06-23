# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['raion', 'raion.cli', 'raion.commands', 'raion.core', 'raion.routing']

package_data = \
{'': ['*']}

install_requires = \
['fastapi[all]>=0.65.2,<0.66.0', 'typer[all]>=0.3.2,<0.4.0']

entry_points = \
{'console_scripts': ['raion = raion.cli:app']}

setup_kwargs = {
    'name': 'raion',
    'version': '0.1.7',
    'description': 'Rion Framework',
    'long_description': '## About Raion Framework\n\nRaion is a web application framework with expressive, elegant syntax inspired by [laravel](https://laravel.com) and built with [fastapi](https://fastapi.tiangolo.com). We believe development must be an enjoyable and creative experience to be truly fulfilling. Raion takes the pain out of development by easing common tasks used in many web projects, such as:\n\n- [Simple, fast routing engine](https://raion.dev/docs/routing).\n- [Powerful dependency injection container](https://raion.dev/docs/container).\n- Multiple back-ends for [session](https://raion.dev/docs/session) and [cache](https://raion.dev/docs/cache) storage.\n- Expressive, intuitive [database ORM](https://raion.dev/docs/eloquent).\n- Database agnostic [schema migrations](https://raion.dev/docs/migrations).\n- [Robust background job processing](https://raion.dev/docs/queues).\n- [Real-time event broadcasting](https://raion.dev/docs/broadcasting).\n\nRaion is accessible, powerful, and provides tools required for large, robust applications.\n\n## Learning Raion\n\nRaion has the most extensive and thorough [documentation](https://raion.dev/docs) and tutorial library of all modern web application frameworks, making it a breeze to get started with the framework.\n\n## Raion Sponsors\n\nWe would like to extend our thanks to the following sponsors for funding Raion development. If you are interested in becoming a sponsor, please visit the Raion [Patreon page](https://patreon.com/raiondev).\n\n## Contributing\n\nThank you for considering contributing to the Raion framework! The contribution guide can be found in the [Raion documentation](https://raion.dev/docs/contributions).\n\n## Code of Conduct\n\nIn order to ensure that the Raion community is welcoming to all, please review and abide by the [Code of Conduct](https://raion.dev/docs/contributions#code-of-conduct).\n\n## Security Vulnerabilities\n\nIf you discover a security vulnerability within Raion, please send an e-mail via [support@raion.dev](mailto:support@raion.dev). All security vulnerabilities will be promptly addressed.\n\n## License\n\nThe Raion framework is open-sourced software licensed under the [MIT license](https://opensource.org/licenses/MIT).',
    'author': 'Raion',
    'author_email': 'framework@raion.dev',
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
