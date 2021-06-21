import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="standard_fw_gen",
    version="0.0.1",
    author="Jack",
    author_email="JackLinZero@163.com",
    description="Standard firmware generate tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/JackLinXX_admin/standard_fw_gen",
    project_urls={
        "Bug Tracker": "https://gitee.com/JackLinXX_admin/standard_fw_gen/issues",
    },
    entry_points={
        "console_scripts":[
            "standard_fw_gen = src.standard_fw_gen:main"
        ]
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)