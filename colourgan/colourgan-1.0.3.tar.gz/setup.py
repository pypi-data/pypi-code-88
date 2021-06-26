import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="colourgan",
    version="1.0.3",
    author="Narender Nain",
    author_email="narenderkumarnain@gmail.com",
    description="GAN Based colouring model",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/narenderkumarnain/GAN-Apps",
    project_urls={
    },
    install_requires=['numpy','opencv-python==4.5.2.52' ,
                      'Pillow==8.2.0', 'torch==1.8.1','torchvision==0.9.1'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
)