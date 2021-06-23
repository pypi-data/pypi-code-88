##########################################################################
# Track Analyzer - Quantification and visualization of tracking data     #
# Authors: Arthur Michaut                                                #
# Copyright 2016-2019 Harvard Medical School and Brigham and             #
#                          Women's Hospital                              #
# Copyright 2019-2021 Institut Pasteur and CNRS–UMR3738                  #
# See the COPYRIGHT file for details                                     #
#                                                                        #
# This file is part of Track Analyzer package.                           #
#                                                                        #
# Track Analyzer is free software: you can redistribute it and/or modify #
# it under the terms of the GNU General Public License as published by   #
# the Free Software Foundation, either version 3 of the License, or      #
# (at your option) any later version.                                    #
#                                                                        #
# Track Analyzer is distributed in the hope that it will be useful,      #
# but WITHOUT ANY WARRANTY; without even the implied warranty of         #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the           #
# GNU General Public License for more details .                          #
#                                                                        #
# You should have received a copy of the GNU General Public License      #
# along with Track Analyzer (COPYING).                                   #
# If not, see <https://www.gnu.org/licenses/>.                           #
##########################################################################


from setuptools import setup, find_packages

from track_analyzer import __version__ as tra_vers

setup(name='track_analyzer',
      version=tra_vers,
      description="Track Analyzer: quantification and visualization of tracking data",
      long_description=open('README.md').read(),
      long_description_content_type="text/markdown",
      author="Arthur Michaut",
      author_email="arthur.michaut@gmail.com",
      url="https://gitlab.pasteur.fr/track-analyzer/track-analyzer",
      download_url="https://pypi.org/project/track-analyzer/",
      license="GPLv3",
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Console',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Intended Audience :: Science/Research',
          'Topic :: Scientific/Engineering :: Bio-Informatics',
          ],
      python_requires='>=3.6',
      install_requires=[i for i in [l.strip() for l in open("requirements.txt").read().split('\n')] if i],
      # zip_safe=False,
      packages=[p for p in find_packages() if p != 'tests'],
      # file where some variables must be fixed by install
      entry_points={
          'console_scripts': [
              'traj_analysis=track_analyzer.scripts.analyze_tracks:main',
              'map_analysis=track_analyzer.scripts.analyze_maps:main',
          ]
      }
      )

