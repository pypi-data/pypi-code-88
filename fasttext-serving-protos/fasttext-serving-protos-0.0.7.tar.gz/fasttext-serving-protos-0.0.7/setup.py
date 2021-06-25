import setuptools
 
setuptools.setup(
    name="fasttext-serving-protos",
    version="0.0.7",
    author="NielsenIQ",
    author_email="gonzalo.delafuente.consultant@nielseniq.com",
    description=" FastText Serving Protocol Bufers Python implementation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.0',
)
