import json
import setuptools

kwargs = json.loads(
    """
{
    "name": "terraform-cdk-alicloud-k8s",
    "version": "0.0.2",
    "description": "terraform-cdk-alicloud-k8s",
    "license": "Apache-2.0",
    "url": "https://github.com/jialechan/terraform-cdk-alicloud-k8s.git",
    "long_description_content_type": "text/markdown",
    "author": "jialechan<jiale.chen@transsnet.com>",
    "bdist_wheel": {
        "universal": true
    },
    "project_urls": {
        "Source": "https://github.com/jialechan/terraform-cdk-alicloud-k8s.git"
    },
    "package_dir": {
        "": "src"
    },
    "packages": [
        "terraform-cdk-alicloud-k8s",
        "terraform-cdk-alicloud-k8s._jsii"
    ],
    "package_data": {
        "terraform-cdk-alicloud-k8s._jsii": [
            "terraform-cdk-alicloud-k8s@0.0.2.jsii.tgz"
        ],
        "terraform-cdk-alicloud-k8s": [
            "py.typed"
        ]
    },
    "python_requires": ">=3.6",
    "install_requires": [
        "cdktf>=0.4.1, <0.5.0",
        "constructs>=3.3.92, <4.0.0",
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
