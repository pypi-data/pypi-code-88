import pathlib
from setuptools import setup, find_packages

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

# This call to setup() does all the work
setup(
    name="Yolo_ED2_Demo",
    version="1.0.3",
    description="Run inference on Yolo Distribution Distillation model.",
    long_description=README,
    long_description_content_type="text/markdown",
    url="",
    author="cleverhans",
    author_email="maximilian.henne@iks.fraunhofer.de",
    license="Apache",
    classifiers=[
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python :: 3",
    ],
    packages=find_packages(),
    install_requires=["torch==1.6.0",
                      "torchvision==0.7.0",
                      "numpy==1.18.2",
                      "opencv-python==4.4.0.42",
                      "pycocotools==2.0.1",
                      "matplotlib==3.3.1",
                      ],
    python_requires=">=3.6",
)