import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="instpy",
    version="0.0.1",
    author="Carlos Enrique Yucra",
    author_email="calollikito12000@gmail.com",
    description="Inferencial Stadistics library",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="",
    LICENSE='MIT',
    classifiers=[
        "Intended Audience :: Education",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    keyword='inferencial stadistics',
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    install_requires=[
        'statsmodels>=0.12.0',
        'matplotlib>=3.3.0',
        'numpy>=1.19.2',
        'pandas>=1.1.2',
        'plotly>=4.12.0',
        'scipy>=1.5.2'
    ],
    python_requires=">=3.6",
)
