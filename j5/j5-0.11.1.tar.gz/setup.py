# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['j5',
 'j5.backends',
 'j5.backends.console',
 'j5.backends.console.j5',
 'j5.backends.console.sb',
 'j5.backends.console.sr',
 'j5.backends.console.sr.v4',
 'j5.backends.console.zoloto',
 'j5.backends.hardware',
 'j5.backends.hardware.j5',
 'j5.backends.hardware.sb',
 'j5.backends.hardware.sr',
 'j5.backends.hardware.sr.v4',
 'j5.backends.hardware.zoloto',
 'j5.boards',
 'j5.boards.arduino',
 'j5.boards.sb',
 'j5.boards.sr',
 'j5.boards.sr.v4',
 'j5.boards.zoloto',
 'j5.components',
 'j5.components.derived',
 'j5.vision']

package_data = \
{'': ['*']}

install_requires = \
['cached_property>=1.5.1,<2.0.0',
 'pyquaternion>=0.9.5,<0.10.0',
 'pyserial>=3.4,<4.0',
 'pyusb>=1.0,<2.0',
 'typing-extensions>=3.7,<4.0']

extras_require = \
{'zoloto-vision': ['zoloto>=0.5,<0.6']}

setup_kwargs = {
    'name': 'j5',
    'version': '0.11.1',
    'description': 'j5 Robotics Framework',
    'long_description': '# j5\n\n[![Tests](https://github.com/j5api/j5/actions/workflows/test.yml/badge.svg)](https://github.com/j5api/j5/actions/workflows/test.yml)\n[![Test Coverage](https://api.codeclimate.com/v1/badges/54e440aba5a51c9ee133/test_coverage)](https://codeclimate.com/github/j5api/j5/test_coverage)\n[![Maintainability](https://api.codeclimate.com/v1/badges/54e440aba5a51c9ee133/maintainability)](https://codeclimate.com/github/j5api/j5/maintainability)\n[![Documentation Status](https://readthedocs.org/projects/j5/badge/?version=master)](https://j5.readthedocs.io/en/master/?badge=master)\n[![PyPI version](https://badge.fury.io/py/j5.svg)](https://badge.fury.io/py/j5)\n[![MIT license](https://img.shields.io/badge/license-MIT-brightgreen.svg?style=flat)](https://opensource.org/licenses/MIT)\n![Bees](https://img.shields.io/badge/bees-110%25-yellow.svg)\n\nj5 Framework - Creating consistent APIs for robotics\n\n## What is j5?\n\n`j5` is a Python 3 framework that aims to make building consistent APIs for robotics easier. It was created to reduce the replication of effort into developing the separate, yet very similar APIs for several robotics competitions. Combining the common elements into a single library with support for various hardware gives a consistent feel for students and volunteers. This means more time to work on building robots!\n\n## How do I use j5?\n\n`j5` is designed to never be visible to students. It sits behind the scenes and works magic.\n\n```python unchecked\nfrom robot import Robot\n\nr = Robot()\nr.motor_boards[0].motors[1] = 0.5\n```\n\nThe above code is likely to be familiar to any student who has competed in one of the below competitions. However, it is not a trivial problem to make this code portable across the platforms. For example, the motor board for Student Robotics is a separate board to the brain board, but is built into the same board for HR RoboCon.\n\n`j5` lets competition vendors define how the basic parts of the apis are accessed. A robot can thus be constructed from any combination of parts from various organisations.\n\n```python\nfrom j5 import BaseRobot\nfrom j5.backends.hardware.sr.v4 import (\n    SRV4MotorBoardHardwareBackend,\n    SRV4PowerBoardHardwareBackend,\n    SRV4ServoBoardHardwareBackend,\n)\nfrom j5.boards import BoardGroup\nfrom j5.boards.sr.v4 import MotorBoard, PowerBoard, ServoBoard\n\n\nclass Robot(BaseRobot):\n    """My Competition Robot."""\n\n    def __init__(self) -> None:\n        self._power_boards = BoardGroup.get_board_group(\n            PowerBoard, SRV4PowerBoardHardwareBackend,\n        )\n        self.power_board = self._power_boards.singular()\n\n        self.motor_boards = BoardGroup.get_board_group(\n            MotorBoard, SRV4MotorBoardHardwareBackend,\n        )\n        self.motor_board = self.motor_boards.singular()\n\n        self.servo_boards = BoardGroup.get_board_group(\n            ServoBoard, SRV4ServoBoardHardwareBackend,\n        )\n        self.servo_board = self.servo_boards.singular()\n```\n\n## Competitions\n\nWe intend to support the kits of the following robotics competitions:\n\n- [SourceBots Summer School](https://sourcebots.co.uk/)\n- [Student Robotics](https://studentrobotics.org/)\n- [Hills Road RoboCon](https://hr-robocon.org/)\n\nWhilst `j5` isn\'t officially endorsed by Student Robotics or RoboCon, we are working closely with Student Robotics to ensure perfect compatibility. Many `j5` contributors are members of Student Robotics and SourceBots.\n\n[sbot](https://github.com/sourcebots/sbot), a `j5` based API, was successfully deployed to over 100 users in August 2019. This is the first known case of a real-world deployment of a `j5` based API.\n\nIf you are interested in adding support for your hardware or building your own API, please get in touch.\n\n## Contributions\n\nThis project is released under the MIT Licence. For more information, please see `LICENSE`.\n\n`j5 contributors` refers to the people listed in the `CONTRIBUTORS` file.\n\nThe `CONTRIBUTORS` file can be generated by executing `CONTRIBUTORS.gen`. This generated file contains a list of people who have contributed to the `j5` project.\n\nMore information about contributing, and how to contact contributors can be found in [our docs](https://docs.j5.org.uk/en/master/development/communications.html)\n',
    'author': 'j5 contributors',
    'author_email': 'j5api@googlegroups.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://j5.org.uk',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
