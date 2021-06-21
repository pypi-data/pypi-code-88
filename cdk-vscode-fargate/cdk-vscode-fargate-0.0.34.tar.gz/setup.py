import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "cdk-vscode-fargate",
    "version": "0.0.34",
    "description": "cdk-vscode-fargate",
    "license": "Apache-2.0",
    "url": "https://github.com/mikeapted/cdk-vscode-fargate.git",
    "long_description_content_type": "text/markdown",
    "author": "Mike Apted<mike.apted@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/mikeapted/cdk-vscode-fargate.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "cdk_vscode_fargate",
        "cdk_vscode_fargate._jsii"
    ],
    "package_data": {
        "cdk_vscode_fargate._jsii": [
            "cdk-vscode-fargate@0.0.34.jsii.tgz"
        ],
        "cdk_vscode_fargate": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-certificatemanager>=1.106.1, <2.0.0",
        "aws-cdk.aws-ec2>=1.106.1, <2.0.0",
        "aws-cdk.aws-ecs-patterns>=1.106.1, <2.0.0",
        "aws-cdk.aws-ecs>=1.106.1, <2.0.0",
        "aws-cdk.aws-efs>=1.106.1, <2.0.0",
        "aws-cdk.aws-kms>=1.106.1, <2.0.0",
        "aws-cdk.aws-logs>=1.106.1, <2.0.0",
        "aws-cdk.aws-route53>=1.106.1, <2.0.0",
        "aws-cdk.aws-secretsmanager>=1.106.1, <2.0.0",
        "aws-cdk.core>=1.106.1, <2.0.0",
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
