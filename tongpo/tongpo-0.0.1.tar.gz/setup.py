from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'programming resources and utils'
LONG_DESCRIPTION = 'package to maintain my programming resources and utilities'

setup(
    name="tongpo",
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    author="pnowk",
    author_email="pnowk123@gmail.com",
    license='MIT',
    packages=find_packages(),
    install_requires=[],
    keywords='python',
    classifiers= [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        'License :: OSI Approved :: MIT License',
        "Programming Language :: Python :: 3",
    ]
)