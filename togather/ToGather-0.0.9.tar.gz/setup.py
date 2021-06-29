import setuptools

setuptools.setup(
    name='ToGather',
    version='0.0.9',
    packages=setuptools.find_namespace_packages(include=['bin','bin.*']),
    package_data={'': ['bin/*']},
    include_package_data=True,
    install_requires=['PyQt5'],
    entry_points={
        'console_scripts': [
            'ToGather = bin.ToGather:main'
        ]
    },
    url='',
    license='',
    author='ToGather',
    author_email='',
    description=''
)
