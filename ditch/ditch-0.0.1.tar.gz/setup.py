from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'programming resources'
LONG_DESCRIPTION = 'package to maintain my programming resources'

setup(
    name="ditch",
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