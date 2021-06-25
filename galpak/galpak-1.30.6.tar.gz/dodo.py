# This file is the tasks repository for `doit`.
# See http://pydoit.org/tasks.html#intro

# Simply run `doit` from the projects directory to build the website.

import sys
import os, io
from os import listdir
from os.path import isfile, join, basename, abspath
import tarfile
import shutil
import re

from flask_frozen import Freezer

sys.path.insert(1, 'web')

from web.run import app, downloads_path

# sorting arrays
def sorted_aphanumeric(data):
    convert = lambda text: int(text) if text.isdigit() else text.lower()
    alphanum_key = lambda key: [ convert(c) for c in re.split('([0-9]+)', key) ]
    return sorted(data, key=alphanum_key)

__version__ = None
f = open('src/galpak/__version__.py')
exec(f.read())
print("Galpak version",__version__)

   

#### TASKS #####################################################################

DOIT_CONFIG = {'default_tasks': ['website']}


def task_doc():
    """
    Generate the documentation webpages using sphinx.
    """
    return {
        'actions': [build_doc],
        'verbosity': 2
    }


def task_tarball():
    """
    Generate a tarball of module, ready for download.
    """
    return {
        'actions': [build_tarball],
        'verbosity': 2
    }


def task_website():
    """
    Re-build the whole website. (documentation pages included)
    """
    return {
        'actions': [build_doc, build_website],
        'verbosity': 2
    }


def task_publish():
    """
    Upload the website to the remote webserver.
    """
    return {
        'actions': [publish],
        'verbosity': 2
    }


def task_all():
    """
    Do all the tasks.
    """
    return {
        'actions': [build_doc, build_tarball, build_website, publish],
        'verbosity': 2
    }


def task_test():
    """
    Run the test suite.
    """
    return {
        'actions': ['python -m pytest --ignore=tests/other'],
        'verbosity': 2
    }


### HELPERS ####################################################################

def filter_tarball(tarinfo):
    """
    A filter for the files we do not want in the tarball.
    Return None to exclude, or return the `tarinfo` if okay.
    """
    name = tarinfo.name
    # Remove the module directory name
    i = name.find('/')
    if i > 0:
        name = name[i+1:]
    # Exclude all these
    if name.endswith(".pyc") or \
            name.startswith('web') or \
            name.startswith('data/debug') or \
            name.startswith('data/tests') or \
            name.startswith('build') or \
            name.startswith('.idea') or \
            name.startswith('.git') or \
            name.startswith('slides') or\
            name.startswith('.tox') or\
            name.startswith('.doit') or \
            name.startswith('.pytest') or \
            name.startswith('dist') or \
            name.startswith('MGE') or \
            name.startswith('html') or \
            name.endswith('pymulti') or \
            name.endswith('eggs/') or \
            name.endswith('info'):
        return None
    return tarinfo


def make_tarball(output_filename, sources_dirnames):
    """
    Helper to make `output_filename` a tarball (.tar.gz) file from the files
    list `sources_dirnames`.
    """
    print("Generating tarball %s..." % output_filename)
    with tarfile.open(output_filename, "w:gz") as tar:
        for source_dirname in sources_dirnames:
            tar.add(source_dirname,
                    arcname=basename(source_dirname),
                    filter=filter_tarball)


#### URL GENERATORS ############################################################

# Freezer needs help to generate the downloads filenames
def downloads_filename():
    downloads_files = [f for f in listdir(downloads_path)
                       if isfile(join(downloads_path, f))]
    downloads_files = sorted_aphanumeric(downloads_files)
    downloads_files.reverse()
    downloads_files = downloads_files[0:5]
    print( os.path.abspath(downloads_path) )
    print(downloads_files)
    for tarball in downloads_files:
        yield {'filename': tarball}


#### ACTIONS ###################################################################

def build_doc():
    print("Generating sphinx documentation webpages...")
    os.chdir('doc')
    os.system('make html_silently')
    os.chdir('..')


def build_website():
    """
    Generate static webpages from the flask app.
    """
    print("Generating static webpages...")
    #print("config",app.config)
    app.config['JSON_SORT_KEYS']=False
    freezer = Freezer(app)
    freezer.register_generator(downloads_filename)
    freezer.freeze()

    # Copy sphinx documentation static pages into website's doc/
    source = abspath("doc/build/html")
    target = abspath("web/build/doc")
    print("Copy documentation from %s to %s..." % (source, target))
    shutil.rmtree(target, ignore_errors=True)
    shutil.copytree(source, target)


def build_tarball():
    #from galpak.__version__ import __version__
    # Read version.py

    source = abspath(".")
    target = abspath("build/galpak_"+__version__+".tar.gz")
    make_tarball(target, [source])


def publish():
    print("Upload files to webserver...")
    cmd = "rsync -r --delete --protocol=29 web/build/ nbouche@mistral:galpak/"
    os.system(cmd)

    print("Building wheel")
    cmd = 'rm dist/* -f '
    os.system(cmd)
    cmd = "python3 setup.py sdist bdist_wheel"
    os.system(cmd)
    #https://packaging.python.org/guides/using-testpypi/
    print("Pushing to pypi")
    cmd = "python3 -m twine upload dist/*"
    os.system(cmd)
