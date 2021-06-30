import setuptools
with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()
setuptools.setup(
    name="chinacoordtran",
    version="1.1",
    author="thiswildidea",
    author_email="314984468@qq.com",
    description="Coordinate Transformation for china ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thiswildidea/chinacoordtran_py",
    packages=setuptools.find_packages(),
    classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: MIT License",
    "Operating System :: OS Independent",
    ],
)