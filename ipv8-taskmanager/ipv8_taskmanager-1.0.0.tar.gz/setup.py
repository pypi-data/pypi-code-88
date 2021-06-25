from setuptools import find_packages, setup
setup(
    name='ipv8_taskmanager',
    author='Tribler',
    description='The IPv8 TaskManager',
    long_description=('This module provides a set of tools to maintain a list of asyncio Tasks that are to be '
                      'executed during the lifetime of an arbitrary object, usually getting killed with it. This '
                      'module is extracted from the IPv8 main project.'),
    long_description_content_type='text/markdown',
    version='1.0.0',
    url='https://github.com/Tribler/py-ipv8',
    package_data={'': ['*.*']},
    packages=find_packages(),
    py_modules=[],
    install_requires=[],
    extras_require={},
    tests_require=[],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Topic :: Software Development :: Libraries :: Python Modules"
    ]
)
