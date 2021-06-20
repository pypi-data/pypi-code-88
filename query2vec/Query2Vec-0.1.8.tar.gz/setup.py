import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Query2Vec",
    packages=["Query2Vec"],
    version="0.1.8",
    license='MIT',
    author="Maede Ashofteh Barabadi",
    description="Query2Vec package using word2vec and tfidf",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        "scikit-learn==0.23.2",
        "gensim==4.0.1",
        "tqdm==4.61.0",
        "numpy==1.19.5"
    ],
    package_data={
        '': ['data/external/*']
    }
    ,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)
