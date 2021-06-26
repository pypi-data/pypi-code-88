from setuptools import setup

requirements = open('requirements.txt').read().splitlines()

setup(python_requires='>=3.7', install_requires=requirements)
