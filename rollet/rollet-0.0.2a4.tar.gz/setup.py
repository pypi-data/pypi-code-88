from setuptools import setup, find_packages
import codecs
import os
import rollet

here = os.path.abspath(os.path.dirname(__file__))

long_description = open(os.path.join(here, "README.md"), encoding="utf8").read()

with open(os.path.join(here, "requirements.txt")) as fq:
    requirements = list(map(lambda x:x.strip(), fq.readlines()))

VERSION = rollet.__version__
DESCRIPTION = 'Collect data from various sources'

setup(
    name = "rollet",
    version = VERSION,
    author = "Opscidia (Tech)",
    author_email = "tech@opscidia.com",
    maintainer = "Loïc Rakotoson",
    maintainer_email = "loic.rakotoson@opscidia.com",
    description = DESCRIPTION,
    long_description_content_type = "text/markdown",
    long_description = long_description,
    license_files = ('LICENSE',),
    packages = find_packages(),
    include_package_data = True,
    install_requires = requirements,
    keywords = ['fetch', 'pull', 'extract', 'scrap'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires = '>=3.7',
    entry_points = {
        'console_scripts': [
            'rollet = rollet.runtime:rollet_extract'
        ]
    },
)