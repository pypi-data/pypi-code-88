# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['lnpanda']

package_data = \
{'': ['*']}

install_requires = \
['pandas>=1.2.4,<2.0.0',
 'pdir2>=0.3.2,<0.4.0',
 'protobuf3-to-dict>=0.1.5,<0.2.0',
 'py-lnd-grpc>=0.3.0,<0.4.0']

setup_kwargs = {
    'name': 'lnpanda',
    'version': '0.1.5',
    'description': 'A tool which pairs Pandas to LND Lightning Network Data for Data Science',
    'long_description': '# lnpanda\n\nlnpanda allows you to query Bitcoin lightning network data using Pandas dataframes. Pandas is a powerful data science tool, and the combination can be used to find insights about your node. In addition, pandas dataframes are a just convenient and powerful way to interact with your node, while staying on the command line!\n\n\n## Install\n\n```python\npip install lnpanda\n```\n\n## Environment Variables\n\nAdd information like node ip address, and directory containing:\n- tls.cert \n- admin.macaroon\n\n```bash\nexport CRED_PATH=/path/to/macaroon/and/tls/cert\nexport LND_NODE_IP=192.168.1.xx\n```\n\n## Basic Usage\n\n```python\nfrom lnpanda import lnpanda\n\n# initialize lnpanda object\na = lnpanda()\n\n# Get info about channel balances and fee rates in 1 view \na.list_channels_and_fees()\n\n# List routed transactions, shows eff_fee_rate of fwd\na.list_forwards()\n```\n\n## Using pandas queries\n\n```python\n# List channels with a fee rate > 100\na.list_channels_and_fees().query("fee_rate > 0.000100")\n\n# Get sum of latest 25 routed transactions in sats\na.list_forwards().tail(25).fee_msat.sum()/1000\n\n# Get a set of alias\' of the last 10 outgoing forwards\noutgoing_chan_ids = list(a.list_forwards().tail(10).chan_id_out)\nset(map(lambda x: a.get_peer_alias(x), outgoing_chan_ids))\n```',
    'author': 'Sam Korn',
    'author_email': 'korn94sam@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7.1',
}


setup(**setup_kwargs)
