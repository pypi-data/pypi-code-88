from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.13'
DESCRIPTION = 'Calculating roots of quadratic equations'
LONG_DESCRIPTION = 'A package that allows one to input a,b,c coefficients and boolean for whether or not there are real' \
                   'roots.'

# Setting up
setup(
    name="quadroots",
    version=VERSION,
    author="Shaun Porwal",
    author_email="shaun.porwal@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['math', 'cmath', 're', 'argparse'],
    keywords=['python', 'quadratic', 'roots', 'calculator'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
