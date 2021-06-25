import os
import sys


def root():
    """
    :return: Project root directory

    Alternative method
    os.path.dirname(sys.modules['__main__'].__file__)
    """

    return "/".join(sys.argv[0].split("/")[:-1])

