# SPDX-FileCopyrightText: 2014 MicroPython & CircuitPython contributors (https://github.com/adafruit/circuitpython/graphs/contributors)
#
# SPDX-License-Identifier: MIT
import os
import site
from datetime import datetime
from typing import List

from setuptools import setup
from pathlib import Path
import subprocess
import re


# git_out = subprocess.check_output(["git", "describe", "--tags"])
# version = git_out.strip().decode("utf-8")
#
# # Detect a development build and mutate it to be valid semver and valid python version.
# pieces = version.split("-")
# if len(pieces) > 2:
#     pieces.pop()
#     # Merge the commit count and build to the pre-release identifier.
#     pieces[-2] += ".dev." + pieces[-1]
#     pieces.pop()
# version = "-".join(pieces)

def local_scheme(version):
    return ""

setup(
    name="foamyguy-test-actions-deploy",
    description="Testing actions and pypi releasing",
    url="https://github.com/FoamyGuy/test_actions_deploy",
    maintainer="Tim Cocks",
    maintainer_email="foamyguy@gmail.com",
    author_email="foamyguy@gmail.com",
    #version=version,
    setup_requires=["setuptools_scm", "setuptools>=38.6.0"],
    use_scm_version={"local_scheme": local_scheme},
    license="MIT",

    py_modules=["foamyguy_testing_actions"]
)
