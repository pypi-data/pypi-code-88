
from setuptools import find_packages, setup
from apollopy.__init__ import VERSION

with open("README.md") as f:
    README = f.read()

setup(
    name="apollopy",
    version=VERSION,
    description="A basic CLI tool which helps you being healthy.",
    long_description_content_type="text/markdown",
    long_description=README,
    url="https://bitbucket.org/shravannn/apollo/",
    author="Shravan Asati",
    author_email="dev.shravan@protonmail.com",
    packages=find_packages(),
    install_requires=["plyer", "click", "pyttsx3"],
    license='BSD',
    entry_points='''
    [console_scripts]
    apollo=apollopy.__init__:base
    '''
)
