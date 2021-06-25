# -*- coding: utf-8 -*-
# Copyright 2020 PyePAL authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Model agnostic Python implementation of the epsilon-PAL algorithm"""

from distutils.core import setup
from pybind11.setup_helpers import Pybind11Extension, build_ext


eqeq_module = Pybind11Extension(
    "pyeqeq_eqeq", ["src/main.cpp"], include_dirs=["src"], extra_compile_args=["-O3"]
)


setup(
    ext_modules=[eqeq_module],
    cmdclass={"build_ext": build_ext},
    package_data={"": ["data/*.dat"]},
    include_package_data=True,
    headers=['src/main.h']
)
