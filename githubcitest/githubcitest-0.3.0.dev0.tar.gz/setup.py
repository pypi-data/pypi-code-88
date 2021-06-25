#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                                     #
#   BSD 3-Clause License                                                              #
#                                                                                     #
#   Copyright (c) 2021, Patrick Hohenecker                                            #
#   All rights reserved.                                                              #
#                                                                                     #
#   Redistribution and use in source and binary forms, with or without                #
#   modification, are permitted provided that the following conditions are met:       #
#                                                                                     #
#   1. Redistributions of source code must retain the above copyright notice, this    #
#      list of conditions and the following disclaimer.                               #
#                                                                                     #
#   2. Redistributions in binary form must reproduce the above copyright notice,      #
#      this list of conditions and the following disclaimer in the documentation      #
#      and/or other materials provided with the distribution.                         #
#                                                                                     #
#   3. Neither the name of the copyright holder nor the names of its                  #
#      contributors may be used to endorse or promote products derived from           #
#      this software without specific prior written permission.                       #
#                                                                                     #
#   THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"       #
#   AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE         #
#   IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE    #
#   DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE      #
#   FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL        #
#   DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR        #
#   SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER        #
#   CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,     #
#   OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE     #
#   OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.              #
#                                                                                     #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #


import setuptools


__author__ = "Patrick Hohenecker"
__copyright__ = "Copyright (c) 2021, Patrick Hohenecker"
__license__ = "BSD-3-Clause"
__version__ = "0.1.0"
__maintainer__ = "Patrick Hohenecker"
__email__ = "patrick.hohenecker@gmx.at"
__status__ = "Development"


# read the long description from the README file
long_description = ""


setuptools.setup(
        author="Patrick Hohenecker",
        author_email="patrick.hohenecker@gmx.at",
        classifiers=[
                "Programming Language :: Python :: 3.9"
        ],
        copyright="Copyright (c), 2021 Patrick Hohenecker",
        description="",
        install_requires=[
                "torch>=1.8.0"
        ],
        license="BSD-3-Clause",
        long_description=long_description,
        long_description_content_type="text/markdown",
        name="githubcitest",
        package_dir={"": "src/main/python"},
        packages=setuptools.find_packages("src/main/python"),
        python_requires=">=3.9",
        url="https://github.com/phohenecker/ci-test",
        version="0.3.0.dev0"
)
