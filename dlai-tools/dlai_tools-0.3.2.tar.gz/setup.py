import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="dlai_tools",  # Replace with your own username
    version="0.3.2",
    author="Andrés Castillo",
    author_email="andcastillo@gmail.com",
    description="Deployment script for notebooks",
    long_description="Comming soon",
    long_description_content_type="text/markdown",
    url="https://github.com/https-deeplearning-ai/dlai_tools",
    download_url = 'https://github.com/https-deeplearning-ai/dlai_tools/releases/tag/0.3.2',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
