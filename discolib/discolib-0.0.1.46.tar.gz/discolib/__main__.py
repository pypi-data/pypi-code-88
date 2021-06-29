#
# DISCo Python interface library
# Copyright (c) 2021 Greg Van Aken
#

"""DISCo: Descriptive Interface for Self-aware Components"""

import argparse
import discolib
import os
import pathlib

PROJECT_DIR_NAME = 'disco'
PROJECT_MAIN_NAME = 'main.py'

def get_parser():
    """Create a new argument parser."""
    package_name = os.path.dirname(__file__)
    parser = argparse.ArgumentParser(package_name)
    parser.add_argument('init', default=init())
    parser.add_argument('--version', '-v', action='version', version=discolib.__version__)
    return parser

def init():
    """Create a new example project."""
    project_path = pathlib.Path(os.getcwd(), PROJECT_DIR_NAME)
    os.mkdir(project_path)
    main_path = pathlib.Path(project_path, PROJECT_MAIN_NAME)
    with open(main_path, 'w') as main_file:
        main_file.write(
"""
from discolib.core import Disco
from discolib.io import DiscoIO, Validate

class SerialIO(DiscoIO):

    @Validate.read
    def read(self, length):
        \"\"\"Implement your own read() that will read bytes from your component(s).\"\"\"
        ...

    @Validate.write
    def write(self, data):
        \"\"\"Implement your own write() that send bytes to your component(s).\"\"\"
        ...


def main():
    disco = Disco(SerialIO())               # Initialize a DISCo object
    print(disco.get_attr_json(indent=2))    # Get all of the DISCo's attributes (as json)
    print(dir(disco))                       # Check out all of the attributes which can be interracted with via attr.setpoint = X.

if __name__ == '__main__':
    main()
"""
        )

def main(args=None):
    """Parse args and respond"""

    parser = get_parser()
    args = parser.parse_args(args)


if __name__ == '__main__':
    main()
