# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------------
# documentation

r"""
package_cb65
============

Problem
-------

- Build a python package ready to be published and shared.
- Must provide:
  - Structure for documentation
  - Structure for code splitting into interface & implementation
  - Structure for `$ python -m $package` execution of the package
  - Structure for `$ pip install -e $package`
  - Structure for pinning the dependencies
  - Structure for versionning
  - Structure for testing
  - Structure for licensing
  - Structure for the readme
  - Structure for publication to PyPi

Solution
--------

1. $ pip install package_cb65
2. $ mkdir ./dependencies
3. $ deps_path=./dependencies build_component a_pkg
4. ⇒ ./dependencies/a_pkg has been built
   where: a_pkg verifies all conditions above.

"""

# --------------------------------------------------------------------------------
# interface

__all__ = [ "build" ]

def build():
    """docstring"""

    debug = os.environ.get("debug") == "true"
    if debug:
        logging.basicConfig(
            level=logging.DEBUG, force=True, format="%(levelname)s: %(message)s"
        )

    return _program({})["container"]

# --------------------------------------------------------------------------------
# Import

import argparse
import logging
import os
import re
from datetime import date
from pathlib import Path
from uuid import uuid4 as uuid
from functools import partial
from tools_09d3 import link

# --------------------------------------------------------------------------------
# Logger

logger = logging.getLogger(__name__)

# --------------------------------------------------------------------------------
# Argument parser

parser = argparse.ArgumentParser(description="Install user defined packages.")
arg_name = "name"
parser.add_argument(
    arg_name,
    help="name of the component. Example: a_component",
    default=None
)
fullname_author = "fullname"
parser.add_argument(
    fullname_author,
    help="Fullname of the author. Example: Evy Galois",
)
id_name = "id"
parser.add_argument(
    "--" + id_name,
    help="id of the component. Example: a171",
)

# --------------------------------------------------------------------------------
# Shortcut

def mkdir(a_path):
    a_path.mkdir(parents=True, exist_ok=False)
    return a_path

def mkfile(a_path, content):
    with a_path.open(mode="w", encoding="utf-8") as a_file:
        a_file.write(content)
    return a_path

# --------------------------------------------------------------------------------
# Instruction

def deps_path():
    try:
        value = Path(os.environ["deps_path"])
    except KeyError as e:
        msg = r"""The path to the dependencies directory must be specified.
It's where the package will be built.
The path should be stored in the environment variable: `deps_path`
for example:
  export deps_path=./dependencies
"""
        raise AssertionError(msg)

    return value

def args():
    return vars(parser.parse_args())

def name(args):
    return args[arg_name]

def fullname(args):
    return args[fullname_author]

def id(args):
    a_id = args[id_name]
    if a_id is None:
        a_id = str(uuid()).split("-")[1]

    return a_id

def identifier(name, id):
    return f"{name}_{id}"

def container(deps_path, identifier):
    return mkdir(deps_path / identifier)

def src(container):
    return mkdir(container / "src")

def pkg(src, identifier):
    return mkdir(src / identifier)

def tests(container):
    return mkdir(container / "tests")

def logs(container):
    return mkdir(container / "logs")

def docs(container):
    return mkdir(container / "docs")

def source_docs(docs):
    mkdir(docs / "source")

def build_docs(docs):
    mkdir(docs / "build")

def impl(identifier, pkg):
    path = pkg / "impl.py"
    content = f'''# -*- coding: utf-8 -*-

# --------------------------------------------------------------------------------
# Interface

__all__ = [ "something" ]

def something(file_loc, print_cols, a_int=1):
    """Gets and prints the spreadsheet's header columns

    Parameter

        file_loc : str
            The file location of the spreadsheet
        print_cols : bool, optional
            A flag used to print the columns to the console (default is False)
        a_int : int, default=1
            An example of a parameters with default value documented.

    Yield

        int
            Description of the anonymous integer return value.

    Raise

        LinAlgException
            If the matrix is not numerically invertible.

    Return

        list
            a list of strings representing the header columns

    Note

        provides additional information about the code, possibly including a discussion of the algorithm

    See also

        func_a : Function a with its description.
        func_b, func_c_, func_d
        func_e
    """
    return _something(file_loc, print_cols, a_int=1)

# --------------------------------------------------------------------------------
# Import

import logging

# --------------------------------------------------------------------------------
# Logger

logger = logging.getLogger(__name__)

# --------------------------------------------------------------------------------
# Implementation

def _something():
    """MAY be documented."""
    return 1
'''

    mkfile(path, content)


def init(pkg, identifier):
    path = pkg / "__init__.py"
    content = f'''# -*- coding: utf-8 -*-

r"""
{identifier}
{re.sub('.', '=', identifier)}

Problem
-------

1. A brief informal statement of the problem

  - give examples

2. The precise correctness conditions required of a solution


Solution
--------

3. Describe the solution

  - Whenever needed, explain the "why" of the design

"""

# --------------------------------------------------------------------------------
# Interface

from .impl import *
'''

    mkfile(path, content)

def main(identifier, pkg):
    path = pkg / "__main__.py"
    content = f"""# -*- coding: utf-8 -*-

from {identifier} import something

def main():
    print(something())

if __name__ == "__main__":
    main()
"""

    mkfile(path, content)

def pyproject(container):
    path = container / "pyproject.toml"
    content = f"""[build-system]
# gives a list of packages that are needed to build your package. Listing something
# here will only make it available during the build, not after it is installed.
requires = [
    "setuptools>=42",
    "wheel"
]
build-backend = "setuptools.build_meta"
"""
    mkfile(path, content)

