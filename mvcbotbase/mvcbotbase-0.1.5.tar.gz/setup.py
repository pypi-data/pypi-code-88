from setuptools import setup

setup(
    name="mvcbotbase",
    version="0.1.5",
    packages=["mvcbotbase"],
    download_url=(
        "https://github.com/megahomyak/mvcbotbase/archive/v0.1.5.tar.gz"
    ),
    url="https://github.com/megahomyak/mvcbotbase",
    author="megahomyak",
    author_email="g.megahomyak@gmail.com",
    description="A base to make social network bots (generic)",
    install_requires=["simple_avk"]
)
