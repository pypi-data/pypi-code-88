from setuptools import find_packages, setup
setup(
    name='pyreckless',
    packages=find_packages(include=['pyreckless']),
    version='0.1.0',
    description='Python Indicator Library for Automated Trading',
    author='onbirkod',
    license='MIT',
    install_requires=['numpy'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
)