import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mhealth_datasets_upload",
    version="0.5",
    author="binodtc",
    author_email="binod.thapachhetry@gmail.com",
    description="A pacakge to scan an external drive for files and upload to the server.",
    url="https://bitbucket.org/mhealthresearchgroup/upload-data.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],

    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.8",
    install_requires=['paramiko==2.7.2','pywin32==228'],
    include_package_data=True
)