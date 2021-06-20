import setuptools

setuptools.setup(
    name="eTouch",
    version="0.0.3",
    author="Ahmed Almalki",
    author_email="ahmed.s.malki@gmail.com",
    description="Automating CA service management",
    url="https://github.com/asajm/eTouch",
    project_urls={
        "Bug Tracker": "https://github.com/asajm/eTouch/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)