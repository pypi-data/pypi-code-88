import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="html-index",
    version="1.0.7.2",
    author="Madeline Sparkle",
    author_email="muguang138@gmail.com",
    description="HTML file indexing generator.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Mg138/html-index",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    entry_points={
        'console_scripts': [
            'index = html_index.index:main'
        ]
    },
    python_requires=">=3.6",
    include_package_data=True,
    install_requires=[
        'PyYAML~=5.4.1'
    ]
)
