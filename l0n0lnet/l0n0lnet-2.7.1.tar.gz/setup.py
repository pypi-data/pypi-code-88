import setuptools
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="l0n0lnet",
    version="2.7.1",
    author="l0n0l",
    author_email="1038352856@qq.com",
    description="一个简单的高性能c++网络库",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://gitee.com/l00n00l/l0n0lnet",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=setuptools.find_packages(),
    python_requires='>=3.6',
    include_package_data=True,
    package_data={
        "": ["*.so"]
    },
    install_requires=[
        "cmake",
        "GitPython"
    ],
    entry_points={
        "console_scripts": [
            "l0n0lgenpass = l0n0lnet.commands:generate_pass_file",
            "l0n0ltsocks5client = l0n0lnet.commands:run_transform_socks5_client",
            "l0n0ltsocks5server = l0n0lnet.commands:run_transform_socks5_server",
            "l0n0lrserver = l0n0lnet.commands:run_reverse_server",
            "l0n0lrclient = l0n0lnet.commands:run_reverse_client",
            "l0n0ltcpproxy = l0n0lnet.commands:run_tcp_proxy_server",
            "l0n0lsocks5 = l0n0lnet.commands:run_socks5_server",
        ]
    }
)
