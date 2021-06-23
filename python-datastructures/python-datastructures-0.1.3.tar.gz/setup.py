# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['python_datastructures']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'python-datastructures',
    'version': '0.1.3',
    'description': 'Python datastructures package',
    'long_description': '![Test Build](https://github.com/TuTomasz/Python-Datastructures/workflows/Test%20Build/badge.svg)\n\n![Screenshot](assets/logo.png)\n\nPython-Datastructures is a Python library containing implementations of various data structures written purely in Python. Useful when preparing for interviews or building school projects. Allow the user to focus on developing your algorithms and not worry about finding python implementations of classic data structures.\n\n## Installation\n\nUse the package manager [pip](https://pip.pypa.io/en/stable/) to install python-datastructures.\n\n```bash\npip install python-datastructures\n```\n\n## Usage\n\nSample usage of the library. Import any datastructure from the list of supported datastructures.\n\n- Stack\n- Queue\n- DeQueue\n- SinglyLinkedList\n- DoublyLinkedList\n- CircularList\n- MaxHeap\n- MinHeap\n- Trie\n\n![](assets/demo.webp)\n\n```python\nfrom python_datastructures import MinHeap\n\narr = [2,3,18,29,7,82,1,9]\nheap = MinHeap(arr)\nprint(heap.peek()) # returns 1\n```\n\n## Documentation\n\nExplore the Different data structures and methods associated with them.\nDocumentation below describes the various methods associated with each data structure as well as a short description on what it does.\n\n[Read the docs](https://tutomasz.github.io/Python-Datastructures/docs/python_datastructures/index.html)\n\n## Development\n\nTo set up dev environment and work on the package clone the repository then run.\n\n```makefile\nmake setup\n```\n\nOther usefull development commands include:\n\n```makefile\nmake test               // run tests\nmake lint               // code formatting\nmake build              // build package localy\nmake install-build      // install local package globally\nmake uninstall-build    // uninstall local package gloablly\n```\n\n## Contributing\n\nPull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.\n\nPlease make sure to update tests as appropriate.\n\n## License\n\n[MIT](https://choosealicense.com/licenses/mit/)\n',
    'author': 'Tomasz Turek',
    'author_email': 'ttomaszito@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/TuTomasz/Python-Datastructures',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
