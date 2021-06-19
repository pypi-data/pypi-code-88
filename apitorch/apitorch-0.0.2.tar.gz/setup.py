from setuptools import setup

DESCRIPTION = 'API Torch Python client'
LONG_DESCRIPTION = ''
NAME = 'apitorch'
VERSION = '0.0.2'

requirements = [
    'requests>=2.20.0,<3.0'
]
test_requirements = []  # ['vcrpy']

setup(
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
    ],
    description=DESCRIPTION,
    install_requires=requirements,
    name=NAME,
    license='MIT',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    # package_dir={'apitorch': "apitorch"},
    packages=['apitorch'],
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/apitorch/apitorch.py',
    version=VERSION,
)
