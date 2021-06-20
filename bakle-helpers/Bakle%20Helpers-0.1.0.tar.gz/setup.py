from setuptools import setup

setup(
    name='Bakle Helpers',
    version='0.1.0',
    description='Package that provides multiple helpers',
    author='Bashir Akle',
    author_email='bashir.akle@gmail.com',
    url='https://github.com/bakle/Py-Validator',
    packages=['bakle_helpers'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'flake8'],
    package_data={'bakle_helpers': ['support/*.txt']}
)