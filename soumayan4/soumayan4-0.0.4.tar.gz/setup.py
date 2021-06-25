import codecs
import setuptools


setuptools.setup(
    name="soumayan4",
    version="0.0.4",
    author="Soumayan Bandhu Majumder",
    author_email="soumayanmajumder@gmail.com",
    description="This is a fake news detector trained on different languages and mainly on COVID19 domain",
    long_description_content_type="text/markdown",
    url="https://github.com/soumayan/fake-news-detection",
    license="MIT",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    install_requires=[
        "spacy==2.3.5",
        "polyglot",
        "pyicu",
        "Morfessor",
        "pycld2",
        "spacytextblob==0.1.7",
        "scikit-learn==0.23.1"
    ],
)