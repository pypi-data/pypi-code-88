import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vinfo",
    version="0.0.1",
    author="yoshiyasu takefuji",
    author_email="takefuji@keio.jp",
    description="video or image file information ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ytakefuji/vinfo",
    project_urls={
        "Bug Tracker": "https://github.com/ytakefuji/vinfo",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    py_modules=['vinfo'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    entry_points = {
        'console_scripts': [
            'vinfo = vinfo:main'
        ]
    },
)
