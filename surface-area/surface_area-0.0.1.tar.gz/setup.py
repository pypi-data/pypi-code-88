from setuptools import setup, find_packages
VERSION = '0.0.1'
DESCRIPTION = 'finds surface area of 3D shapes'
setup(
    name="surface_area",
    version=VERSION,
    author="Elliott Weiss",
    author_email="elliott.murray.weiss@gmail.com",
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python', 'math', 'shapes', 'area'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)