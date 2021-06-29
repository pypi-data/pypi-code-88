import setuptools

setuptools.setup(
    name='ToGather',
    version='0.0.4',
    packages=setuptools.find_namespace_packages(include=['bin','bin.*']),
    install_requires=['PyQt5'],
    entry_points={
        'console_scripts': [
            'ToGather = bin.ToGather:main'
        ]
    },
    url='',
    package_data={'': ['bin/*.ui', 'bin/Logo.png']},
    include_package_data=True,
    license='',
    author='ToGather',
    author_email='',
    description=''
)
