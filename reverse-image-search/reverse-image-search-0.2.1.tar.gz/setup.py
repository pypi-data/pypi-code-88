# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['reverse_image_search']

package_data = \
{'': ['*']}

install_requires = \
['joblib>=1.0.1,<2.0.0',
 'opencv-python>=4.5.2,<5.0.0',
 'scikit-image>=0.18.1,<0.19.0',
 'tabulate>=0.8.9,<0.9.0']

entry_points = \
{'console_scripts': ['reverse_image_search = reverse_image_search.cli:cli']}

setup_kwargs = {
    'name': 'reverse-image-search',
    'version': '0.2.1',
    'description': 'Reverse Image Search',
    'long_description': "# Reverse Image Search\nForgot where you left the original of that beautiful photo? If you still have the thumbnail, you can try to find it using Reverse Image Search!\n\n### Installation\n```\npip install reverse-image-search\n```\n\n### Usage\n```bash\n$ reverse_image_search images/hills-2836301_1920_thumbnail.jpg images/\nFinding similar images...\n- to: images/hills-2836301_1920_thumbnail.jpg\n- in: images\n- filetypes: ['.jpg', '.jpeg']\n- threshold: 0.9\n\nMatches:\nfilepath                                 similarity\n---------------------------------------  ------------\nimages/hills-2836301_1920_thumbnail.jpg  100%\nimages/hills-2836301_1920.jpg            99%\n\n```\n\n### How does it work?\n1. load the image you want to search for.\n2. Walk through your files at a given path.\n3. Compares the structural similarity between images using Scikit-Image.\n4. Print the results in a table when the similarity is above a certain threshold.\n\n\n### Credits\nImage from https://pixabay.com/photos/hills-india-nature-kodaikanal-2836301/\n",
    'author': 'Your Name',
    'author_email': 'you@example.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
