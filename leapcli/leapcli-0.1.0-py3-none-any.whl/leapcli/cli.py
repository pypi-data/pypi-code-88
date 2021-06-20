"""
Usage:

   cli.py init
"""

from docopt import docopt
def __main__():
    arguments = docopt(__doc__)
    print(arguments)

if __name__ == '__main__':
    __main__()
