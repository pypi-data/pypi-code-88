from setuptools import setup

with open('README.md') as file:
    long_description = file.read()
    file.close()

setup(
    name='Bakle Helpers',
    version='0.1.2',
    description='Package that provides multiple helpers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Bashir Akle',
    author_email='bashir.akle@gmail.com',
    url='https://github.com/bakle/Py-Validator',
    packages=['bakle_helpers'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'flake8'],
    package_data={'bakle_helpers': ['support/*.txt']}
)