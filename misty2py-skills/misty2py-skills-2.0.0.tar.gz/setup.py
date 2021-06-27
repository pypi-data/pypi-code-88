# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['misty2py_skills', 'misty2py_skills.demonstrations']

package_data = \
{'': ['*']}

install_requires = \
['Deprecated>=1.2.12,<2.0.0',
 'SpeechRecognition>=3.8.1,<4.0.0',
 'keyboard>=0.13.5,<0.14.0',
 'misty2py==5.0.0',
 'num2words>=0.5.10,<0.6.0',
 'pdoc3>=0.9.2,<0.10.0',
 'pylint>=2.8.3,<3.0.0',
 'pymitter>=0.3.0,<0.4.0',
 'pynput>=1.7.3,<2.0.0',
 'python-dotenv>=0.17.1,<0.18.0']

setup_kwargs = {
    'name': 'misty2py-skills',
    'version': '2.0.0',
    'description': 'A Python library of Misty II skills developed using Misty2py library',
    'long_description': '# Misty2py-skills\n\n[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/ChrisScarred/misty2py/blob/main/LICENSE)\n\nMisty2py-skills is a Python 3 library of Misty II skills developed using Misty2py library.\n\nRead the full documentation [here](https://chrisscarred.github.io/misty2py-skills)!\n\n## Documentations\n\nThe package `misty2py_skills` contains:\n\n- `misty2py_skills.face_recognition` module - a skill that greets people upon face detection with their name if known and prompts a face training session if their face (and therefore their name) is not known.\n- `misty2py_skills.hey_misty` module - a skill of Misty reacting to the *"Hey Misty"* keyphrase. *Note: due to internal works of Misty\'s API, Misty only reacts to the keyphrase once every runtime.*\n- `misty2py_skills.remote_control` module - a skill that lets you control Misty via a keyboard. *Note: since Misty is not a remote control race car, the controllability and responsiveness is not on the level of the typical remotelly controlled devices*.\n- `misty2py_skills.question_answering` module - a skill that allows to have a trivial conversation with Misty.\n\n- `misty2py_skills.demonstrations` sub-package which contains skills that demonstrate the workings of `misty2py` package but are not necessarily useful for a real world implementation as-is.\n\n  - `misty2py_skills.demonstrations.battery_printer` module - a skill that prints Misty\'s battery status every 250 ms in the terminal for the duration specified as the second CLI argument in seconds (optional, defaults to 2 seconds). Demonstrates working with events in `misty2py`.\n  - `misty2py_skills.demonstrations.explore` module - a skill that should theoretically perform SLAM mapping of an unknown room but due to misalignment of Misty\'s API documentation and the real underlying structures, mapping is not currently performed as it auto-stops after a few second from entering the SLAM mapping mode.\n\n- `misty2py_skills.essentials` sub-package for relatively simple skills that can be used as building blocks or are otherwise helpful for developing real-life skills.\n\n  - `misty2py_skills.essentials.free_memory` module - a skill that removes non-system audio, video, image and recording files from Misty\'s memory.\n  - `misty2py_skills.essentials.movement` module - a module containing the class `Movement` which handles Misty\'s movement. *Note: only driving is currently implemented.*\n\n- `misty2py_skills.expressions` sub-package for expressions (audio-visual characteristics of Misty). Currently contains these modules:\n\n  - `misty2py_skills.expressions.listening` module - a simple expression that makes Misty appear to be listening.\n  - `misty2py_skills.expressions.angry` module - a simple expression that makes Misty appear to be angry.\n\n- `misty2py_skills.utils` sub-package of utility modules, including:\n\n  - `misty2py_skills.utils.template` file - a template file for developing a skill with Misty2py.\n  - `misty2py_skills.utils.status` module - contains the classes `Status` and `ActionLog` which can be used to track the execution state of a script.\n  - `misty2py_skills.utils.converse` module - contains utility functions for speaking and printing data.\n  - `misty2py_skills.utils.utils` module - contains other utility functions.\n\n## Running the skills\n\nCopy the `.env.example` from the root directory of this repository into `.env` and replace the values of `MISTY_IP_ADDRESS` and `PROJECT_DIR` with appropriate values.\n\nIf you are running the skills from the source, run commands `pip install poetry` and `poetry install` to get the dependencies.\n\nIf you are running speech recognition-related skills, follow the directions below.\n\n### Running speech recognition-related skills\n\nSet up an account at [Wit.ai](https://wit.ai/).\n\nCreate a new app at [Wit.ai](https://wit.ai/). If you wish to run the skill `misty2py_skills.question_answering`, select the option "Import From a Backup" and use the file in `accompanying_data` in the root directory of this package\'s [repository](https://github.com/ChrisScarred/misty2py-skills) as a backup file.\n\nGo to the dashboard of the new app, select Settings under Management and get the Server Access Token.\n\nReplace the value of `WIT_AI_KEY` in your `.env` file with the Server Access Token.\n',
    'author': "Chris 'Scar(R)ed' Vajdík",
    'author_email': 'scarred.chris@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ChrisScarred/misty2py-skills',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
