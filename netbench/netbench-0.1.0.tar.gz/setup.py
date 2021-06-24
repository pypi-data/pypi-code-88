# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['netbench', 'netbench.bandwidth', 'netbench.latency', 'netbench.ptp']

package_data = \
{'': ['*']}

install_requires = \
['click>=8.0.1,<9.0.0', 'pandas>=1.2.5,<2.0.0']

entry_points = \
{'console_scripts': ['netbench = netbench.main:netbench']}

setup_kwargs = {
    'name': 'netbench',
    'version': '0.1.0',
    'description': 'A complete CLI suite for network benchmarking.',
    'long_description': '# Netbench\n\nNetbench is a CLI utlity for running benchmarks in a network. It allows\nmeasuring bandwidth or synchronization between devices. Mainly, Netbench acts\nas a wrapper around other well-established tools, offering a consistent and\nconvenient interface for runnings all the necessary benchmarks from one place\nand also providing results in an analytics-friendly format.\n\n## Pre-requisites for installation\n\nNetbench relies on [iperf3](https://github.com/esnet/iperf) for bandwidth\nmeasurements and injecting load into the network. Some Linux distributions\noffer it in a package, but you can always build it from source.\n\nFor PTP synchronization benchmarking, the\n[linuxptp](https://github.com/richardcochran/linuxptp) tools are used. Again,\npackages are available in some distributions.\n\n## Installing netbench\n\nSimply install it with pip:\n\n```shell\npip install --user netbench\n```\n\nNote that, to be able to use the `netbench` command, the pip installation\ndirectory must be present in your `PATH`.\n',
    'author': 'Víctor Vázquez',
    'author_email': 'victorvazrod@ugr.es',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/rabbits-ugr/netbench',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
