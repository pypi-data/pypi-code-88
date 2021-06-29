import setuptools

setuptools.setup(
    name='cg_learning_client',
    version='0.0.1',
    description='A client for connecting to LRS of cg',
    author='yml',
    author_email='windcome@outlook.com',
    packages=['cg_learning_client'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.5',
    install_requires=[
        'requests>=2.21.0'
    ]
)