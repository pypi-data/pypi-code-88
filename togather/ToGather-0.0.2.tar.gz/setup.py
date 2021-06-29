from distutils.core import setup

setup(
    name='ToGather',
    version='0.0.1',
    packages=[''],
    install_requires=['PyQt5'],
    entry_points={
        'console_scripts': [
            'ToGather = ToGather:main'
        ]
    },
    scripts=['ToGather.py'],
    url='',
    include_package_data=True,
    license='',
    author='ToGather',
    author_email='',
    description=''
)
