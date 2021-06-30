import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fmtsrc",
    version="0.0.5",
    author="yuki nakamura",
    author_email="naka_yk@live.jp",
    description="File or URL formatting",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yknaka/fmtsrc",
    project_urls={
        "Source File Formatting": "https://github.com/yknaka/fmtsrc",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['fmtsrc'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': [
            'fmtsrc = fmtsrc:main'
        ]
    },
)
