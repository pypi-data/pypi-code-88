import os
from setuptools import setup

current_dir = os.path.abspath(os.path.dirname(__file__))
README = open(os.path.join(current_dir, 'README.rst')).read()
REQUIRES_PYTHON = ">=3.5.0"
VERSION = open(os.path.join(current_dir, 'abcunit_backend', '__init__.py')).readline().split('"')[1]

reqs = [line.strip() for line in open('requirements.txt')]
dev_reqs = [line.strip() for line in open('requirements_dev.txt')]

docs_requirements = [
    "sphinx",
    "sphinx-rtd-theme",
    "nbsphinx",
    "pandoc",
    "ipython",
    "m2r2"
]

setup(
    name="abcunit-backend",
    version=VERSION,
    description="Backend solution for abcunit success / failure logs",
    long_description=README,
    author="Jonathan Haigh",
    author_email="jonathan.haigh@stfc.ac.uk",
    url="https://github.com/cedadev/abcunit-backend",
    python_requires=REQUIRES_PYTHON,
    license="BSD 2-Clause License",
    packages=["abcunit_backend"],
    install_requires=reqs,
    extras_require={"dev": dev_reqs, "docs": docs_requirements}
)
