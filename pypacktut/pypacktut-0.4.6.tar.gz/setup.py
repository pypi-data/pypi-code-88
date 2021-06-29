from setuptools import setup, find_packages

NAME = 'pypacktut'
VERSION = '0.4.6'
DESCRIPTION = 'Python package tutorial'
other_reqs = ['numpy>=1.14.5']
extra_reqs = {'interactive': ['matplotlib>=2.2.0']}

with open("README.md", "r", encoding="utf-8") as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name=NAME,
    version=VERSION,
    author="Nitin Singh",
    author_email="singh.nitin512@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    install_requires=other_reqs,
    extras_require=extra_reqs,
    url="https://github.com/pypacktut",
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "pypacktut"},
    packages=find_packages(where="pypacktut"),
    python_requires=">=3.6"
)