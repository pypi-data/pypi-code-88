from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '3.0.1'
DESCRIPTION = 'This will you to do Arithmetic operations very fast.'
LONG_DESCRIPTION = long_description

# Setting up
setup(
    name="Coolcalci",
    version=VERSION,
    author="Python Rohan",
    author_email="rohan9878787@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'calculator', 'calci', 'calculate', 'calculation', 'Arithmetic'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)