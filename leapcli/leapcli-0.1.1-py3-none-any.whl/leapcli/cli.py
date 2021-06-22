"""Tensorleap CLI.

Usage:
  leap init (--tensorflow|--pytorch) [PROJECT] [ORG]
  leap login [API_KEY]
  leap check
  leap push EXPERIMENT

Arguments:
  EXPERIMENT    Name of experiment.
  PROJECT       Project name (default: current directory name).
  ORG           Organization name (default: Git origin).

Options:
  -h --help     Show this screen.
  --version     Show version.
"""

from docopt import docopt
def __main__():
    arguments = docopt(__doc__)
    print(arguments)

if __name__ == '__main__':
    __main__()
