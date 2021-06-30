from setuptools import setup, find_packages

VERSION = '0.0.2'
DESCRIPTION = 'My first Python package'

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()


# Setting up
setup(
    name="python-comparator",
    version=VERSION,
    author="Sanyam Arya",
    author_email="er.sanyam.arya@gmail.com",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    url="https://github.com/gituser/test-tackage",
    license='MIT',
    packages=find_packages(),
    install_requires=[],

    keywords=['python', 'compare', 'compare values'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3",
)
