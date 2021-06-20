import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-ecrpublic-gc",
    "version": "0.1.30",
    "description": "Garbage collector for Amazon ECR public",
    "license": "Apache-2.0",
    "url": "https://github.com/pahudnet/cdk-ecrpublic-gc.git",
    "long_description_content_type": "text/markdown",
    "author": "Pahud Hsieh<pahudnet@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/pahudnet/cdk-ecrpublic-gc.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_ecrpublic_gc",
        "cdk_ecrpublic_gc._jsii"
    ],
    "package_data": {
        "cdk_ecrpublic_gc._jsii": [
            "cdk-ecrpublic-gc@0.1.30.jsii.tgz"
        ],
        "cdk_ecrpublic_gc": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-events-targets>=1.95.1, <2.0.0",
        "aws-cdk.aws-events>=1.95.1, <2.0.0",
        "aws-cdk.aws-iam>=1.95.1, <2.0.0",
        "aws-cdk.aws-lambda-nodejs>=1.95.1, <2.0.0",
        "aws-cdk.aws-lambda>=1.95.1, <2.0.0",
        "aws-cdk.aws-stepfunctions-tasks>=1.95.1, <2.0.0",
        "aws-cdk.aws-stepfunctions>=1.95.1, <2.0.0",
        "aws-cdk.core>=1.95.1, <2.0.0",
        "constructs>=3.2.27, <4.0.0",
        "jsii>=1.30.0, <2.0.0",
        "publication>=0.0.3"
    ],
    "classifiers": [
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Typing :: Typed",
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
