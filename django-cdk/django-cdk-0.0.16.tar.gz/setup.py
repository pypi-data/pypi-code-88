import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "django-cdk",
    "version": "0.0.16",
    "description": "django-cdk",
    "license": "Apache-2.0",
    "url": "https://github.com/briancaffey/django-cdk.git",
    "long_description_content_type": "text/markdown",
    "author": "Brian Caffey<briancaffey2010@gmail.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/briancaffey/django-cdk.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "django_cdk",
        "django_cdk._jsii"
    ],
    "package_data": {
        "django_cdk._jsii": [
            "django-cdk@0.0.16.jsii.tgz"
        ],
        "django_cdk": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "aws-cdk.aws-autoscaling>=1.106.0, <2.0.0",
        "aws-cdk.aws-certificatemanager>=1.106.0, <2.0.0",
        "aws-cdk.aws-cloudformation>=1.106.0, <2.0.0",
        "aws-cdk.aws-cloudfront>=1.106.0, <2.0.0",
        "aws-cdk.aws-cloudwatch>=1.106.0, <2.0.0",
        "aws-cdk.aws-ec2>=1.106.0, <2.0.0",
        "aws-cdk.aws-ecr-assets>=1.106.0, <2.0.0",
        "aws-cdk.aws-ecr>=1.106.0, <2.0.0",
        "aws-cdk.aws-ecs-patterns>=1.106.0, <2.0.0",
        "aws-cdk.aws-ecs>=1.106.0, <2.0.0",
        "aws-cdk.aws-eks>=1.106.0, <2.0.0",
        "aws-cdk.aws-elasticache>=1.106.0, <2.0.0",
        "aws-cdk.aws-elasticloadbalancingv2>=1.106.0, <2.0.0",
        "aws-cdk.aws-events-targets>=1.106.0, <2.0.0",
        "aws-cdk.aws-events>=1.106.0, <2.0.0",
        "aws-cdk.aws-iam>=1.106.0, <2.0.0",
        "aws-cdk.aws-lambda>=1.106.0, <2.0.0",
        "aws-cdk.aws-logs>=1.106.0, <2.0.0",
        "aws-cdk.aws-rds>=1.106.0, <2.0.0",
        "aws-cdk.aws-route53-targets>=1.106.0, <2.0.0",
        "aws-cdk.aws-route53>=1.106.0, <2.0.0",
        "aws-cdk.aws-s3-deployment>=1.106.0, <2.0.0",
        "aws-cdk.aws-s3>=1.106.0, <2.0.0",
        "aws-cdk.aws-secretsmanager>=1.106.0, <2.0.0",
        "aws-cdk.aws-ssm>=1.106.0, <2.0.0",
        "aws-cdk.core>=1.106.0, <2.0.0",
        "cdk8s>=1.0.0.b11, <2.0.0",
        "constructs>=3.2.27, <4.0.0",
        "jsii>=1.29.0, <2.0.0",
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
