import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setuptools.setup(
    name="autoKS",
    version="0.0.2",
    author="Wei Zi-Qian",
    author_email="weiziqian1996@163.com",
    description="A python package to process knowledge structure data automatically",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/weiziqian1996/autoKS",
    python_requires=">=3.8",
)
