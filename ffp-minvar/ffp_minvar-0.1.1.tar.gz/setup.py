import setuptools
from distutils.core import setup, Extension

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


shared_module = Extension('alg_lomv',
                    sources = ['src/alg_lomv.c'],
                    include_dirs= ['include'],
                    extra_compile_args=['-lm', '-lgsl', '-lgslcblas', '-g'])

# setuptools.setup
setup(
    name="ffp_minvar",
    version="0.1.1",
    author="Lucius Luo",
    author_email="lucius0228@gmail.com",
    description="rewritten python package of ffp_minvar algorithm",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/luciusluo/ffp_minvar",
    project_urls={
        "Bug Tracker": "https://github.com/luciusluo/ffp_minvar/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "lib"},
    packages=setuptools.find_packages(where="lib"),
    python_requires=">=3.6",
    include_package_data=True, # might delete later
    ext_modules = [shared_module]
)