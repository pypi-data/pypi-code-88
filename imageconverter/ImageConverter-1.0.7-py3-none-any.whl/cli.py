"""
This module provides the command line interface for ImageConverter.
"""

import sys
import json
from argparse import ArgumentParser
from pathlib import Path
from os.path import isfile, realpath, dirname
from ImageConverter import VERSION
from .cli_dir.banner import Banner

def main(argv=None):
    _banner = Banner()
    _banner.intro()

if __name__ == '__main__':
    main()