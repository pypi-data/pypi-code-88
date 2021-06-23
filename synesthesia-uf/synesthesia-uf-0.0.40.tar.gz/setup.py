from setuptools import setup, find_packages
import codecs
import os


VERSION = '0.0.40'
DESCRIPTION = 'A Python audio image creation tool'
LONG_DESCRIPTION = 'A Python audio image creation tool that takes audio and creates images from them.'

# Setting up
setup(
    name="synesthesia-uf",
    version=VERSION,
    author="Super Fun Adventure Club Dude Man Squad",
    author_email="<georgekolasa@ufl.edu",
    description=DESCRIPTION,
    packages=find_packages(),
    include_package_data = True,
    package_data = {
        # If any package contains *.txt files, include them:
        # And include any files found in the 'data' subdirectory
        # of the 'rawdata' package, also:
        'synesthesia': ['images/*.*', '*.svg', '*.png', '*.txt'],
    },
    url="https://github.com/cbaddeley/Synesthesia",
    license="GPL 3",
    install_requires=['PyQt5', 'librosa', 'essentia',
                      'pillow'],
    keywords=['audio', 'visualizer', "image"],

    entry_points =
    {   "console_scripts":
        [
            "syne = synesthesia:pmain_func"
        ]
    }

)