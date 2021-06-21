import os
from setuptools import setup


packages = []
for dirpath, dirnames, filenames in os.walk('quantities'):
    if '__init__.py' in filenames:
        packages.append('.'.join(dirpath.split(os.sep)))
    else:
        del(dirnames[:])


setup(
    author = 'Darren Dale',
    author_email = 'dsdale24@gmail.com',
    description = "Support for physical quantities with units, based on numpy",
    download_url = "http://pypi.python.org/pypi/quantities",
    keywords = ['quantities', 'units', 'physical', 'constants'],
    license = 'BSD',
    long_description = """Quantities is designed to handle arithmetic and
    conversions of physical quantities, which have a magnitude, dimensionality
    specified by various units, and possibly an uncertainty. See the tutorial_
    for examples. Quantities builds on the popular numpy library and is
    designed to work with numpy ufuncs, many of which are already
    supported. Quantities is actively developed, and while the current features
    and API are stable, test coverage is incomplete so the package is not
    suggested for mission-critical applications.

    .. _tutorial: http://python-quantities.readthedocs.io/en/latest/user/tutorial.html
    """,
    name = 'quantities-scidash',
    packages = packages,
    platforms = 'Any',
    requires = [
        'python (>=3.6)',
        'numpy (>=1.13)',
        ],
    url = 'http://python-quantities.readthedocs.io/',
    version = '0.12.4.3',
)
