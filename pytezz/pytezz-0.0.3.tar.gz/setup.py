from setuptools import find_packages, setup




if __name__ == "__main__":
    setup(
        name="pytezz",
        version="0.0.3",
        description="pytezz",
        long_description="pytezz - a project of FAST Developer Community",
        long_description_content_type="text/markdown",
	url="https://github.com/fast-developers-community/PyTorch-Library/pytezz",
        author="daniyal shaiq",
        author_email="daniyalshaiq01@gmail.com",
        packages=find_packages(),
        include_package_data=True,
        install_requires=["torch>=1.6.0"],
        platforms=["linux", "unix"],
        python_requires=">3.5.2",
    )


