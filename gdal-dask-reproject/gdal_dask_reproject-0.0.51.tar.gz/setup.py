import sys
from setuptools import setup
import param
import re


version = param.version.get_setup_version(__file__, 'cc_reproject', archive_commit="$Format:%h$")


if version == 'None':
    sys.exit("Param seems to be unable to find the version of your package. Are you sure you tagged it with annotation?")


if 'sdist' in sys.argv and 'bdist_wheel' in sys.argv:
    try:
        version = re.split('((\d+\.)+(\d+[^\.|\+|\s]*))', version)[1]
    except IndexError:
        sys.exit("Param can't parse your version correctly; are you sure you entered it as a set of digits separated by dots in the tag?")


install_requires = [
    'param',
    'pyct <=0.4.6',
    'dask[complete]',
    'pyproj',
    'rasterio',
    'rioxarray',
]

extras_require = {
    'tests': [
        'pytest',
    ]
}

setup_args = dict(
    name='gdal_dask_reproject',
    version=version,
    install_requires=install_requires,
    tests_require=extras_require['tests'],
    zip_safe=False,
    packages=[
        'cc_reproject',
        'cc_reproject.tests'
        ],
    include_package_data=True,
    # entry_points={
    #     'console_scripts': [
    #         'cc_reproject = cc_reproject.__main__:main'
    #     ]
    # }
)


if __name__ == '__main__':
    setup(**setup_args)
