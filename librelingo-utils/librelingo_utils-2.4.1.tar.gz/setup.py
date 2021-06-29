# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['librelingo_utils']

package_data = \
{'': ['*']}

install_requires = \
['librelingo-types>=3.0.0,<4.0.0']

setup_kwargs = {
    'name': 'librelingo-utils',
    'version': '2.4.1',
    'description': 'Utilities to be used in LibreLingo-related-packages',
    'long_description': '<a name="librelingo_utils"></a>\n# librelingo\\_utils\n\nlibrelingo-utils contains utility functions that are meant to make it easier\nto create Python software that works with LibreLingo courses.\n\n<a name="librelingo_utils.utils"></a>\n# librelingo\\_utils.utils\n\n<a name="librelingo_utils.utils.calculate_number_of_levels"></a>\n#### calculate\\_number\\_of\\_levels\n\n```python\ncalculate_number_of_levels(nwords, nphrases)\n```\n\nCalculates how many levels a skill should have\n\n<a name="librelingo_utils.utils.clean_word"></a>\n#### clean\\_word\n\n```python\nclean_word(word)\n```\n\nRemove punctuation and other special characters from a word.\n\n<a name="librelingo_utils.utils.get_dumb_opaque_id"></a>\n#### get\\_dumb\\_opaque\\_id\n\n```python\nget_dumb_opaque_id(name, id_, salt="")\n```\n\nGenerate a unique, opaque ID based on a name, and id_ and a salt\nid\n\n<a name="librelingo_utils.utils.get_opaque_id"></a>\n#### get\\_opaque\\_id\n\n```python\nget_opaque_id(obj, salt="")\n```\n\nGenerate a unique, opaque ID based on a type and a type specific\nid\n\n<a name="librelingo_utils.utils.audio_id"></a>\n#### audio\\_id\n\n```python\naudio_id(language, text)\n```\n\nGenerate the ID that will identify the audio file of a sentence.\n\n<a name="librelingo_utils.utils.iterate_phrases"></a>\n#### iterate\\_phrases\n\n```python\niterate_phrases(course)\n```\n\n"Flatten" a course into a sequence of phrases\n\n',
    'author': 'Dániel Kántor',
    'author_email': 'git@daniel-kantor.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
