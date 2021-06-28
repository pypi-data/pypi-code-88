import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ml-platform-client",
    version="0.3.22",
    author="JeremyXin",
    author_email="chengjiexin@emotibot.com",
    description="emotibot ml platform client for python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    # url="https://github.com/pypa/sampleproject",
    packages=setuptools.find_packages(),
    install_requires=[
        "flask==1.1.1"
        "flask-restful==0.3.8",
        "minio==5.0.5",
        "pymysql==0.7.11"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
