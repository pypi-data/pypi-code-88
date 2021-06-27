import pathlib
from setuptools import setup, find_packages
import os
from os.path import join
import io

# The directory containing this file
#HERE = pathlib.Path(__file__).parent
HERE = os.path.abspath(os.path.dirname(__file__))

# The text of the README file
#README = (HERE / "README.md").read_text()
#with io.open(os.path.join(HERE, '02-SMSSpamDetection', 'README.md'), encoding='utf-8') as f:
#    README = '\n' + f.read()
with io.open(os.path.join(HERE, 'README.md'), encoding='utf-8') as f:
    README = '\n' + f.read()

# This call to setup() does all the work
setup(
    name="spamdetection",
    version="0.0.1",
    description="Classify text messages between 'spam' and 'ham'",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/fabio-a-oliveira/nuveo-teste-ia",
    author="Fabio Oliveira",
    author_email="info@realpython.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    packages=find_packages(exclude=("tests",)),
    include_package_data=True,
    install_requires=["scikit-learn", "pywebio"],
    entry_points={
        #"console_scripts": ["realpython=reader.__main__:main"]
        'console_scripts': ['spam-detection=spamdetection.__main__:main']
    },
)