def requirements(container):
    path = container / "requirements.txt"
    content = f"""# https://caremad.io/posts/2013/07/setup-vs-requirement/
# -e https://github.com/foo/bar.git#egg=bar
-e .
"""
    mkfile(path, content)

def impl_test(tests, identifier):
    path = tests / f"{identifier}_test.py"
    content = f'''# -*- coding: utf-8 -*-

from {identifier} import something

def test_{identifier}():
    """docstring"""
    assert something() == 1

'''
    mkfile(path, content)

def readme(container):
    path = container / "README"
    content = "README"
    mkfile(path, content)

def license(container, fullname):
    path = container / "LICENSE"
    today = date.today().isoformat()
    content = f"""MIT License

Copyright (c) {today} {fullname}

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE."""
    mkfile(path, content)

def gitignore(container, logs, docs):
    path = container / ".gitignore"
    content = f"""
/{logs.name}/
/{docs.name}/build/
__pycache__/
*.py[cod]
*$py.class
"""
    mkfile(path, content)

def cfg(container, identifier, fullname):
    path = container / "setup.cfg"
    content = f"""[metadata]
name = {identifier}
version = 0.0.1
author = {fullname}
author_email = todo@todo.com
description = A small example package
long_description = README
long_description_content_type = text/x-rst
url = https://github.com/phfrohring/python
project_urls =
    Bug Tracker = https://github.com/todo
classifiers =
    Programming Language :: Python :: 3
    License :: OSI Approved :: MIT License
    Operating System :: OS Independent

[options]
package_dir=
    =src
packages = find:
python_requires = >=3.6
install_requires=

[options.packages.find]
where=src

[options.extras_require]
dev =
  pytest
  sphinx
  black
  isort
  sphinx-rtd-theme
  build
  twine

[options.entry_points]
console_scripts =
    {identifier} = {identifier}.__main__:main
"""

    return mkfile(path, content)

def makefile(container, src, tests, logs, cfg):
    path = container / "makefile"
    content = f'''# Interface.
.PHONY: help test dev doc format clean
.DEFAULT_GOAL := help

# Shell commands are interpreted by Bash.
SHELL := /bin/bash

# The directory in which make is executed is considered the root directory.  `root
# directory` means that all relative directories are to be interpreted relative to
# this one.
# Example: the file named `a_file` has a path: `$(set_root)/a_file`
set_root := $(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

# This makefile
this_makefile := {path.name}

# This setup.cfg
this_setup_cfg := {cfg.name}

# Directory of sources.
set_src := {src.name}
points_src := $(shell find $(set_src) -type f -name "*.py")
$(set_src): $(points_src)
        @echo "Target: $@"
        @echo "  Newer dependencies: $?"
        @mkdir -p $@
        @touch $@

# Directory of docs.
root_dist := dist

# Directory of docs.
root_doc := docs
makefile_doc := $(root_doc)/Makefile
build_doc := $(root_doc)/build
set_doc := $(root_doc)/source
points_doc := $(shell find $(set_doc) -type f)
$(set_doc): $(points_doc)
        @echo "Target: $@"
        @echo "  Newer dependencies: $?"
        @mkdir -p $@
        @touch $@

# Directory of tests.
set_test := {tests.name}
points_test := $(shell find $(set_test) -type f -name "*.py")
$(set_test): $(points_test)
        @echo "Target: $@"
        @echo "  Newer dependencies: $?"
        @mkdir -p $@
        @touch $@

# Directory of logs.
set_log := {logs.name}
test_log := $(set_log)/test.log
dev_log := $(set_log)/dev.log

help:  ## Print help.
        @grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \\
awk 'BEGIN {{FS = ":.*?## "}}; {{printf "\\033[36m%-30s\\033[0m %s\\n", $$1, $$2}}'

test: $(test_log) ## Test package.
        @echo "Target: $@"
        @cat $<

dev: $(dev_log) ## Install a project in editable mode.
        @echo "Target: $@"
        @cat $<

doc: $(build_doc) ## Build documentation.
        @echo "Target: $@"
        @echo $(build_doc)/html/index.html &

format: ## Format code.
        @echo "Target: $@"
        @black $(set_src) $(set_test)

publish: ## Publish to PyPi.
        @echo "Target: $@"
        @python -m build; twine upload $(root_dist)/*

clean: ## Clean built targets.
        rm -rf $(set_log)/*
        rm -rf $(build_doc)/*
        rm -rf $(root_dist)/*

$(build_doc):  $(makefile_doc) $(set_src) $(set_doc) $(dev_log)
        @echo "Target: $@"
        @echo "  Newer dependencies: $?"
        @cd $(root_doc); $(MAKE) html
        @touch $@

$(test_log): $(set_test) $(set_src) $(this_makefile) $(dev_log)
        @echo "Target: $@"
        @echo "  Newer dependencies: $?"
        @-pytest $< > $@

$(dev_log): $(this_setup_cfg)
        @echo "Target: $@"
        @echo "  Newer dependencies: $?"
        @pip install -e .[dev] > $@

$(makefile_doc):
        @echo "Target: $@"
        @sphinx-quickstart --ext-autodoc --ext-intersphinx --ext-todo --ext-viewcode $(root_doc)

'''
    mkfile(path, content)

def setuppy(container, identifier):
    path = container / "setup.py"
    content = f"""import setuptools
setuptools.setup()
"""

    mkfile(path, content)

instructions = [
    deps_path,
    args,
    fullname,
    name,
    id,
    identifier,
    container,
    docs,
    source_docs,
    build_docs,
    src,
    tests,
    logs,
    cfg,
    makefile,
    pyproject,
    requirements,
    readme,
    license,
    gitignore,
    setuppy,
    pkg,
    impl_test,
    impl,
    init,
    main,
]

_program = partial(link, instructions)
