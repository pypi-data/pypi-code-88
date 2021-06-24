import os, re
from setuptools import setup, find_packages

PKG = "mautil"
VERSIONFILE = os.path.join(PKG, "_version.py")
verstr = "unknown"
try:
    verstrline = open(VERSIONFILE, "rt").read()
except EnvironmentError:
    pass # Okay, there is no version file.
else:
    VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
    mo = re.search(VSRE, verstrline, re.M)
    if mo:
        verstr = mo.group(1)
    else:
        raise Exception("unable to find version in {}".format(VERSIONFILE))


setup(
    name = PKG,
    packages = find_packages(exclude=['examples']),
    version = verstr,
    license='MIT',
    description = 'deep learning training framework based on pytorch',
    author = 'Tom Ma',
    author_email = '40295257@qq.com',
    url = 'https://github.com/world2vec/mautil',
    keywords = ['deep learning framework', 'pytorch'],
    install_requires=[
        'torch>=1.6',
        'tqdm',
        'psutil',
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'Programming Language :: Python :: 3',
    ],
)
