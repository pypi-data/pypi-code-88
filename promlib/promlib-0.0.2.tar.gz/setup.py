# -*- coding: utf-8 -*-

from setuptools import (
    find_packages,
    setup,
)

with open('./README.md') as readme:
    long_description = readme.read()

setup(
    name="promlib",
    scripts=["promlib.py"],
    version="0.0.2",
    description="A collection of tools for software project management. Because developers are managers too.",
    long_description_content_type='text/markdown',
    long_description=long_description,
    author='lim',
    author_email='louaimisto@gmail.com',
    url='https://github.com/lmist/promlib',
    include_package_data=True,
    install_requires=[
    ],
    python_requires='>=3.6,<4',
    license="MIT",
    zip_safe=False,
    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.9',
    ],




)
