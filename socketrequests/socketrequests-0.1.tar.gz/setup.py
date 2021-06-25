import setuptools


setuptools.setup(
    name="socketrequests",
    version="0.01",
    author="WanderingWizard",
    author_email="86394469+WanderingWizards@users.noreply.github.com",
    description="A small HTTP requests package.",
    long_description="A small HTTP requests package.",
    long_description_content_type="text/markdown",
    url="https://github.com/WanderingWizards/SocketRequests",
    project_urls={
        "Bug Tracker": "https://github.com/WanderingWizards/SocketRequests/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3",
)
