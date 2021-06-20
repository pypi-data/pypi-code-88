import os
from setuptools import find_packages, setup

__author__ = "Guanjie Wang"
__email__ = "gjwang@buaa.edu.cn"
__date__ = " 24/06/2020"


NAME = 'matfleet'
VERSION = '0.0.5'
DESCRIPTION = 'test'
README_FILE = os.path.join(os.path.dirname(__file__), 'README.md')
LONG_DESCRIPTION = open(README_FILE, encoding='UTF8').read()

REQUIREMENTS = []
URL = "https://gitee.com/alkemiems/matfleet"
AUTHOR = __author__
AUTHOR_EMAIL = __email__
LICENSE = 'MIT'
PACKAGES = find_packages()
# cmdclass = {'sdist': sdist}
PACKAGE_DATA = {}
ENTRY_POINTS = {}
# PACKAGE_DATA = {"potentialmind.data": ["fp/*.stp", "xsf/*.xsf"],
#                 "potentialmind.gui": ["generate/*.ui", "train/*.ui", "predict/*.ui", "pmlib/*.ui"]}


# # PACKAGE_DATA = {}
ENTRY_POINTS = {
    "console_scripts": (
        "pic2pdf = matfleet.untilities.mang_jpg2pdf:pictures2pdf"
    ),
}


def setup_package():
    setup(
        name=NAME,
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author=AUTHOR,
        author_email=AUTHOR_EMAIL,
        license=LICENSE,
        packages=find_packages(),
        package_data=PACKAGE_DATA,
        include_package_data=True,
        entry_points=ENTRY_POINTS,
        install_requires=REQUIREMENTS,
        cmdclass={},
        zip_safe=False,
        url=URL
    )


if __name__ == '__main__':
    setup_package()
