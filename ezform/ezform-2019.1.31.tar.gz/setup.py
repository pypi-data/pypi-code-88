# -*- python -*-
#
# Copyright 2016, 2017, 2018, 2019 Xingeng Chen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from setuptools import find_packages, setup


class PkgSetup(object):
    NAME = 'ezform'
    DESCRIB = 'simple extensions to Django forms'
    LICENSE = 'Apache License 2.0'
    AUTHOR = 'Xingeng Chen'

    CLASSIFIERS = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ]

    KEYWORDS = ('Django', 'Data Validation')

    @classmethod
    def read_src_file(cls, *parts):
        import codecs
        import os
        dir_path = os.path.abspath(os.path.dirname(__file__))
        with codecs.open(os.path.join(dir_path, *parts), 'r') as _f:
            return _f.read()

    @classmethod
    def find_version(cls, *file_paths):
        import re

        MSG_VERSION_STRING_NOTFOUND = 'Unable to find version string.'

        version_file = cls.read_src_file(*file_paths)
        version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]", version_file, re.M)
        if version_match:
            return version_match.group(1)
        raise RuntimeError(MSG_VERSION_STRING_NOTFOUND)

    @classmethod
    def getConfig(cls):
        cfg = {
            'name': cls.NAME,
            'author': cls.AUTHOR,
            'license': cls.LICENSE,
            'classifiers': cls.CLASSIFIERS,
            'keywords': cls.KEYWORDS,
            'version': cls.find_version(cls.NAME, '__init__.py'),
            'packages': find_packages(),
            'platforms': 'Any',
            'python_requires': '>=2.7',
            'install_requires': ['Django',],
            'description': cls.DESCRIB,
        }
        return cfg


setup(**(PkgSetup.getConfig()))
