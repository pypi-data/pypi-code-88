import setuptools

with open("README.md", "r", encoding="utf_8_sig") as fh:
    long_description = fh.read()

setuptools.setup(
    name="happyreport",
    version="0.0.10",
    author="wuhaoyu",
    author_email="wuhaoyu96@163.com",
    description="Standardized report mail sending module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.4',
    entry_points={'console_scripts': ['hrc = happyreport.cmd:main']},
    include_package_data=True,
    install_requires=['pandas']
    )
