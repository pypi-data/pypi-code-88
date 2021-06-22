from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

with open("requirements.txt") as fp:
    install_requires = fp.read()

setup(
    name="zyppnotify",
    version="0.1.2",
    author="Erfan Nariman, Melvin Folkers",
    author_email="erfan@zypp.io, melvin@zypp.io",
    description="Send users notifications through various platforms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords="python, notifications, teams, whatsapp, e-mail, sms",
    url="https://github.com/zypp-io/zyppnotify",
    packages=find_packages(),
    install_requires=install_requires,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    project_urls={
        "Bug Reports": "https://github.com/zypp-io/zyppnotify/issues",
        "Source": "https://github.com/zypp-io/zyppnotify",
    },
)
