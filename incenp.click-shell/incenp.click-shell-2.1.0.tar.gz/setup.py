# -*- coding: utf-8 -*-
# incenp.click_shell - A shell extension for Click
# Copyright © 2015 Clark Perkins
# Copyright © 2021 Damien Goutte-Gattat
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
#
# * Redistributions of source code must retain the above copyright
#   notice, this list of conditions and the following disclaimer.
#
# * Redistributions in binary form must reproduce the above copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
#
# * Neither the name of click-shell nor the names of its contributors
#   may be used to endorse or promote products derived from this
#   software without specific prior permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
# "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
# LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
# A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
# HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
# SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
# LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
# THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from setuptools import setup
from incenp.click_shell import __version__

# Use the README.md as the long description
with open('README.rst', 'r') as fh:
    LONG_DESCRIPTION = fh.read()

setup(
    name='incenp.click-shell',
    version=__version__,
    url="https://github.com/gouttegd/click-shell",
    author="Damien Goutte-Gattat",
    author_email="dgouttegattat@incenp.org",
    description="A shell extension for Click",
    long_description=LONG_DESCRIPTION,
    license='BSD',
    include_package_data=True,
    packages=[
        'incenp',
        'incenp.click_shell'
        ],
    zip_safe=False,
    install_requires=[
        'click>=6.0'
        ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: User Interfaces',
        'Topic :: System :: Shells',
        'Topic :: Utilities',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
        ],
    command_options={
        'build_sphinx': {
            'project': ('setup.py', 'Click-Shell'),
            'version': ('setup.py', __version__),
            'release': ('setup.py', __version__)
            }
        }
)
