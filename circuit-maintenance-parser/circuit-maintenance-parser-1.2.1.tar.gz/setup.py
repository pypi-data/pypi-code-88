# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['circuit_maintenance_parser', 'circuit_maintenance_parser.parsers']

package_data = \
{'': ['*']}

install_requires = \
['bs4>=0.0.1,<0.0.2',
 'click>=7.1,<8.0',
 'geopy>=2.1.0,<3.0.0',
 'icalendar>=4.0.7,<5.0.0',
 'lxml>=4.6.2,<5.0.0',
 'pydantic[dotenv]>=1.8.2,<2.0.0',
 'toml==0.10.1',
 'tzwhere>=3.0.3,<4.0.0']

entry_points = \
{'console_scripts': ['circuit-maintenance-parser = '
                     'circuit_maintenance_parser.cli:main']}

setup_kwargs = {
    'name': 'circuit-maintenance-parser',
    'version': '1.2.1',
    'description': 'Python library to parse Circuit Maintenance notifications and return a structured data back',
    'long_description': '# circuit-maintenance-parser\n\n`circuit-maintenance-parser` is a Python library that parses circuit maintenance notifications from Network Service Providers (NSPs), converting heterogeneous formats to a well-defined structured format.\n\n## Context\n\nEvery network depends on external circuits provided by NSPs who interconnect them to the Internet, to office branches or to\nexternal service providers such as Public Clouds.\n\nObviously, these services occasionally require operation windows to upgrade or to fix related issues, and usually they happen in the form of **circuit maintenance periods**.\nNSPs generally notify customers of these upcoming events so that customers can take actions to minimize the impact on the regular usage of the related circuits.\n\nThe challenge faced by many customers is that mostly every NSP defines its own maintenance notification format, even though in the\nend the relevant information is mostly the same across NSPs. This library is built to parse notification formats from\nseveral providers and to return always the same object struct that will make it easier to process them afterwards.\n\nThe format of this output is following the [BCOP](https://github.com/jda/maintnote-std/blob/master/standard.md) defined\nduring a NANOG meeting that aimed to promote the usage of the iCalendar format. Indeed, if the NSP is using the\nproposed iCalendar format, the parser is straight-forward and there is no need to define custom logic, but this library\nenables supporting other providers that are not using this proposed practice, getting the same outcome.\n\nYou can leverage on this library in your automation framework to process circuit maintenance notifications, and use the standarised output to handle your received circuit maintenance notifications in a simple way.\n\n## How does it work?\n\nStarting from a Provider parsing class, **multiple** parsers can be attached (in a specific order) and specific provider information (such as the default email used from the provider).\n\nEach provider could use the standard ICal format commented above or define its custom HTML parsers, supporting multiple notification types for the same provider that could be transitioning from one type to another.\n\n### Supported Providers\n\n#### Supported providers using the BCOP standard\n\n- EuNetworks\n- NTT\n- PacketFabric\n- Telstra\n\n#### Supported providers based on other parsers\n\n- Cogent\n- Lumen\n- Megaport\n- Telstra\n- Zayo\n\n> Note: Because these providers do not support the BCOP standard natively, maybe there are some gaps on the implemented parser that will be refined with new test cases. We encourage you to report related **issues**!\n\n## Installation\n\nThe library is available as a Python package in pypi and can be installed with pip:\n`pip install circuit-maintenance-parser`\n\n## Usage\n\n> Please, refer to the [BCOP](https://github.com/jda/maintnote-std/blob/master/standard.md) to understand the meaning\n> of the output attributes.\n\n## Python Library\n\n```python\nfrom circuit_maintenance_parser import init_provider\n\nraw_text = """BEGIN:VCALENDAR\nVERSION:2.0\nPRODID:-//Maint Note//https://github.com/maint-notification//\nBEGIN:VEVENT\nSUMMARY:Maint Note Example\nDTSTART;VALUE=DATE-TIME:20151010T080000Z\nDTEND;VALUE=DATE-TIME:20151010T100000Z\nDTSTAMP;VALUE=DATE-TIME:20151010T001000Z\nUID:42\nSEQUENCE:1\nX-MAINTNOTE-PROVIDER:example.com\nX-MAINTNOTE-ACCOUNT:137.035999173\nX-MAINTNOTE-MAINTENANCE-ID:WorkOrder-31415\nX-MAINTNOTE-IMPACT:OUTAGE\nX-MAINTNOTE-OBJECT-ID;X-MAINTNOTE-OBJECT-IMPACT=NO-IMPACT:acme-widgets-as-a-service\nX-MAINTNOTE-OBJECT-ID;X-MAINTNOTE-OBJECT-IMPACT=OUTAGE:acme-widgets-as-a-service-2\nX-MAINTNOTE-STATUS:TENTATIVE\nORGANIZER;CN="Example NOC":mailto:noone@example.com\nEND:VEVENT\nEND:VCALENDAR\n"""\n\ndata = {\n  "raw": raw_text,\n  "provider_type": "NTT"\n}\n\nparser = init_provider(**data)\n\nparsed_notifications = parser.process()\n\nprint(parsed_notifications[0].to_json())\n{\n  "account": "137.035999173",\n  "circuits": [\n    {\n      "circuit_id": "acme-widgets-as-a-service",\n      "impact": "NO-IMPACT"\n    },\n    {\n      "circuit_id": "acme-widgets-as-a-service-2",\n      "impact": "OUTAGE"\n    }\n  ],\n  "end": 1444471200,\n  "maintenance_id": "WorkOrder-31415",\n  "organizer": "mailto:noone@example.com",\n  "provider": "example.com",\n  "sequence": 1,\n  "stamp": 1444435800,\n  "start": 1444464000,\n  "status": "TENTATIVE",\n  "summary": "Maint Note Example",\n  "uid": "42"\n}\n```\n\n## CLI\n\n```bash\n$ circuit-maintenance-parser --raw-file tests/integration/data/ical/ical1\nCircuit Maintenance Notification #0\n{\n  "account": "137.035999173",\n  "circuits": [\n    {\n      "circuit_id": "acme-widgets-as-a-service",\n      "impact": "NO-IMPACT"\n    }\n  ],\n  "end": 1444471200,\n  "maintenance_id": "WorkOrder-31415",\n  "organizer": "mailto:noone@example.com",\n  "provider": "example.com",\n  "sequence": 1,\n  "stamp": 1444435800,\n  "start": 1444464000,\n  "status": "TENTATIVE",\n  "summary": "Maint Note Example",\n  "uid": "42"\n}\n```\n\n```bash\n$ circuit-maintenance-parser --raw-file tests/integration/data/zayo/zayo1.html --parser zayo\nCircuit Maintenance Notification #0\n{\n  "account": "clientX",\n  "circuits": [\n    {\n      "circuit_id": "/OGYX/000000/ /ZYO /",\n      "impact": "OUTAGE"\n    }\n  ],\n  "end": 1601035200,\n  "maintenance_id": "TTN-00000000",\n  "organizer": "mr@zayo.com",\n  "provider": "zayo",\n  "sequence": 1,\n  "stamp": 1599436800,\n  "start": 1601017200,\n  "status": "CONFIRMED",\n  "summary": "Zayo will implement planned maintenance to troubleshoot and restore degraded span",\n  "uid": "0"\n}\n```\n\n# Contributing\n\nPull requests are welcomed and automatically built and tested against multiple versions of Python through Travis CI.\n\nThe project is following Network to Code software development guidelines and is leveraging:\n\n- Black, Pylint, Mypy, Bandit and pydocstyle for Python linting and formatting.\n- Unit and integration tests to ensure the library is working properly.\n\n## Local Development\n\n### Requirements\n\n- Install `poetry`\n- Install dependencies and library locally: `poetry install`\n- Run CI tests locally: `invoke tests --local`\n\n### How to add a new Circuit Maintenance provider?\n\n1. If your Provider requires a custom parser, within `circuit_maintenance_parser/parsers`, **add your new parser**, inheriting from generic\n   `Parser` class or custom ones such as `ICal` or `Html` and add a **unit test for the new provider parser**, with at least one test case under\n   `tests/unit/data`.\n2. Add new class in `providers.py` with the custom info, defining in `_parser_classes` the list of parsers that you will use, using the generic `ICal` and/or your custom parsers.\n3. **Expose the new parser class** updating the map `SUPPORTED_PROVIDERS` in\n   `circuit_maintenance_parser/__init__.py` to officially expose the parser.\n\n## Questions\n\nFor any questions or comments, please check the [FAQ](FAQ.md) first and feel free to swing by the [Network to Code slack channel](https://networktocode.slack.com/) (channel #networktocode).\nSign up [here](http://slack.networktocode.com/)\n',
    'author': 'Network to Code',
    'author_email': 'opensource@networktocode.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/networktocode/circuit-maintenance-parser',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6.1,<4.0.0',
}


setup(**setup_kwargs)
