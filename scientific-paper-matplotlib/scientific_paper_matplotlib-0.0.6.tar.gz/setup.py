import setuptools

requirements = ['matplotlib', 'numpy', 'pandas']
with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

setuptools.setup(
    name="scientific_paper_matplotlib",
    version="0.0.6",
    author="Khaled Alamin",
    author_email="khaled.alamin@gmail.com",
    description="This package is for publishers who wants a ready_use plot configuration like label size and datetime config... etc",
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages = ['scientific_paper_matplotlib'],
    install_requires = requirements,
    #url="https://github.com/pypa/scientific_paper_matplotlib",
    #project_urls={
    #    "Bug Tracker": "https://github.com/pypa/scientific_paper_matplotlib/issues",
    #},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    #package_dir={"": "src"},
    #packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)