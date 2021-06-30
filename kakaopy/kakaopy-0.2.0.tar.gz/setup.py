from setuptools import setup, find_packages

# the setup script
setup(
    name="kakaopy",
    version = "0.2.0",
    description = "kakao search API customizing",
    long_description = open('README.md').read(),
    long_description_content_type = "text/markdown",
    url = "https://github.com/SeoJeongYeop/kakaopy",
    author = "Jeongyeop Seo",
    author_email="sjyswe99@gmail.com",
    license ="MIT",
    packages = find_packages(exclude=['tests']),
    zip_safe=False,
    classifiers = [
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],

)