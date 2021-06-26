import pathlib
from setuptools import setup, find_packages

# The directory containing this file
here = pathlib.Path(__file__).parent.resolve()

# The text of the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

# This call to setup() does all the work
setup(
    name="abd",
    version="0.0.1",
    description="Abstract base class for decorators",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/w13b3/abstract_base_decorator",
    author="wiebe",
    license="Mozilla Public License Version 2.0",
    python_requires='>=3.6.*, <4',
    classifiers=[  # https://pypi.org/classifiers/
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3 :: Only",
        "Typing :: Typed",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    keywords=["decorator abstract oop"],
    package_dir={'': 'abd'},
    packages=find_packages("", exclude=["/test"]),
    include_package_data=False,
    install_requires=[''],
    entry_points={},
)