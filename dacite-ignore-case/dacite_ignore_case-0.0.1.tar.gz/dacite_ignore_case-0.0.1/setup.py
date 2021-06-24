import setuptools


setuptools.setup(
    name='dacite_ignore_case',
    version='0.0.1',
    description='Extends dacite.from_dict with a ignore case function',
    author='zkdev',
    author_email='dev@zeekay.dev',
    project_urls={
        "Bug Tracker": "https://github.com/zkdev/dacite-ignorecase/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
       'dacite',
    ],
    license='MIT',
    python_requires='>=3.9.*',
    package_dir={'': 'dacite_ignore_case'},
    packages=setuptools.find_packages(where='dacite_ignore_case'),
)
