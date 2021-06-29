#! /usr/bin/env python3
'''

COPYRIGHT:
Copyright (c) 2015-2021, California Institute of Technology ("Caltech").
U.S. Government sponsorship acknowledged.

All rights reserved.

LICENSE:
Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice,
this list of conditions and the following disclaimer.

- Redistributions in binary form must reproduce the above copyright
notice, this list of conditions and the following disclaimer in the
documentation and/or other materials provided with the distribution.

- Neither the name of Caltech nor its operating division, the Jet
Propulsion Laboratory, nor the names of its contributors may be used to
endorse or promote products derived from this software without specific prior
written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
POSSIBILITY OF SUCH DAMAGE.

NTR:
'''

import os
import setuptools
import sys

# first item in list must be README file name
data_files_names = ["README.md", "LICENSE.txt", 'requirements.txt']
read_me_file = data_files_names[0]
with open(read_me_file, "rt") as f: description = f.read()
deps = ['flask']
setuptools.setup(name='ddnp',
                 version='1.0.0',
                 packages=setuptools.find_packages(),
                 setup_requires=deps,
                 src_root=os.path.abspath(os.path.dirname(__file__)),
                 install_requires=deps,
                 author='Al Niessner',
                 author_email='Al.Niessner@jpl.nasa.gov',
                 classifiers=["Programming Language :: Python :: 3",
                              "Operating System :: OS Independent",
                              'License :: Free To Use But Restricted',
                              'Development Status :: 5 - Production/Stable'],
                 description='Docker Data Network Proxy',
                 license='see LICENSE file for details',
                 long_description=description,
                 long_description_content_type="text/markdown",
                 keywords='docker data network proxy copy secret environment',
                 url='https://github.com/al-niessner/DCP')
