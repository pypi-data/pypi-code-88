#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.


from __future__ import print_function
from glob import glob
from os.path import join as pjoin
from pathlib import Path
import os
from setupbase import (
    create_cmdclass,
    get_version,
)
import setuptools

HERE = os.path.abspath(os.path.dirname(__file__))

COSAPP_CONFIG_DIR = Path.home() / ".cosapp.d"

name = "cosapp_lab"

# Get our version
version = get_version(pjoin(name, "_version.py"))
lab_path = os.path.join(HERE, name, "lab_static")
lab_static_path = os.path.join(lab_path, "static")
app_path = os.path.join(HERE, name, "app_static")

# Representative files that should exist after a successful build
jstargets = [
    os.path.join(HERE, "lib", "index.js"),
    os.path.join(HERE, name, "lab_static", "package.json"),
]
package_data_spec = {name: ["*"]}
labext_name = "cosapp_lab"

data_files_spec = [
    ("share/jupyter/labextensions/%s" % labext_name, lab_path, "*.*"),
    ("share/jupyter/labextensions/%s/static" % labext_name, lab_static_path, "*.*"),
    ("etc/jupyter/nbconfig/notebook.d", "jupyter-config", "cosapp_lab.json"),
    (
        "etc/jupyter/jupyter_notebook_config.d",
        "jupyter-config",
        "cosapp_lab_server.json",
    ),
]

cmdclass = create_cmdclass(
    package_data_spec=package_data_spec, data_files_spec=data_files_spec
)

# cmdclass = create_cmdclass(
#     "jsdeps", package_data_spec=package_data_spec, data_files_spec=data_files_spec
# )

# cmdclass["jsdeps"] = combine_commands(
#     install_npm(HERE, build_cmd="build", npm=["jlpm"]),
#     ensure_targets(jstargets)
# )


setup_args = dict(
    scripts=glob(pjoin("scripts", "*")),
    cmdclass=cmdclass,
    entry_points={
        "console_scripts": [
            "cosapp=cosapp_lab.main:cosapp",
        ],
    },
)

if __name__ == "__main__":

    setuptools.setup(**setup_args)
    if not COSAPP_CONFIG_DIR.exists():
        COSAPP_CONFIG_DIR.mkdir(parents=True, exist_ok=True)
