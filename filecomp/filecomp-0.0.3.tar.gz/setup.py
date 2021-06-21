from setuptools import setup
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.3'
DESCRIPTION = 'Function that finds maximal and minimal sized contents of a directory'

# Setting up
setup(
    name="filecomp",
    version=VERSION,
    author="Veefencer",
    author_email="daredevill2912@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=["filecomp"],
    install_requires=[],
    classifiers=[
            "Programming Language :: Python :: 3",
            "Operating System :: Microsoft :: Windows",
    ],
    python_requires='>=3.7'
)
