# Copyright (C) 2021 Aleksandr Popov

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.

# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" Pymuplot provides plotting of PMU data.

"""

from setuptools import setup
from pymuplot import __version__


DOCLINES = __doc__.split("\n")


INSTALL_REQUIRES = [
    'pyqtgraph>=0.12',
]


PACKAGES = [
    'pymuplot',
]


setup(
    name='pymuplot',
    version=__version__,
    description=DOCLINES[0],
    author="Aleksandr Popov",
    author_email="aleneus@gmail.com",
    license="LGPLv3",
    keywords="synchrophasor",
    url="https://github.com/aleneus/pymuplot",
    packages=PACKAGES,
    install_requires=INSTALL_REQUIRES,
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: X11 Applications :: Qt",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
)
