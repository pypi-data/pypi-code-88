from setuptools import setup, find_packages

NAME = 'pypacktut'
VERSION = '0.4.5'
DESCRIPTION = 'Python package tutorial'
LONG_DESCRIPTION = 'Package package tutorial with a slightly longer description'
other_reqs = ['numpy>=1.14.5']
extra_reqs = {'interactive': ['matplotlib>=2.2.0']}

setup(
    name=NAME,
    version=VERSION,
    author="Nitin Singh",
    author_email="singh.nitin512@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=other_reqs,
    extras_require=extra_reqs,
    keywords=['python', 'package tutorial'],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)