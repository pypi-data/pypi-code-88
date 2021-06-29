import sys

__version__ = "0.1a"
__author__ = "Nagendra_2k3"


def cmd():
    args = sys.argv[1:]
    if len(args) < 1:
        print(f"usage: ...{args}")
