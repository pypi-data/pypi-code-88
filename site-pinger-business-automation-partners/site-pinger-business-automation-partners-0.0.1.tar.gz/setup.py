import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="site-pinger-business-automation-partners",
    version="0.0.1",
    author="Travis Lazar",
    author_email="business.automation.partners@gmail.com",
    description="A small package for pinging publicly available URLs for status",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/business-automation-partners/site_pinger",
    project_urls={
        "Bug Tracker": "https://github.com/business-automation-partners/site_pinger/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'requests',
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)