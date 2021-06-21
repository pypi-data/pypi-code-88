import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hi-covid-bot",
    version="0.0.1",
    author="Davin Takahashi, Zion Basque",
    author_email="dvntaka@yahoo.com",
    description="Web Scraper for COVID-19 cases in Hawaii that posts results to Twitter or email.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dvntaka/hawaii_coronavirus_bot",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)