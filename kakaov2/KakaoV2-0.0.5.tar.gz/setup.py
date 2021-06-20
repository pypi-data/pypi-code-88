from setuptools import setup, find_packages

setup(
    name="KakaoV2",
    version="0.0.5",
    url="https://github.com/ULTRA0221/KakaoV2",
    author="ULTRA#0221",
    author_email="kakao@ultra0221.me",
    description="Kakaotalk LOCO/HTTP API protocol wrapper for python.",
    packages=["KakaoV2"],
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    install_requires=["pymongo", "requests", "pycryptodomex", "aiohttp"],
    zip_safe=False,
    classifiers=["License :: OSI Approved :: MIT License"]
)
