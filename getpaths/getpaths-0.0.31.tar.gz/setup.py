'''
run the following to update module:

change version number
python3 setup.py sdist bdist_wheel
twine upload dist/* --verbose
'''


from setuptools import setup, find_packages
import os
import shutil

VERSION = '0.0.31' 
DESCRIPTION = 'Pathing Library'


# read the contents of your README file
from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

# get rid of certain folders if they exist
build_path = os.path.join(this_directory, 'build')
dist_path = os.path.join(this_directory, 'dist')
getpaths_info_path = os.path.join(this_directory, 'getpaths.egg-info')

if os.path.exists(build_path):
    shutil.rmtree(build_path)
if os.path.exists(dist_path):
    shutil.rmtree(dist_path)
if os.path.exists(getpaths_info_path):
    shutil.rmtree(getpaths_info_path)


# Setting up
setup(
        name="getpaths", 
        version=VERSION,
        author="Jv Kyle Eclarin",
        author_email="<jvykleeclarin@gmail.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type='text/markdown',
        packages=find_packages(),
        install_requires=[],
        project_urls={
        "Documentation": "https://pypi.org/project/getpaths/",
        "Code": "https://github.com/mathemusician/getpath",
        "Issue tracker": "https://github.com/mathemusician/getpath/issues",
        },
        
        keywords=['python', 'pathing', 'path', 'getpath'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 2",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)