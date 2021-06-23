# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['autococonut', 'autococonut.engine']

package_data = \
{'': ['*'], 'autococonut': ['docs/*', 'templates/*']}

install_requires = \
['Jinja2>=3.0.1,<4.0.0',
 'Pillow>=8.2.0,<9.0.0',
 'evdev>=1.4.0,<2.0.0',
 'mss>=6.1.0,<7.0.0',
 'pynput>=1.7.3,<2.0.0']

entry_points = \
{'console_scripts': ['autococonut = autococonut.autococonut:main',
                     'autococonut-gui = autococonut.autococonut_gui:main']}

setup_kwargs = {
    'name': 'autococonut',
    'version': '0.9.4',
    'description': 'A workflow recording tool.',
    'long_description': '# AutoCoconut, a creative tool for OpenQA\n\n**AutoCoconut** is a tool that enables tracking mouse and keyboard events to make a workflow report with screenshot illustrations. \nSuch workflow report can be helpful when creating bug reports, tutorials, or test cases for GUI testing frameworks, such as OpenQA\nand others.\n\n## Development\n\nCurrently, the development has reached **Phase 2**.\n\nWhich means that the script is able:\n\n* record various events,  mouse buttons and actions (click, double click, drag, vertical scroll), keyboard events (press and release)\n* identify various types of keys (modifiers, special keys, character keys, etc.)\n* find pre-defined patterns in single events and interpret them\n* take screenshots to illustrate the workflow (or create needles for OpenQA)\n* produce various output - *raw* file, *json* file, or a workflow description in adoc and html.\n\n## Documentation\n\nSo far, **AutoCoconut** works as a CLI application. It can be started using the `autococonut.py` script. The script monitors the mouse and keyboard and records their events, such as clicks, keypresses, etc. and makes a list of these single events. Later, some of the single events are merged into super events by the Interpreter part to make it more understandable. For instance, when some presses a sequence of keys, such as "h", "e", "l", "l", and "o", the Interpreter recognizes it correctly as typing "hello" instead of pressing single keys. \n\nIt also takes the pictures of screens to capture either the click areas (for mouse events) or the result of the action (keyboard events) or both. For most of the actions, two screenshots are taken: a *regular* one and a *corrected* one. The regular screenshot is taken in the moment of the event, the corrected screenshot is either taken earlier or later according to a *time_offset* that a user can set. By default the `time_offset` is **1 second**.\n\nThe list of events can be obtained as a *raw* list, where all the events are recorded as is without any attempt to interpret them, as they came from the\nmouse and keyboard listeners. Alternatively, users can ask for an *interpreted* json file where interpreted *superevents* are recorded, also users can\nobtain a workflow report with screenshots in a number of formats.\n\n## Usage\n\n1. Start the script and go to the application where you want to record.\n2. When you are ready, press the **stop key** to start recording (**F10** by default).\n3. Use the application to finish your use case.\n4. When finished, press the **stop key** again to stop recording.\n5. You will receive the output according to your choice.\n\n### CLI arguments and their explanation\n\nThe script also accepts various arguments to control the flow and the output:\n\n**-s, --stopkey**: The stop key is used to start and stop the recording. By default, it is **F10**. Using this option, you can choose a stop key to your likings. Note, that if you choose a stop key that you want to use as a regular key later in the process, the script will terminate. Another good key to try, if F10 does not fit, is **esc**. \n\n**-e, --offset**: Defines a time (in seconds) that the script uses as an offset time correction to take the alternative screenshot. Usually, the offset takes an earlier screenshot for mouse actions and a later screenshot for keyboard actions. The time can be given in decimal numbers, too. Note, that with applications with slower response, the later screenshots might not show the correct screen, because it might happen before the finish of the ongoing action.The default is **1 second**.\n\n**-o, --output**: You can choose one of several outputs. The *raw* output returns a json file with all single events without interpretation. In this json file, all key presses and releases are recorded separately, including the combinations. The *json* output provides an interpreted list of super events organized in a json file. The *adoc*, *html*, and *openqa* outputs produce a list of steps in that chosen format. The *openqa* format lists the OpenQA test commands that can be used for OpenQA scripts.\n\n**-f, --file**: If a filename is given, the output will be saved to a file instead being displayed on a command line.\n\n**-r, --resolution**: Not implemented yet. It will come during the development Phase 2. If the resolution is given, the screen resolution will be changed to your selected resolution first, and then the script will start the recording.\n',
    'author': 'Lukáš Růžička',
    'author_email': 'lruzicka@redhat.com',
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
