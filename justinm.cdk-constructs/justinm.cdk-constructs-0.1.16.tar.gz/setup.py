import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "justinm.cdk-constructs",
    "version": "0.1.16",
    "description": "@justinm/cdk-constructs",
    "license": "MIT",
    "url": "https://github.com/justinm/cdk-constructs.git",
    "long_description_content_type": "text/markdown",
    "author": "Justin McCormick<me@justinmccormick.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/justinm/cdk-constructs.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "justinm.constructs",
        "justinm.constructs._jsii",
        "justinm.constructs.infra",
        "justinm.constructs.management"
    ],
    "package_data": {
        "justinm.constructs._jsii": [
            "cdk-constructs@0.1.16.jsii.tgz"
        ],
        "justinm.constructs": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-budgets>=1.110.0, <2.0.0",
        "aws-cdk.aws-cloudtrail>=1.110.0, <2.0.0",
        "aws-cdk.aws-cloudwatch>=1.110.0, <2.0.0",
        "aws-cdk.aws-ec2>=1.110.0, <2.0.0",
        "aws-cdk.aws-iam>=1.110.0, <2.0.0",
        "aws-cdk.aws-logs>=1.110.0, <2.0.0",
        "aws-cdk.aws-route53>=1.110.0, <2.0.0",
        "aws-cdk.aws-s3>=1.110.0, <2.0.0",
        "aws-cdk.aws-sns>=1.110.0, <2.0.0",
        "aws-cdk.core==1.110.0",
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
        "License :: OSI Approved"
    ],
    "scripts": []
}
"""
)

with open("README.md", encoding="utf8") as fp:
    kwargs["long_description"] = fp.read()


setuptools.setup(**kwargs)
