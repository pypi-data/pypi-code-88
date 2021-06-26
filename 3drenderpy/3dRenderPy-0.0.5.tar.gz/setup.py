import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="3dRenderPy",
    version="0.0.5",
    author="Ulysses Lynne",
    author_email="yufeilin@bennington.edu",
    description="This is an implementation of a ray tracer based on Jamis Buck's The Ray Tracer Challenge. It supports several primitives.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/woes-lynne/3DRenderPy",
    project_urls={
        "Bug Tracker": "https://github.com/woes-lynne/3DRenderPy/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
    install_requires=[
        "numpy>=1.19.5",
        "Pillow>=5.1.0"
    ]
)
