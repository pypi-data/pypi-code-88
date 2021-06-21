from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'A package to let your IDE know what JsMacros can do'
LONG_DESCRIPTION = 'This Package add all classes listed in the Doc to Python so you can autocomplete then in your IDE'

# Setting up
setup(
    name="JsMacrosAC",
    version=VERSION,
    author="Hasenzahn1",
    author_email="<motzer10@gmx.de>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'JsMacros', 'Autocomplete', 'Doc'],
    classifiers=[
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)