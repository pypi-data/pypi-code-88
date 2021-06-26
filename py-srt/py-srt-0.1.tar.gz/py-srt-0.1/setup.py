from setuptools import setup, find_packages
#from distutils.core import setup
setup(
    name='py-srt',
    version='0.1',
    author = 'sayam.py',
    url='https://github.com/Py',
    description='A simple cmd-line program, py',
    long_description='https://github.com/sayampy/Py',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        py=py.cli:cli
    ''',
)
