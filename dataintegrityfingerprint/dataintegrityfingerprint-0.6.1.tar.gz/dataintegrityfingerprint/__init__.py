__author__ = 'Oliver Lindemann <oliver@expyriment.org>, ' \
             'Florian Krause <florian@expyriment.org>'

__version__ = '0.6.1'

PACKAGE_NAME = "dataintegrityfingerprint"

from sys import version_info as _vi
if _vi.major< 3:
    raise RuntimeError("{} requires Python 3 or larger.".format(PACKAGE_NAME))

from .dif import DataIntegrityFingerprint
