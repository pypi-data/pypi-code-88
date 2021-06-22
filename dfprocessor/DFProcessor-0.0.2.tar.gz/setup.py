from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'Preprocessing tools for pandas dataframe'
LONG_DESCRIPTION = 'A package that allows gives you multiple tool to preprocess your pandas.core.frame.DataFrame.'

# Setting up
setup(
    name="DFProcessor",
    version=VERSION,
    author="Benjamín Serra",
    author_email="<benjaserrau@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'pandas', 'spacy', 'nltk', 're', 'io', 'math'],
    keywords=['python', 'preprocessing', 'pandas', 'preprocess', 'dataframe', 'toolkit'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Microsoft :: Windows",
    ]
)