# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['skipper_lib', 'skipper_lib.events']

package_data = \
{'': ['*']}

install_requires = \
['pika>=1.2.0,<2.0.0', 'requests>=2.25.1,<3.0.0']

entry_points = \
{'console_scripts': ['skipper-lib = skipper_lib:main']}

setup_kwargs = {
    'name': 'skipper-lib',
    'version': '1.1.2',
    'description': 'Simple and flexible ML workflow engine',
    'long_description': '# Katana ML Skipper\n\n## Overview\n\nThis is a helper library for Katana ML Skipper workflow product. The idea of this library is to wrap all reusable code to simplify and improve workflow implementation.\n\nSupported functionality:\n\n- API to communicate with RabbitMQ for event receiver/producer\n\n## Author\n\nKatana ML, Andrej Baranovskij\n\n## Instructions\n\nVersion number should be updated in __init__.py and pyproject.toml\n\n1. Install Poetry\n\n```\npip install poetry\n```\n\n2. Add pika and requests libraries\n\n```\npoetry add pika\npoetry add requests\n```\n\n3. Build\n\n```\npoetry build\n```\n\n4. Publish to TestPyPI\n\n```\npoetry publish -r testpypi\n```\n\n5. Install from TestPyPI\n\n```\npip install -i https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple  skipper-lib\n```\n\n6. Publish to PyPI\n\n```\npoetry publish\n```\n\n7. Install from PyPI\n\n```\npip install skipper-lib\n```\n\n8. Test imported library from CMD\n\n```\npython -m skipper_lib\n```\n\n9. Import EventReceiver\n\n```\nfrom skipper_lib.events.event_receiver import EventReceiver\n```\n\n10. Import EventProducer\n\n```\nfrom skipper_lib.events.event_producer import EventProducer\n```\n\n## Structure\n\n```\n.\n├── LICENSE\n├── poetry.lock\n├── pyproject.toml\n├── skipper_lib\n│   ├── __init__.py\n│   ├── __main__.py\n│   ├── events\n│       ├── __init__.py\n│       ├── event_producer.py\n│       └── event_receiver.py\n└── README.md\n```\n\n## License\n\nLicensed under the Apache License, Version 2.0. Copyright 2020-2021 Katana ML, Andrej Baranovskij. [Copy of the license](https://github.com/katanaml/katana-pipeline/blob/master/LICENSE).\n',
    'author': 'Andrej Baranovskij',
    'author_email': 'andrejus.baranovskis@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/katanaml/katana-skipper',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
