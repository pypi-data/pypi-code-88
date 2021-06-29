"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
"""

import setuptools
import pathlib

here = pathlib.Path(__file__).parent.resolve()
long_description = (here / 'README.md').read_text(encoding='utf-8')

setuptools.setup(
    name='lsf-lions-sectioned-format',
    version='2021.06.29',
    author='Lion Kimbro',
    author_email='LionKimbro@gmail.com',
    description="Read/write LSF plain-text container format files",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/LionKimbro/lsf',
    py_modules = ['lsf'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: CC0 1.0 Universal (CC0 1.0) Public Domain Dedication',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
        'Operating System :: OS Independent',
        'Topic :: Text Processing :: General',
    ],
    keywords='textfile, text, container, format',  # Optional
    python_requires='>=3.6, <4'
)
