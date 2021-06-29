from setuptools import find_packages, setup
from distutils.core import Extension

module = Extension("blendlib",
                    define_macros = [("MAJOR_VERSION", "1"),
                                     ("MINOR_VERSION", "0")],
                    include_dirs = ["/library"],
                    libraries = ["library/blendlib"],
                    library_dirs = ["/library"],
                    sources = ["library/blendlib.c"])

setup(
    name="photoblend2",
    version="0.0.2",
    url="https://github.com/aausek/PhotoBlend",
    description="Photoblend is a custom PyQt5 & C++ image editor app with blending mode features, filters and other"
                "manipulation options to render unique and creative images.",
    license="MIT",
    author="Team Senioritis",
    install_requires=["PySide2", "Pillow", "numpy", "wsl"],
    packages=find_packages(include=["library", "library.*"]),
    data_files=["library/blendlib.so"],
    ext_modules=[module],
    entry_points={"console_scripts": ["photoblend2=library.main:main"]},
)
