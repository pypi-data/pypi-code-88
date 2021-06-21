
from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()


long_description = (here / 'README.md').read_text(encoding='utf-8')


setup(

    name='stormkitty',  # Required

    version='2.0.0',  # Required

    description='stormbound module',  # Optional

    long_description=long_description,  # Optional


    long_description_content_type='text/markdown',  # Optional (see note above)


    url='https://github.com/Nyelsonon/stormkitty',  # Optional

    author='nyelson',  # Optional

    author_email='nyelsonexists@gmail.com',  # Optional

    classifiers=[  # Optional
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate you support Python 3. These classifiers are *not*
        # checked by 'pip install'. See instead 'python_requires' below.
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
    ],


    keywords='sample, setuptools, development',  # Optional

    package_dir={'': 'src'},  # Optional

    packages=find_packages(where='src'),  # Required

    python_requires='>=3.6, <4',

    install_requires=['requests'],  # Optional
)
