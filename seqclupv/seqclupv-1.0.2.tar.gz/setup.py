import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="seqclupv",
    version="1.0.2",
    author="R. E. C. te Wierik",
    author_email="r.e.c.tewierik@student.tudelft.nl",
    description="An extension of the original 'SeqClu' algorithm that is characterized "
                "by voting for cluster prototypes.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/rtewierik/seqclupv",
    project_urls={
        "Bug Tracker": "https://github.com/rtewierik/seqclupv/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires=">=3.9",
    package_data={'': ['data/*/*.ts', 'data/handwriting/*']},
    install_requires=['fastdtw>=0.3.4',
                      'numpy>=1.20.3',
                      'seaborn>=0.11.1',
                      'matplotlib>=3.4.2',
                      'sklearn>=0.0',
                      'scipy>=1.6.3',
                      'pandas>=1.2.4',
                      'ipython>=7.24.1',
                      'xxhash>=2.0.2',
                      'psutil>=5.8.0',
                      'sktime>=0.6.1']
)
