import setuptools
 
with open("README.md", "r",encoding='utf-8') as fh:
    long_description = fh.read()
 
setuptools.setup(
    name="bengaliwordcorrector",
    version="1.1.1",
    author="Abu Kaisar Mohammad Masum",
 
    author_email="abukaisar24@gmail.com",
 
    description="bengali automatic word corrector",
 
    long_description=long_description,

    long_description_content_type="text/markdown",
    url="https://github.com/kaisarmasum",
    packages=setuptools.find_packages(),
    package_data={'bengaliwordcorrector': ['data/Bengaliwordlist.txt']},
 
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
