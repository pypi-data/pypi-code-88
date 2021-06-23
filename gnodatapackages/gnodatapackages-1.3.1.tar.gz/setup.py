import setuptools
from os import path

# def readme():
with open('README.md') as f:
    long_description = f.read()
    

# def readme():
#     with open('README.rst') as f:
#         return f.read()
   
# this_directory = path.abspath(path.dirname(__file__))
# with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

    
setuptools.setup(
    name="gnodatapackages", # Replace with your own username
    version="1.3.1",
    author="charmandersgsg",
    author_email="charmandersgsg@gmail.com",
    description="data def packages for gno",
#     long_description = long_description,
    long_description="data def packages for gno",
    long_description_content_type="text/markdown",
    url="https://github.com/charmandersgsg/gnodatapackages",
    packages=['gnodatapackages'],
    include_package_data=True,
    install_requires=[
          'pandas',
          'ftfy',
          'fasttext',
      ],
    test_suite='nose.collector',
    tests_require=['nose'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)