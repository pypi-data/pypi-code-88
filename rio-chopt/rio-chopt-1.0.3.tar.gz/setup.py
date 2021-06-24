# Copyright 2021 Chainopt LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import find_packages, setup


EXTRAS = {
    
}

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

REQUIRES = []
with open('requirements.txt') as f:
    for line in f:
        line, _, _ = line.partition('#')
        line = line.strip()
        if ';' in line:
            requirement, _, specifier = line.partition(';')
            for_specifier = EXTRAS.setdefault(':{}'.format(specifier), [])
            for_specifier.append(requirement)
        else:
            REQUIRES.append(line)


setup(
    name="rio-chopt",
    version="1.0.3",
    packages=find_packages(),
    author="Chainopt",
    author_email="support@chainopt.com",
    license="Apache License Version 2.0",
    description="This utility helps you deploy your code as an API locally on your machine",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/pypa/rio-chopt",
    keywords=["Swagger", "OpenAPI", "ModelOps","CLI","DataScience"],
    project_urls={
        "Bug Tracker": "https://github.com/chainopt/rio-cli/issues",
    },
    
    classifiers=[
        "Topic :: Utilities",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Information Technology",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    include_package_data=True,
    install_requires=REQUIRES,
    entry_points="""
        [console_scripts]
        rio=rio.cli:cli
    """,
)
