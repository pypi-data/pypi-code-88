from setuptools import setup


with open('README.md') as README:
    description = README.read()

setup(
    name='strip-spreadsheet',
    version='1.0.0',
    description='Strip a spreadsheet of extra spaces and blank-celled rows',
    py_modules=['strip_spreadsheet'],
    package_dir={'': 'src'},
    long_description=description,
    long_description_content_type='text/markdown',

    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Operating System :: OS Independent',
    ]
    )
