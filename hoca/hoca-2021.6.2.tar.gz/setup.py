# Copyright (C) 2021 Jean-Louis Paquelin <jean-louis.paquelin@villa-arson.fr>
#
# This file is part of the hoca (Higher-Order Cellular Automata) library.
#
# hoca is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# hoca is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with hoca.  If not, see <http://www.gnu.org/licenses/>.

import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="hoca",
    version="2021.6.2",
    description="Provides a set of tools to implement Higher-Order Cellular Automata populations",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/jlp6k/hoca/",
    author="Jean-Louis Paquelin and Enrico Formenti",
    author_email="g-art-dev@villa-arson.org",  # TODO: replace by hoca@g-art.net when ready
    license="GNU Lesser General Public License v3 or later",
    # For classifiers see: https://pypi.org/classifiers/
    classifiers=[
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Topic :: Software Development",
        "Topic :: Software Development :: Libraries",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Artificial Life",
        "Topic :: Scientific/Engineering :: Image Processing",
        "Topic :: Artistic Software",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
    ],
    # TODO: add keywords
    keywords=["cellular automata", "agents"],
    packages=["hoca",
              "hoca.core",
              "hoca.monitor",
              "hoca.demo"],
    include_package_data=True,
    python_requires='>=3',
    install_requires=["numpy >= 1.20.1", "Pillow >= 7.0.0", "av >= 8.0.3"],
)
