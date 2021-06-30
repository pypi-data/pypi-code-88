# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bbbmeetings']

package_data = \
{'': ['*']}

install_requires = \
['requests>=2.25.1,<3.0.0', 'xmltodict>=0.12.0,<0.13.0']

setup_kwargs = {
    'name': 'bbbmeetings',
    'version': '0.1.2',
    'description': 'A module for reading bbb meetings from bbb servers',
    'long_description': '# bbbmeetings\n\nA Library that helps with reading information regarding Big Blue Button via the BBB-API. The goal of bbbmeetings is to make it easy to generate stats about one or more BBB-Instances.\n\nIt was a non-goal to create a full coverage of the BBB-API, for ending meetings, creating meetings, managing recordings etc.\n\n\n\n## Installation\n\nVia pip\n\n```\npip install bbbmeetings\n```\n\n\n\n## Usage\n\nFirst we need to create a BBB Server. To allow the connection with that server you need to know its secret, which can be found using `bbb-conf -- secret` as [mentioned here](https://docs.bigbluebutton.org/admin/bbb-conf.html#--secret). You can create a server like this:\n\n```python\nfrom bbbmeetings import BBBServer\nserver = BBBServer(host="https://bbb.example.org", secret="!#%Random!#$%Fsecret!#$%")\n```\n\nFor convenience bbbmeetings offers a way of treating multiple servers as one server:\n\n```python\nfrom bbbmeetings import BBBServers, BBBServer\n\n# Create a BBBServers Object from multiple BBBServer-Objects\nservers = BBBServers.from_list([\n        BBBServer("https://bbb1.example.org", "!#%Random!#$%Fsecret!#$%"),\n        BBBServer("https://bbb2.example.org", "!#%Random!#$%Fsecret!#$%"),\n        BBBServer("https://bbb3.example.org", "!#%Random!#$%Fsecret!#$%"),\n        BBBServer("https://bbb4.example.org", "!#%Random!#$%Fsecret!#$%"),\n        BBBServer("https://bbb5.example.org", "!#%Random!#$%Fsecret!#$%"),\n    ])\n```\n\nMost methods on `BBBServer` and `BBBServers` are the same, but in the following examples I will use `servers` to showcase how this module may be used:\n\n```python\n# Get a list of meetings running on all servers and print all details about them\nfor meeting in servers.meetings:\n    print(meeting)\n```\n\nYou can also get some numbers directly (in this case I use python\'s formatting strings):\n\n```python\nprint(f"On all servers there are {servers.people} people in {servers.n_meetings} meetings. {servers.video_active} people have their webcam on, {servers.connected_with_mic} connected with mic. There are {servers.moderators} moderators.")\n```\n\nIf you want to have a list of all people in all meetings on all servers run:\n\n```python\nprint(f"The names of everyone on all servers are {\', \'.join([a.name for a in servers.attendees])}")\n```\n\nIf you just want a list with the names of Presenters you can run:\n\n```python\npresenter_names = [a.name for a in servers.attendees if a.isPresenter]\n```\n\nOr if you want to know the longest running meeting:\n\n```python\nprint(f"Longest running meeting is {servers.longest_duration.name} with a duration of {servers.longest_duration.duration}")\n```\n\n',
    'author': 'David Huss',
    'author_email': 'david.huss@hfbk-hamburg.de',
    'maintainer': 'David Huss',
    'maintainer_email': 'david.huss@hfbk-hamburg.de',
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
