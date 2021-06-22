# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kafka_bridge_client']

package_data = \
{'': ['*']}

install_requires = \
['aiohttp>=3.7.4,<4.0.0']

setup_kwargs = {
    'name': 'kafka-bridge-client',
    'version': '0.1.1',
    'description': 'Python client for Strimzi Kafka Bridge',
    'long_description': "# kafka-bridge-client\nPython async client for Strimzi Kafka Bridge. Package include consumer only.\n\n## Install\n```\npip install kafka-bridge-client\n```\n\n## Usage\n```python\nfrom kafka_bridge_client import KafkaBridgeConsumer\n\n\nconsumer = KafkaBridgeConsumer(\n    CONFIG['topics']['name'],\n    group_id=CONFIG['group_id'],\n    auto_offset_reset='earliest',\n    enable_auto_commit=False,\n    bootstrap_server=CONFIG['kafka_bridge']['url'],\n    consumer_name='consumer-name',\n)\n```\n",
    'author': 'Bogdan Zaseka',
    'author_email': 'zaseka.bogdan@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
