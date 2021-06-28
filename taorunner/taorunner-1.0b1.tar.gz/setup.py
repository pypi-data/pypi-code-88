import setuptools

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setuptools.setup(
    name="taorunner",  # Replace with your own username
    version="1.0beta1",
    author="Botao Yu",
    author_email="btyu@foxmail.com",
    description="A script tool to run a batch of task consecutively.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(),
    # package_data={},
    entry_points={
        'console_scripts': ['taorunner=taorunner.main:main'],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
